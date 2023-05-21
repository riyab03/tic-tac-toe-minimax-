#intialozation of board
board={1:' ',2:' ',3:' ',
       4:' ',5:' ',6:' ',
       7:' ',8:' ',9:' '}


#printing the board
def printBoard(board):
    print(board[1]+'  |  '+board[2]+'  |  '+board[3])
    print('___|_____|___')
    print(board[4]+'  |  '+board[5]+'  |  '+board[6])
    print('___|_____|___')
    print(board[7]+'  |  '+board[8]+'  |  '+board[9])
    print('   |     |   ')
    print('\n')


print("GET READY TO PLAY WITH BOT !!")
name =(input("Enter the name of player:"))
printBoard(board)
print("Please enter between 1-9")


#method to check space is free
def spaceIsFree(position):
    if(board[position]==' '):
        return True
    else:
        return False


#method to check draw
def checkDraw():
    for key in board.keys():
        if (board[key]==' '):
            return False
    return True

#method to check whether win or not
def checkforwin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False



def checkmark(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

#method to insert the letter in board
def insertletter(letter,position):
    if spaceIsFree(position):
        board[position]=letter
        printBoard(board)
        
        if (checkforwin()):
            if letter=='X':
                print("BOT WINS!!")
                exit()
            else:
                print("WINNER IS "+name)
                exit()
        
        if(checkDraw()):
            print("DRAW!!")
            exit()
        return
    else:
        print("can't insert!Already filled..")
        position=int(input("Enter new position for 'O':"))
        insertletter(letter,position)
        return

player='0'
bot='X'

def playerMore():
    position =int(input("enter the position:"))
    insertletter(player,position)
    return

def compmov():
    bestScore=-1000
    bestmove =0
    for key in board.keys():
        if(board[key]==' '):
            board[key]=bot
            score =minimax(board,0,False)
            board[key]=' '
            if(score>bestScore):
                bestScore=score
                bestmove=key
    insertletter(bot,bestmove)
    return bestScore

def minimax(board,depth,ismaximizing):
    if (checkmark(bot)):
        return 1
    elif (checkmark(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (ismaximizing):
        bestScore = -800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore

global firstcomputermove
firstcomputermove=True

while not checkforwin():
    
    print("BOTS TURN :")
    compmov()
    print("YOUR TURN :")
    playerMore()