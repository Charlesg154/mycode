#!/usr/bin/env python3
import random
# Winner is 2 out of 3
# computer needs to make a choice
# choices need to be evaluated
# print out the result (who won)


def main():
    """body of the game"""

    point=0 # Variable to keep track of user point
    cpoint=0 # Variable to keep track of CPU point

    while point != 4: # At the end of the game I'm going to set the point value to 4 to stop the game.

        choice= input("Rock, Paper, or Scissors?\n>")#Have user input their choice
        botchoice= random.choice(["rock", "paper", "scissors"])#Have CPU make their choice

        choice= choice.lower() # validates input by forcing input to be lower case

        #print choices
        print(f"You chose {choice}!\n")
        print(f"CPU chose {botchoice}!\n")

        if choice not in ["rock", "paper", "scissors"]:#If the user enters an invalid option, give CPU a point
            print("You entered an invalid choice, you lose(r)!")
            cpoint+=1

        elif choice == botchoice:#Draw, no point
            print("Draw")

        #Define win conditions.  Give user a point
        elif choice == "scissors" and botchoice == "paper":
            print("You win!")
            point+=1
        elif choice == "paper" and botchoice == "rock":
            print("You win!")
            point+=1
        elif choice == "rock" and botchoice == "scissors":
            print("You win!")
            point+=1
        
        #Anything else would be a loss.  Give cpu a point
        else:
            print("You lose!")
            cpoint+=1
        
        #Print current score
        print(f"Score is {point}/{cpoint}\n")

        #See if either user or CPU has meant winning score of two.
        #If so, print win or lose message and set point value to 4 to end the loop
        if point == 2:
            print("Congratulations!  You win the game!")
            point=4
        elif cpoint == 2:
            print("CPU wins the game!")
            point=4


main()

