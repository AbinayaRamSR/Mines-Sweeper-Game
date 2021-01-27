import random

def Generalmindsweeperboard(n, k):
    arr = [[0 for row in range(n)]for col in range(n)]
    for num in range(k):
        x = random.randint(0, n-1)
        y = random.randint(0, n-1)
        arr[y][x] = 'X'

        if(x>=1 and x<=n-1) and (y>=0 and y<=n-1):
            if(arr[y][x-1] != 'X'):    # center left
                arr[y][x-1] += 1

        if(x>=0 and x<=n-2) and (y>=0 and y<=n-1):
            if(arr[y][x+1] != 'X'):    # center right
                arr[y][x+1] += 1

        if(x>=0 and x<=n-1) and (y>=1 and y<=n-1):
            if(arr[y-1][x] != 'X'):    # center top
                arr[y-1][x] += 1

        if(x>=0 and x<=n-1) and (y>=0 and y<=n-2):
            if(arr[y+1][x] != 'X'):    # center bottom
                arr[y+1][x] += 1

        if(x>=1 and x<=n-1) and (y>=1 and y<=n-1):
            if(arr[y-1][x-1] != 'X'):   # top left
                arr[y-1][x-1] += 1

        if(x>=0 and x<=n-2) and (y>=0 and y<=n-2):
            if(arr[y+1][x+1] != 'X'):   # bottom right
                arr[y+1][x+1] += 1

        if(x>=0 and x<=n-2) and (y>=0 and y<=n-1):
            if(arr[y-1][x+1] != 'X'):   # top right
                arr[y-1][x+1] += 1

        if(x>=1 and x<=n-1) and (y>=0 and y<=n-2):
            if(arr[y+1][x-1] != 'X'):   # bottom left
                arr[y+1][x-1] += 1
    return arr

def Generalboard(n):
    arr = [['-' for row in range(n)]for col in range(n)]
    return arr

def CheckWon(map):
    for row in map:
        for cell in row:
            if cell == '-':
                return False
    return True

def DisplayBoard(map):
    for row in map:
        print (" ".join(str(cell) for cell in row))
        print ("")

def CheckRePlay(Score):
    print (" Your Score: ", Score)
    Option = input("Do you want to replay? Press 1: (0/1) ")
    if (Option == 0):
        return False
    return True

def StartGame():
    GameSatus = True
    while(GameSatus):
        Difficulty = input(" Choose Difficulty level ( 0, 1, 2) : ")
        if Difficulty == 0:
            n = 5
            k = 3
        elif Difficulty == 1:
            n = 6
            k = 8
        else:
            n = 8
            k = 20
        mindsweeperboard = Generalmindsweeperboard(n, k)
        FrontEndBoard = Generalboard(n)
        Score = 0
        while True:
            if (CheckWon(FrontEndBoard) == False):
                print ("Your turn to select: ")
                x = input(" x (1, 5) :")
                y = input(" y (1, 5) :")
                x = int(x)-1
                y = int(y)-1
                if (mindsweeperboard[y][x] == 'X'):
                    print ("Game Over !!")
                    DisplayBoard(mindsweeperboard)
                    GameSatus = CheckRePlay(Score)
                    break
                else:
                    FrontEndBoard[y][x] = mindsweeperboard[y][x]
                    DisplayBoard(FrontEndBoard)
                    Score += 1
            else:
                print ("You Lost ")
                DisplayBoard(FrontEndBoard)
                GameSatus = CheckRePlay(Score)
                break

if __name__ == "__main__":
    try:
        StartGame()
    except KeyboardInterrupt:
        print('\nEnd of Game. Bye Bye!')
