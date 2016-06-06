#William Zhang

import random

#Globcal color variable 
COLORS=['red','orange','yellow','green','blue','purple']

#Generate random color
def hidden_color():
    #hidden color list
    hiddenColor=[]
    #Generate random color
    for i in range(4):
        randColor=COLORS[random.randint(0,5)]
        hiddenColor.append(randColor)
    return hiddenColor

#Opponent's guess
def opponent_guess():
    #opponent guess list
    opponentGuess=[]
    isInt = True
    print("Make a guess of four colors:")
    print("0 - red")
    print("1 - orange")
    print("2 - yellow")
    print("3 - green")
    print("4 - blue")
    print("5 - purple")
    #Get opponent guess
    for i in range(4):
        try:
            guess = int(input("Choose a color(0-5): "))
        except ValueError:
            isInt = False
            guess = -1
        while(guess < 0 or guess > 5 or isInt == False):
            isInt = True
            try:
                guess = int(input("Invalid input. Choose a color(0-5): "))
            except ValueError:
                isInt = False
        opponentGuess.append(COLORS[guess])
        print(opponentGuess)
    print("Your guess is: \n"+str(opponentGuess))
    return opponentGuess

#The clue
def the_clue(hiddenColor, guess):
    #tempoary color and guess list
    tempHiddenColor=hiddenColor[:]
    tempGuess=guess[:]
    #Get the clue
    for i in range(4):
        if(tempGuess[i]==tempHiddenColor[i]):
            tempGuess[i]=''
            tempHiddenColor[i]=''
            print("correct color and position")
    for i in range(4):
        for j in range(4):
            if(tempGuess[i]!='' or tempHiddenColor[j]!=''):
                if(tempGuess[i]==tempHiddenColor[j]):
                    tempHiddenColor[j]=''
                    print("correct color, wrong position")

#The main
def main():
   #initalized hidden color 
    hiddenColor=hidden_color()
    print(hiddenColor)
    #counter and boolean
    i=0
    correctGuess = False
    #tries
    while(i < 10 and correctGuess == False):
        opponentGuess=opponent_guess()
        if(opponentGuess == hiddenColor):
            correctGuess = True
            print("You win")
        else:
            the_clue(hiddenColor,opponentGuess)
        if(i==9):
            print("You lose")
        i+=1

    
    

