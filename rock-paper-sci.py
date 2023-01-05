#!/usr/bin/env python3
import random
# Winner is 2 out of 3
# computer needs to make a choice
# choices need to be evaluated
# print out the result (who won)


def main():
    """body of the game"""

    point=0
    cpoint=0

    while point != 4:
        choice= input("\nRock, Paper, or Scissors?\n>")
        botchoice= random.choice(["rock", "paper", "scissors"])

        choice= choice.lower() # validates input by forcing input to be lower case

      # uncomment these print functions to debug
        print(f"You chose {choice}!\n")
        print(f"CPU chose {botchoice}!\n")

        if choice not in ["rock", "paper", "scissors"]:
            print("You entered an invalid choice, you lose(r)!")
            cpoint+=1
        elif choice == botchoice:#Draw, no point
            print("Draw")
        elif choice == "scissors" and botchoice == "paper":
            print("You win!")
            point+=1
        elif choice == "paper" and botchoice == "rock":
            print("You win!")
            point+=1
        elif choice == "rock" and botchoice == "scissors":
            print("You win!")
            point+=1
        else:
            print("You lose!")
            cpoint+=1
        print(f"Score is {point}/{cpoint}")
        if point == 2:
            print("Congratulations!  You win the game!")
            point=4
        elif cpoint == 2:
            print("CPU wins the game!")
            point=4




    # user picked scissors... did they win or lose?

    ### ADD MORE HERE


main()

