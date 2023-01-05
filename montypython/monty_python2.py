#!/usr/bin/env python3

round = 0
answer = " "

while round < 3 and answer != "Brian" and answer != "Shrubbery":
    round +=1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer = answer.title()
    if answer == "Brian":
        print("Correct!")
    elif answer == "Shrubbery":
        print("You gave the secret answer!")
    elif round ==3:
        print("Sorry, the answer was Brian.")
    else:
        print("Sorry.  Try again!")
