nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49]
primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
primeLocations = [[0,4], [0,6], [2,0], [2,2], [2,6], [3,1], [3,3], [3,5], [4,4], [4,0], [5,1], [5,3], [5,5], [6,4], [6,5]]
allBoards = []
import copy

def test():
    for i in range(7):
        row = ""
        for j in range(7):
            if [j,i] in primeLocations:
                row = row + "x"
            else:
                row = row + "0"
        out.append(row)

    for i in range(7):
        print(out[6-i])

def genAllStarts():
    ret = []
    for i in range(7):
        for j in range(7):
            ret.append([i,j])
    return ret

def genEmptyBoard():
    emptyBoard = []
    for i in range(7):
        temp = []
        for j in range(7):
            temp.append(0)
        emptyBoard.append(temp)
    return emptyBoard

def genAllBoards():
    global primeLocations
    emptyBoard = genEmptyBoard()
    starts = genAllStarts()
    print(primeLocations)
    for start in starts:
        if(start not in primeLocations):
            print(start)
            newBoard = genEmptyBoard()
            newBoard[start[0]][start[1]] = 1
            genBoard(start, 2, newBoard)

def genBoard(location, num, board):
    global allBoards, primeLocations, primes
    if(location in primeLocations and num not in primes):
        return 0
    neighbors = getNeighbors(location)
    for neighbor in neighbors:
        x = neighbor[0]
        y = neighbor[1]
        if board[x][y] == 0:
            newBoard = copy.deepcopy(board)
            newBoard[x][y] = num #this might be backwards
            if(num == 49):
                allBoards.append(newBoard)
                printBoard(newBoard)
            else:
                genBoard(neighbor, num+1, newBoard)

def getNeighbors(cord):
    ret = []
    x = cord[0]
    y = cord[1]
    lowX = False
    lowY = False
    highX = False
    highY = False
    if x - 1 >= 0:
        ret.append([x-1,y])
    if y - 1 >= 0:
        ret.append([x,y-1])

    if x + 1 <= 6:
        ret.append([x+1,y])
    if y + 1 <= 6:
        ret.append([x,y+1])
    return ret

def printBoard(board):
    for i in board:
        for j in i:
            print(j, end = "\t")
        print("")
    print("")

print("udpates")
genAllBoards()
print(len(allBoards))
print(allBoards)


