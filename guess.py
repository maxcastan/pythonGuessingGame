#1/user/bin/env python
"""Max Castaneda, This program lets the user guess a number between 1-100
"""

def main():
    print "Guess a number between 1 and 100."
    randomNumber=random.randint(1,100) #create a random number from 1-100
    found=False  #flag variable, determines if a guess is true
    userGuess=input("Your guess: ") #user input

    while not found: #loop until user correctly guesses the number
        if userGuess==randomNumber:#correct guess
            print "Correct"
            found=True
        elif userGuess > randomNumber:#tell user where to guess next
            print "Guess Lower"
        else:
            print "Guess Higher"



if __name__=="__main__":
    main()
