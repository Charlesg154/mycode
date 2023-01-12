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
The purpose of the project is to present RPG concepts.  User will control a character and need to
collect items and avoid game ending scenarios via clues presented.  One challenge I'd like to present
is reading and writing save data for the user to start and end the game when desired without losing
progress
"""

from time import sleep #Sleep function required for various delays
from threading import Timer #Timer function required for quick-time events

"""GLOBAL VARIABLES"""
HURRY=5 #We will use this variable for our quick time events.  It's read by multiple fuunctions simultaneously so we need it to be global
LOC="HALL" #We will use this variable to annotate our current location


"""Each room and how they interconnect as a dictionary"""
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


"""The Layout of the Map.  The player will later have view of this"""
LAYOUT="""
            [ 00 ]
[ 01 ][ 02 ][ 03 ][ 04 ]
[ 05 ][ 06 ][ 07 ][ 08 ]
[ 09 ][ 10 ][ 11 ][ 12 ]
[ 13 ][ 14 ][ 15 ][ 16 ]
                  [ 17 ]
"""

"""This function's purpose is to allow for custom speed updating text.  DONE"""
def talk(text, spd=0, auto=False):#Parameters are string and speed we want it to update at.
                                #Auto checks if we want the text to immediately continue or if we want to prompt the user.
    for i in text: #For each character in the string
        sleep(spd) #call sleep to pause
        print(i, end="", flush = True) #Print the text, with no separation.  Set flush to true to unbuffer or it'll all display at the same time.
    if auto: #If talk will continue regardless of input
        print(flush = True) #print new line when we're finished.
    else: #Otherwise prompt the user to hit enter.  Check to make sure the text has completed being displayed first however.
        op=input("").upper()
        if op: #If the player actually provided true input.
            options(op) #Pass off input to the options command.
                    #Normally we'll just hit enter to continue scrolling through text.  But we might type in developer tools or even things like SAVE for the player


"""During talk functions, the player can chose to input information.  This could allow for certain tools and options"""
def options(sel):
    if "SAVE" in sel: 
        save()


"""Quick-Time Event Function.  This allows us to give the player a set of choices
Returns a value of a selected choice or expired timer.  DONE"""
def qte(choices, clock): #Parameters are a list of choices and a time for our timer
    global HURRY#Allow editing of HURRY variable.  When this hits 0, the player is out of time.

    talk(f"""
 What will you do?!
--------------------""", .08, True) #Let the user know they're about to have to make a choice
    talk(f""" {choices}
--------------------""", .01, True) #Give the player their list of options.  Also automatically continue forward past the message.

    HURRY=3 #This value will countdown once the timer starts.  Later as it decreases, the player will be warned of the time left.
    t = Timer(clock/3, qteresult, args=[clock]) #Create the imported timer object.
                                                ##Pass it with a third of the time allotted.  This says we want it to call a function when it expires.
                                                ##We use a third because we want to restart it 3 times and give a warning before the player's options expire.
                                                ###qteresult is the function we want the timer to call when time elapses
                                                ####args are the arguments we pass to our qteresult function.  In this case, we want it to know the total time we're asking for
    t.start() #Starts the timer.

    choice = "" #Create an empty string variable called choice.
    while not choice and HURRY: #While choice is not empty and there is still time
        choice=input("> ").upper() #Have the user input a choice and caps it
        for c in choices: #Loop through list of available choices
            if c.upper() in choice: #Check if the string entered contains your word.  We're also going to capitalize the choice list just in case we made a mistake.
                choice=c #Set choice to the proper word from the list

        if choice not in choices: #If they succeeded previously, their choice should be in the list.  If not, they entered something improper.
            choice="" #Since they made a bad choice, we're setting this to null to keep the loop going.

    if HURRY and choice: # If Hurry has not counted to 0 and we succeeded in making a proper choice
        print(f"\nYou chose: {choice}\n")#Display choice to player

    else: #If they ran out of time
        choice = "EXPIRED" #Set choice to a value of expired.

    HURRY=5 #Reset to default value.  This also helps ensure the qteresult function will stop if it's still running.
    t.cancel() #Halt the timer.
    sleep(1)
    return choice #Return results


"""This goes hand in hand with the qte function.  This is what the timer calls whenever it expires.  DONE"""
def qteresult(clock):
    global HURRY #Allow editing of HURRY variable.  When this hits 0, the player is out of time.
    if HURRY == 5: #If hurry equals the default value, we're going to stop this function by returning nothing and ensuring the timer stops
        return

    elif HURRY in range (1,5): #If HURRY is between 1 and 4, we'll begin the countdown process
        print("",end="")#Output a new line.
        for num in range(1,HURRY+1): #Get a set of numbers from 1 to where the HURRY timer currently is.
            print("Hurry! ", end="") #Output "Hurry!" to the player multiple times depending on how high the variable is.  No new line so they they're back to back.
        print("\n> ", end="") #Create a new line with input arrow to main readability

        HURRY-=1 #Decrease our HURRY time variable.
        t = Timer(clock/3, qteresult, args=[clock]) #Restart a new timer, once again to go off in a third of the total time.
                                                    ##Rerun this function when time runs out.
                                                    ###argument is once again the total time allotted
        t.start() #Start timer

    else: # If HURRY has decreased to 0 and this function is called=
       print("There's no more time for a decision...")#Let the player know time expired
       return



"""Story Function.  This will ultimately be what guides the player through the story."""
def story():
    #SMALL GUIDANCE ON HOW TO BEGIN
    talk('"...Greetings... please [ENTER] to continue ...."',.12)
    talk('"...So be it....welcome to this abode..."', .1)
    talk("*Thunder crashes*",.01)
    #INTRODUCTION TO PLAYER
    talk("*You grip your side.  You're awake now.  It's dark.  It's wet.  You're in pain but you seem to be okay*")
    talk("*...for now...*",.07)
    talk('"..."',.2)
    talk('"I\'m scared..."',.1)
    talk('"This hurts...what was that thing?"', .07)
    talk('"I dont want to die!"',.04)
    talk('"I gotta find my way out of this place.  I can\'t remember much but...maybe I can look around.."',.06)
    #ENCOUNTER
    talk("*pit..pat..pit..pat..pit..pat*", .15)
    talk('"Those sound like foot-steps, what should I do?...."')
    result = qte(["SHOUT","HIDE"], 10)
    if result=="SHOUT":
        talk('"HELP!  PLEASE HELP ME!!!!!!"',.05)
        talk("...", .5)
        talk("*pit..pat..pit..pat..pit..pat..pat..pit..pat..pit..pat*",0.01)
        talk('"Help I\'m -"', .1)
        talk("*Before you can finish your words, what emerges from the darkness before you terrifies you for the few moments you\'ve let to view it*", .03)
        talk("*Farewell*",.1)
        return
    talk("*There's too much you don't know.  You conceal yourself and let the footsteps fade away.*", .05)



"""This will potentially be the save function"""
def save():
    print("\n-GAME SAVED!\n")

"""Main function.  This will be the starting and guiding function for everything else."""
def main():
    story()


if __name__== "__main__": #If file is the one being ran
    main() #Execute main function

