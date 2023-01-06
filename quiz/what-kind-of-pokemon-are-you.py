#!/usr/bin/env python3
"""
COMPLETE A POKEMON QUIZ.
"""

import random #We'll need this module to shuffle the order of questions

#Dictionary for Pokémon questions you'll be asked
quiz={1:
    {"Question":"Which color is your favorite?",
        "Charmander":"Red",
        "Squirtle":"Blue",
        "Bulbasaur":"Green",
        "Pikachu":"Yellow"},
    2:
    {"Question":"What is your favorite climate?",
        "Pikachu":"Doesn’t matter as long as I can stretch and walk on my own!",
        "Bulbasaur":"Surrounded by Nature!  I wanna feel the grass between my toes.",
        "Squirtle":"Anywhere with water leaves me feeling nice and refreshed.",
        "Charmander":"Hot and dry!  Keep that rain away from me!"},
    3:
    {"Question":"How do you do the things you do?",
        "Bulbasaur":"The only way that number one should!",
        "Squirtle":"I like to be slick!",
        "Charmander":"Make one wrong move and I will kick your grass",
        "Pikachu":"Pika?"}
    }

def main():
    """
    Main function
    """
    print("\nWelcome to the Pokémon challenge!  What kind of pokemon are you?!")
    print("Let's begin!")#Welcome the user

    Q=1 # This variable will be set to a specific dictionary key as we go
    turn=1 # This value will increment each round and adjust the above Q
    bulb=0 # This is a score to determine how much you're like Bulbasaur
    squirt=0 # This is a score to determine how much you're like Squirtle
    charm=0 # This is a score to determine how much you're like Charmander
    pika=0 # This is a score to determine how much you're like Pikachu

    while True: #Main loop that will occur as long as the user is playing

        Q=quiz.get(turn,False)#Starting with a default of 1, set Q as a specific key in the dictionary
                        #Also return false if question number doesn't exist.
                        #This will allow you to play as long as there are questions

        if Q==False: #Q = False signifies there are no more questions and thus the end of the game

            print("\nCONGRATULATIONS ON COMPLETING THE QUIZ!  Now, we're going to look at you and ask...")
            print("WHO'S THAT POKEMON?!\n")#Congratulate for completing

            #Tally scores against each other to see who has the highest value.  Declare winner.
            #Establish asc value as file name we're going to attempt to open later
            asc=''
            if bulb > squirt and bulb > charm and bulb > pika:
                print("IT'S BULBASAUR!")
                asc = 'bulb.txt'
            elif squirt > bulb and squirt> charm and squirt > pika:
                print("IT'S SQUIRTLE!")
                asc = 'squirt.txt'
            elif charm > squirt and charm > bulb and charm > pika:
                print("IT'S CHARMANDER!")
                asc = 'charm.txt'
            elif pika > squirt and pika > charm and pika > bulb:
                print("IT'S PIKACHU!")
                asc = 'pika.txt'

            else: #If no one has a higher score than everyone else.  We're going to give a unique victory of Ditto
                print("IT'S DITTO!?")
                asc = 'ditto.txt'

            #asc = 'BADFILENAME.BLAH' #Uncomment this if you want to test error

            try:#We're going to try to open the ascii art file if it exist
                with open(asc, "r") as f:
                    print(f.read())
                """
                f = open(asc)#Open the file named whatever we saved to the asc variable
                content = f.read()#Create a variable called content and save the file's contents to it
                print(content)#Print out content
                f.close()
                """
            except Exception as err:
                print("Sorry!  This file doesn't exist in your directory!", err)

            break #End the loop and thus the game

        pokelist=["Bulbasaur","Squirtle","Charmander","Pikachu"]
        random.shuffle(pokelist)#Generate a list of the Pokemon's names and shuffle their order
                                #These names correlates to our dictionary keys

        choice="" #Variable for our new upcoming loop
        while choice=="": #New loop.  This is for the player input.  If they fail to enter properly, they'll repeat

            print("\n", Q.get("Question"),"  (Pick an option, A - D)", sep="")#Get the value for the "Question" key from current Q#

            #Generate the values for the random pokemon key as designated on our random assorted list.
            #These values will be the question answers that the user is being asked.  They are preceeded with A, B, C, and D
            print("A. ", Q.get(pokelist[0]))
            print("B. ", Q.get(pokelist[1]))
            print("C. ", Q.get(pokelist[2]))
            print("D. ", Q.get(pokelist[3]))

            choice=(input(">> ")).capitalize()#Capitalize whatever choice is made
            point=""#Establish point variable.  We'll need this to figure out which pokemon made this round

            #Take the pokemon from the random list assortment that correlates with the answer you chose.
            #Set that pokemon's name as the point variable
            if choice=="A":
                choice=Q.get(pokelist[0])
                point=pokelist[0]
            elif choice=="B":
                choice=Q.get(pokelist[1])
                point=pokelist[1]
            elif choice=="C":
                choice=Q.get(pokelist[2])
                point=pokelist[2]
            elif choice=="D":
                choice=Q.get(pokelist[3])
                point=pokelist[3]

            else: #Any value that wasn't A, B, C, or D is an incorrect value.  Reset the choice variable and have the user repeat
                print("Input was incorrect!  Please try reenter.")
                choice=""

        #Finally, use the name assigned to point to figure out which score to adjust.  Increment corresponding var by 1.
        if point=="Bulbasaur":
            bulb+=1
        elif point=="Squirtle":
            squirt+=1
        elif point=="Charmander":
            charm+=1
        else:
            pika+=1

        turn+=1 #Increment turn value.  This will allow a new question to be generated as long as one exists next round.


main()


