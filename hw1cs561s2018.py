'''CSCI561 HW1
Student Name:YING LIU
Student ID:4524943517
Email:liu423@usc.edu'''

import sys
import os

#global variable nextMove record the next move position
nextMove = ''
#global variable is to record current root value
curRootVal = float("-inf")
#global varaiable record how many state have already visited
nodeVisited = 1
def miniMaxPlay(curPlayer, depth, initialMatrix, rowWeight):
    #print(curPlayer)
    totalDepth = depth
    player = curPlayer
    return miniMaxMax(player, initialMatrix, 0, totalDepth, 0, rowWeight)

def miniMaxMax(me,curMatrix,curDepth,totalDepth,passCount,rowWeight):
    global nodeVisited
    global curRootVal
    global nextMove
    bestVal = float("-inf")
    if me == "Star":
        opponent = "Circle"
    else:
        opponent = "Star"
    validMoves = getValidMoves(curMatrix, me)
    if haveOne(curMatrix,me):
        if len(validMoves) ==0 and curDepth !=totalDepth:
            if passCount == 2:
                result = getValues(curMatrix,rowWeight)
                if me=='Star':
                    return result
                else:
                    return -result
            passCount = passCount+1
            nodeVisited = nodeVisited+1
            curBoard = boardDuplicate(curMatrix)
            tempVal = miniMaxMin(opponent,curBoard,curDepth+1,totalDepth,passCount,rowWeight)
            bestVal =  max(bestVal,tempVal)
            return tempVal
         # Reach the depth
        if curDepth == totalDepth:
            val = getValues(curMatrix,rowWeight)
            if me=='Star':
                return val
            else:
                return -val
        # Recursive run
        for num in range(0,len(validMoves)):
            #print(len(validMoves))
            passCount = 0
            nodeVisited = nodeVisited+1
            curBoard = boardDuplicate(curMatrix)
            nextStep = validMoves[num]
            curBoard2 = changeBoard(curBoard,me,nextStep)
            temp = miniMaxMin(opponent,curBoard2,curDepth+1,totalDepth,passCount,rowWeight)
            bestVal = max(bestVal,temp)
            if curDepth == 0:
                if curRootVal != bestVal:
                    curRootVal = bestVal
                    nextMove = validMoves[num]

        return bestVal
    else:
        if me=='Star':
            return getValues(curMatrix,rowWeight)
        else:
            return -getValues(curMatrix,rowWeight)

def miniMaxMin(me,curMatrix,curDepth,totalDepth,passCount,rowWeight):
    global nodeVisited
    global curRootVal
    global nextMove
    bestVal =  float("inf")
    if me == "Star":
        opponent = "Circle"
    else:
        opponent = "Star"
    validMoves = getValidMoves(curMatrix, me)
    if haveOne(curMatrix,me):
        if len(validMoves) ==0 and curDepth !=totalDepth:
            if passCount == 2:
                result = getValues(curMatrix,rowWeight)
                if me=='Circle':
                    return result
                else:
                    return -result
            passCount = passCount+1
            nodeVisited = nodeVisited+1
            curBoard = boardDuplicate(curMatrix)
            tempVal = miniMaxMax(opponent,curBoard,curDepth+1,totalDepth,passCount,rowWeight)
            bestVal =  min(bestVal,tempVal)
            return tempVal
         # Reach the depth
        if curDepth == totalDepth:
            val = getValues(curMatrix,rowWeight)
            if me == 'Circle':
                return val
            else:
                return -val
        # Recursive run
        for num in range(0,len(validMoves)):
            passCount = 0
            nodeVisited = nodeVisited+1
            curBoard = boardDuplicate(curMatrix)
            nextStep = validMoves[num]
            curBoard2 = changeBoard(curBoard,me,nextStep)
            temp = miniMaxMax(opponent,curBoard2,curDepth+1,totalDepth,passCount,rowWeight)
            bestVal = min(bestVal,temp)
            if curDepth==0:
                if curRootVal != bestVal:
                    curRootVal = bestVal
                    nextMove = validMoves[num]
        return bestVal
    else:
        if me == 'Circle':
            return getValues(curMatrix,rowWeight)
        else:
            return -getValues(curMatrix,rowWeight)

def alphaBetaPlay(curPlayer, depth, initialMatrix, rowWeight):
    alphaInit = float("-inf")
    betaInit = float("inf")
    totalDepth = depth
    player = curPlayer
    val = alphaBetaMax(player,initialMatrix,alphaInit,betaInit,0,totalDepth,0,rowWeight)
    return val


#function alphaBetaMax returns the utility value of end state
def alphaBetaMax(me,curMatrix,a,b,curDepth,totalDepth,passCount,rowWeight):
    global nodeVisited
    global curRootVal
    global nextMove
    bestVal = float("-inf")
    if me == "Star":
        opponent = "Circle"
    else:
        opponent = "Star"
    #get a list of valid moves from current board
    validMoves = getValidMoves(curMatrix,me)
    #if there are no pieces on the board
    #if there are no valid moves but have at least one pieces
    if haveOne(curMatrix,me):
        if len(validMoves) ==0 and curDepth !=totalDepth:
            if passCount == 2:
                result = getValues(curMatrix,rowWeight)
                if me=='Star':
                    return result
                else:
                    return -result
            passCount = passCount+1
            nodeVisited = nodeVisited+1
            curBoard = boardDuplicate(curMatrix)
            tempVal = alphaBetaMin(opponent,curBoard,a,b,curDepth+1,totalDepth,passCount,rowWeight)
            bestVal =  max(bestVal,tempVal)
            a = max(a,bestVal)
            return tempVal
         # Reach the depth
        if curDepth == totalDepth:
            val = getValues(curMatrix,rowWeight)
            if me=='Star':
                return val
            else:
                return -val
        # Recursive run
        for num in range(0,len(validMoves)):
            passCount = 0
            nodeVisited = nodeVisited+1
            curBoard = boardDuplicate(curMatrix)
            nextStep = validMoves[num]
            curBoard2 = changeBoard(curBoard,me,nextStep)
            temp = alphaBetaMin(opponent,curBoard2,a,b,curDepth+1,totalDepth,passCount,rowWeight)
            bestVal = max(bestVal,temp)
            a = max(a,bestVal)
            if curDepth == 0:
                if curRootVal != bestVal:
                    curRootVal = bestVal
                    nextMove = validMoves[num]

            if b<=a:
                break
        return bestVal
    else:
        if me=='Star':
            return getValues(curMatrix,rowWeight)
        else:
            return -getValues(curMatrix,rowWeight)





def alphaBetaMin(me,curMatrix,a,b,curDepth,totalDepth,passCount,rowWeight):
    global nodeVisited
    global curRootVal
    global nextMove
    bestVal =  float("inf")
    if me == "Star":
        opponent = "Circle"
    else:
        opponent = "Star"
    validMoves = getValidMoves(curMatrix, me)
    if haveOne(curMatrix,me):
        if len(validMoves) ==0 and curDepth !=totalDepth:
            if passCount == 2:
                result = getValues(curMatrix,rowWeight)
                if me=='Circle':
                    return result
                else:
                    return -result
            passCount = passCount+1
            nodeVisited = nodeVisited+1
            curBoard = boardDuplicate(curMatrix)
            tempVal = alphaBetaMax(opponent,curBoard,a,b,curDepth+1,totalDepth,passCount,rowWeight)
            bestVal =  min(bestVal,tempVal)
            b = min(b,bestVal)
            return tempVal
         # Reach the depth
        if curDepth == totalDepth:
            val = getValues(curMatrix,rowWeight)
            if me == 'Circle':
                return val
            else:
                return -val
        # Recursive run
        for num in range(0,len(validMoves)):
            passCount = 0
            nodeVisited = nodeVisited+1
            curBoard = boardDuplicate(curMatrix)
            nextStep = validMoves[num]
            curBoard2 = changeBoard(curBoard,me,nextStep)
            temp = alphaBetaMax(opponent,curBoard2,a,b,curDepth+1,totalDepth,passCount,rowWeight)
            bestVal = min(bestVal,temp)
            b = min(b,bestVal)
            if curDepth==0:
                if curRootVal != bestVal:
                    curRootVal = bestVal
                    nextMove = validMoves[num]
            if b<=a:
                break
        return bestVal
    else:
        if me == 'Circle':
            return getValues(curMatrix,rowWeight)
        else:
            return -getValues(curMatrix,rowWeight)


def getValidMoves(board,curMe):
    allValidMoves = []
    if curMe == 'Star' :
       for x in range(1,8):
           for y in range(8):
               #find the start point for star player
               if board[x][y].startswith('S'):
                   if x==1:
                       for xdirection, ydirection in [[-1, -1], [-1, 1]]:
                           xend = x + xdirection
                           yend = y + ydirection
                           if not isOnBoard(xend,yend):
                               continue
                           if board[xend][yend].startswith('C'):
                               continue
                           startPoint = translateToPosition(x,y)
                           endPoint = translateToPosition(xend,yend)
                           allValidMoves.append(startPoint+'-'+endPoint)
                   elif x==2:
                       for xdirection, ydirection in [[-2, -2], [-2, 2]]:
                           xend = x + xdirection
                           yend = y + ydirection
                           if not isOnBoard(xend,yend):
                               continue
                           if board[xend][yend].startswith('C'):
                               continue
                           if ydirection == -2:
                               if board[x-1][y-1].startswith('C'):
                                   startPoint = translateToPosition(x,y)
                                   endPoint = translateToPosition(xend,yend)
                                   allValidMoves.append(startPoint+'-'+endPoint)
                           else:
                               if board[x-1][y+1].startswith('C'):
                                   startPoint = translateToPosition(x, y)
                                   endPoint = translateToPosition(xend, yend)
                                   allValidMoves.append(startPoint + '-' + endPoint)
                       for xdir, ydir in [[-1, -1], [-1, 1]]:
                           xend2 = x + xdir
                           yend2 = y + ydir
                           if not isOnBoard(xend2,yend2):
                               continue
                           if board[xend2][yend2] == '0':
                               startPoint = translateToPosition(x, y)
                               endPoint = translateToPosition(xend2, yend2)
                               allValidMoves.append(startPoint + '-' + endPoint)
                   else:
                       for xdirection, ydirection in [[-2, -2], [-2, 2]]:
                           xend = x + xdirection
                           yend = y + ydirection
                           if not isOnBoard(xend,yend):
                               continue
                           if board[xend][yend] == '0':
                               if ydirection == -2:
                                   if (board[x - 1][y - 1].startswith('C')):
                                       startPoint = translateToPosition(x, y)
                                       endPoint = translateToPosition(xend, yend)
                                       allValidMoves.append(startPoint + '-' + endPoint)
                               else:
                                   if (board[x - 1][y + 1].startswith('C')):
                                       startPoint = translateToPosition(x, y)
                                       endPoint = translateToPosition(xend, yend)
                                       allValidMoves.append(startPoint + '-' + endPoint)
                       for xdir, ydir in [[-1, -1], [-1, 1]]:
                           xend2 = x + xdir
                           yend2 = y + ydir
                           if not isOnBoard(xend2,yend2):
                               continue
                           if board[xend2][yend2] == '0':
                               startPoint = translateToPosition(x, y)
                               endPoint = translateToPosition(xend2, yend2)
                               allValidMoves.append(startPoint + '-' + endPoint)
    else:
        for x in range(0, 7):
            for y in range(8):
                # find the start point for circle player
                if board[x][y].startswith('C'):
                    if x == 6:
                        for xdirection, ydirection in [[1, -1], [1, 1]]:
                            xend = x + xdirection
                            yend = y + ydirection
                            if not isOnBoard(xend, yend):
                                continue
                            if board[xend][yend].startswith('S'):
                                continue
                            startPoint = translateToPosition(x, y)
                            endPoint = translateToPosition(xend, yend)
                            allValidMoves.append(startPoint + '-' + endPoint)
                    elif x == 5:
                        for xdirection, ydirection in [[2, -2], [2, 2]]:
                            xend = x + xdirection
                            yend = y + ydirection
                            if not isOnBoard(xend, yend):
                                continue
                            if board[xend][yend].startswith('S'):
                                continue
                            if ydirection == -2:
                                if (board[x + 1][y - 1].startswith('S')):
                                    startPoint = translateToPosition(x, y)
                                    endPoint = translateToPosition(xend, yend)
                                    allValidMoves.append(startPoint + '-' + endPoint)
                            else:
                                if (board[x + 1][y + 1].startswith('S')):
                                    startPoint = translateToPosition(x, y)
                                    endPoint = translateToPosition(xend, yend)
                                    allValidMoves.append(startPoint + '-' + endPoint)
                        for xdir, ydir in [[1, -1], [1, 1]]:
                            xend2 = x + xdir
                            yend2 = y + ydir
                            if not isOnBoard(xend2, yend2):
                                continue
                            if board[xend2][yend2] == '0':
                                startPoint = translateToPosition(x, y)
                                endPoint = translateToPosition(xend2, yend2)
                                allValidMoves.append(startPoint + '-' + endPoint)
                    else:
                        for xdirection, ydirection in [[2, -2], [2, 2]]:
                            xend = x + xdirection
                            yend = y + ydirection
                            if not isOnBoard(xend, yend):
                                continue
                            if board[xend][yend] == '0':
                                if ydirection == -2:
                                    if (board[x + 1][y - 1].startswith('S')):
                                        startPoint = translateToPosition(x, y)
                                        endPoint = translateToPosition(xend, yend)
                                        allValidMoves.append(startPoint + '-' + endPoint)
                                else:
                                    if (board[x + 1][y + 1].startswith('S')):
                                        startPoint = translateToPosition(x, y)
                                        endPoint = translateToPosition(xend, yend)
                                        allValidMoves.append(startPoint + '-' + endPoint)
                        for xdir, ydir in [[1, -1], [1, 1]]:
                            xend2 = x + xdir
                            yend2 = y + ydir
                            if not isOnBoard(xend2, yend2):
                                continue
                            if board[xend2][yend2] == '0':
                                startPoint = translateToPosition(x, y)
                                endPoint = translateToPosition(xend2, yend2)
                                allValidMoves.append(startPoint + '-' + endPoint)
    return allValidMoves



def changeBoard(board,curMe,nextStep):
    position = nextStep.split('-')
    startPosition = position[0]
    endPosition = position[1]
    startX = translateToX(startPosition)
    startY = translateToY(startPosition)
    endX = translateToX(endPosition)
    endY = translateToY(endPosition)
    if curMe == 'Star':
        found = 'S'
    else:
        found = 'C'
    if abs(endX-startX)==2 :
        midX = (startX + endX) / 2
        midY = (startY + endY) / 2
        if board[endX][endY]=='0':
            board[endX][endY] = found+'1'
            board[midX][midY] = '0'
            board[startX][startY] = '0'
        else:
            res = board[endX][endY]
            val = int(res[1])+1
            board[endX][endY] = found+str(val)
            board[midX][midY] = '0'
            board[startX][startY] = '0'
    else:
        if board[endX][endY] == '0':
            board[endX][endY] = found+'1'
            board[startX][startY] = '0'
        else:
            res = board[endX][endY]
            val = int(res[1]) + 1
            board[endX][endY] = found + str(val)
            board[startX][startY] = '0'
    return board







def translateToPosition(x,y):
    letters = ['H','G','F','E','D','C','B','A']
    node = letters[x] + '%d'%(y+1)
    return node

def translateToX(res):
    if res[0]=='H':
        return 0
    elif res[0]=='G':
        return 1
    elif res[0]=='F':
        return 2
    elif res[0]=='E':
        return 3
    elif res[0]=='D':
        return 4
    elif res[0]=='C':
        return 5
    elif res[0]=='B':
        return 6
    else:
        return 7

def translateToY(res):
     val=int(res[1])-1
     return val

def haveOne(board,curPlayer):
    found = ''
    if curPlayer=='Star':
        found = 'S'
    else:
        found = 'C'
    for x in range(8):
        for y in range(8):
            if board[x][y].startswith(found):
                return True
    return False

def getValues(board,rowValue):
    starScore = 0
    circleScore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y].startswith('S'):
               number = board[x][y]
               num = int(number[1])
               starScore =starScore + num*int(rowValue[7-x])
            if board[x][y].startswith('C'):
               number = board[x][y]
               num = int(number[1])
               circleScore =circleScore + num*int(rowValue[x])
    weight = 0
    weight = starScore - circleScore
    return weight



def isOnBoard(x,y):
    return x>=0 and x<=7 and y>=0 and y<=7

def boardDuplicate(board):
    temp = [
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
    ]
    for x in range(8):
        for y in range(8):
            temp[x][y] = board[x][y]
    return temp

def main():
    global nextMove
    global nodeVisited
    matrix = [
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
    ]

    originalBoard = [
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '0', '0', '0'],
    ]
    #read the input file input.txt
    with open('input1.txt') as f:
        content = f.read().splitlines()
    curplayer = content[0]
    algorithm = content[1]
    depth = int(content[2])
    for i in range(3,11):
        newList =  list(content[i].split(","))
        for j in range(0,8):
            if matrix[i-3][j]!= newList[j]:
                matrix[i-3][j] = newList[j]
                originalBoard[i-3][j] = newList[j]
    newWeight = list(content[11].split(","))

    farSightedValue = 0
    nextUtility = 0

    if(algorithm=="MINIMAX"):
        farSightedValue = miniMaxPlay(curplayer, depth, matrix, newWeight)
    else:
        farSightedValue = alphaBetaPlay(curplayer, depth, matrix, newWeight)
    if nextMove == '':
        tempBoard = originalBoard
        nextMove = 'pass'
        if(curplayer =='Star'):
            nextUtility = getValues(tempBoard,newWeight)
        else:
            nextUtility = -getValues(tempBoard,newWeight)
    else:
        tempBoard = originalBoard
        newBoard = changeBoard(tempBoard,curplayer,nextMove)
        if (curplayer == 'Star'):
            nextUtility = getValues(newBoard, newWeight)
        else:
            nextUtility = -getValues(newBoard, newWeight)
    finalResult = ''
    finalResult = nextMove + '\n' + str(nextUtility) + '\n' + str(farSightedValue) + '\n' + str(nodeVisited)
    outfile = open('output.txt','w')
    outfile.write(finalResult)

main()
