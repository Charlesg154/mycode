#!/usr/bin/env python3

"""
PROJECT EXPECTATIONS:

    The program executes cleanly without error and meets its intended purpose.
    The program has been designed to accommodate human errors.
    The program is designed as efficiently as possible (do more with less!)
    The program’s output is easy to read and is presented well (and free of spelling errors)
    
    Wherever possible, the program follows PEP 8 standards:
        Keep code inside of functions
        Indent consistently (4 spaces)
        title/purpose of script at top of document
        Comment your code well, and often!

"""
"""
RPG PROJECT EXPECTATIONS

    Add additional rooms.
    Count how many "moves" the player has made.
    Find a way to add a description of each room that describes every direction you can go.
    Find a way to have multiple items inside the same room.
    Find a way to add descriptions to items that display when the item is picked up.
    Create alternate win/loss scenarios.
    Add more verbs! What else can your player do besides "get" and "go"?
    Make a trapdoor. Once you go through it you can't go back that way!
    Make a "teleport to" command that will put you in any room!
    Find a way to survive your encounter with the monster!
    Labyrinth- use the rooms list/dict model to create a maze! Life-threatening traps are always a plus.
    Combat- create a function that, when triggered, enters combat mode. Player/monster
        health & damage must be calculated and win/lose conditions created!
    Riddles- create a function that, when triggered, asks the player a series of riddles that may return
        some reward or punishment upon failure!
    Crushing Walls- create a function that, when triggered, puts our hero in a room with gradually closing
        walls. Implement a timer that will run out unless they find the escape solution!
    All-knowing Sphinx- create a function that, when triggered, a cat statue gives you a random cat
        fact from the cat facts API!
    Puzzle- create a function that, when triggered, engages the player in some manner of diabolical
        puzzle where failure is... unhealthy!
    Class- build a Player class object to internalize (and therefore replace) existing procedural
        player characteristics: inventory, health, spells, etc. BUT ALSO implement player stats that
        def __init__(self) upon creation. Create a method that triggers a level-up message where users
        can allocate points to strength, intelligence, and speed.

"""
"""
The purpose of the project is to present RPG concepts.  User will control a character and need to
collect items and avoid game ending scenarios via clues presented.  One challenge I'd like to present
is reading and writing save data for the user to start and end the game when desired without losing
progress
"""

import time

ROOMS = {
        "Hall": {
            "South" : "Kitchen",
            "East"  : "Dining Room",
            "Item"  : "Key"},
        "Kitchen" : {
            "North" : "Hall",
            "Item"  : "Monster"},
        "Dining Room": {
            "West"  : "Hall",
            "South" : "Garden",
            "Item"  : "Green Herb"},
        "Garden": {
            "North" : "Dining Room"}
        }
LOC="Hall"


def talk(text, spd=0):
    for i in text:
        time.sleep(spd)
        print(i, end="", flush = True)
    print(flush = True)
        
def main():
    talk("Welcome",0.1)

if __name__== "__main__":    
    main()
