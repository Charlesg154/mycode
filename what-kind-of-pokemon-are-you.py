#!/usr/bin/env python3

#Dictionary for Pokémon
quiz={"Question 1":
    {"Which color is your favorite?": "Question",
        "Red": "Charmander",
        "Blue": "Squirtle",
        "Green": "Bulbasaur",
        "Yellow": "Pikachu"},
    "Question 2":
    {"What is your favorite climate?": "Question",
        "Doesn’t matter as long as I can stretch and walk on my own!": "Pikachu",
        "Surrounded by Nature!  I wanna feel the grass between my toes.": "Bulbasaur",
        "Anywhere with water leaves me feeling nice and refreshed.": "Squirtle",
        "Hot and dry!  Keep that rain away from me!": "Charmander"},
    "Question 3":
    {"How do you do the things you do?": "Question",
        "The only way that number one should!": "Bulbasaur",
        "I like to be slick!": "Squirtle",
        "Make one wrong move and I will kick your grass": "Charmander",
        "Pika?": "Pikachu"}
    }

bulba=""
squira=""
charma=""
pikaa=""

def main():
    x=input("What variable would you like to check?\n>")
    x=x.upper()
    if(x=="B"):
        print(bulba)
    elif(x=="S"):
        print(squira)
    elif(x=="C"):
        print(charma)
    elif(x=="P"):
        print(pikaa)
    elif(x=="Q"):
        print(quiz)
    else:
        print(quiz["Question 1"])
        print("Goodbye")

main()

#display()
#    f = open('/path/to/file.txt', 'r')

