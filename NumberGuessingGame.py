import random

appRun = True
luckyNumber = random.randint(1,9)
attempts = 0

def getRand():
    global luckyNumber
    luckyNumber = random.randint(1,9)

def getInp():    
    LoopRun = True
    value = None

    while LoopRun:
        print("")
        inp = input("Play Again?(Y/N)")
        if inp == "Y":            
            value = True
            LoopRun = False            
        elif inp == "N":
            value = False            
            LoopRun = False
        else:
            print("Input not Recognised")    
    return value

def Retry(mode):    
    global attempts
    global appRun 
    if mode == 1:
        print("Booyah! You Guessed it right")        
    elif mode == 0:
        print("You Lost! You are out of chances")    
    inp = getInp()   
    if inp:
        getRand()
        attempts = 0
    else:
        appRun = False

while appRun:
    guessedNumber = input("Guess The Number: ")
    if int(guessedNumber) == luckyNumber:        
        Retry(1)
    else:
        print("Oops! It went wrong")
        print("")
        attempts += 1
    if attempts > 4:
        Retry(0)
        
print("Quiting.......")