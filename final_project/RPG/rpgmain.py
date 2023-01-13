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
import random #We're going to need this for the enemy to be able to randomly walk around.



"""GLOBAL VARIABLES"""
HURRY=5 #We will use this variable for our quick time events.  It's read by multiple fuunctions simultaneously so we need it to be global
LOC="04" #We will use this variable to annotate our current location
MLOC="03" #Gonna make this the monster location
VERBS = []
INVENTORY = []



"""The Layout of the Map.  The player will later have view of this"""
LAYOUT="""
              [ 00 ]
                |
[ 01 ]-[ 02 ]-[ 03 ]
   |     |
[ 04 ]-[ 05 ] [ 06 ]
   |            |
[ 07 ]-[ 08 ]-[ 09 ]
   |            |
[ 10 ]-[ 11 ]-[ 12 ]-[ 13 ]
                       |
                     [ 14 ]
"""



"""Each room and how they interconnect as a dictionary"""
ROOMS = {
        "00": {
            "South" : "03",
            "Item"  : ["Exit Key"]},
        "01" : {
            "South" : "04",
            "East" : "02",
            "Item"  : []},
        "02": {
            "South" : "05",
            "East" : "03",
            "West" : "01",
            "Item"  : []},
        "03": {
            "North" : "00",
            "West" : "02",
            "Item"  : []},
        "04": {
            "North" : "01",
            "South" : "07",
            "East" : "05",
            "Item"  : ["Lantern"]},
        "05": {
            "North" : "02",
            "West" : "04",
            "Item"  : []},
        "06": {
            "South" : "09",
            "Item"  : ["Exit Key"]},
        "07": {
            "North" : "04",
            "South" : "10",
            "East" : "08",
            "Item"  : []},
        "08": {
            "East" : "09",
            "West" : "07",
            "Item"  : []},
        "09": {
            "North" : "06",
            "South" : "12",
            "West" : "08",
            "Item"  : []},
        "10": {
            "North" : "07",
            "East" : "11",
            "Item"  : []},
        "11": {
            "East" : "12",
            "West" : "10",
            "Item"  : []},
        "12": {
            "North" : "09",
            "East" : "13",
            "West" : "12",
            "Item"  : []},
        "13": {
            "South" : "14",
            "West" : "12",
            "Item"  : []},
        "14": {
            "North" : "13",
            "Item" : ["Exit Location"]}
        }



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
    global LAYOUT
    if "SAVE" in sel: 
        save()
    if sel == "MAP":
        print(LAYOUT)#Testing this look



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



"""Give user a list of actions and show their and threat's location"""
def showStatus():
    global LOC, VERBS, INVENTORY#Declare global variables so we can edit these

    print('\n---------------------------')
    print("   What's my next move?")##We're going to output a neat banner here for the player to show a new phase
    print('---------------------------')
    #Now we're going to output the current map status to the player
    floor=LAYOUT.replace(LOC, "PL") #Replace the name of the room user is in with text "PL" to indicate where they are on map
    print(floor.replace(MLOC, "MO")) #Print map to user but also add the monster's location "MO"
    print("---------------------------")

    #This is currently our game ending scenario.
    if LOC=="14" and "Exit Key" in INVENTORY and "Exit Location" in INVENTORY:#If  the user has the key to the exit, found the exit, and in the door's location.
        ending()#Trigger ending
        return#Don't go any further in this function

    monstermove()#This function will move the monster's location and also check for an encounter

    undiscovered=[]#We'll use this list to check for any items we haven't found yet
    for i in ROOMS[LOC]["Item"]:#Check the item key in this location to see if it has an associated item
        if i not in INVENTORY:#Check if we have that item in our inventory yet
            undiscovered.append(i)#If we do not, we're going to add it to the list of undiscovered items

    if undiscovered and random.randrange(0,10) < 7: #If there's an item in our undiscovered list and we randomly get a number less than 7 out of 10
        talk('"...maybe there\'s something here."',.05) #Give the user a hint to search the area

    action=""
    while not action:
        action=input(f"Choose an action: {VERBS}\n>").upper()

        #We're going to make some special checks for if the user does some shortcut commands to move around
        direction = "" #We'll need this variable for later in the MOVE command
        cardinal = ["NORTH", "SOUTH", "EAST", "WEST"] #list of directions
        if " " in action: #Check action has a space
            direction = action.split(" ", 1)#Split if it does.  Set direction to equal this value
            for d in direction: #Check the new list
                if d in cardinal: #If either of the words match a directional value
                    action = d #Set the action variable to specifically equal this value
        
        if action in cardinal: #If the user entered a cardinal value, or if the above if statement turned the action into this value
            direction = action.title() #Set the direction value equal to action.  This will allow us to keep track later where the user wanted to move.
            action = "MOVE" #Now set action to move.  This will allow it to pass when we check if the action is in our approved VERBS list.

        if action.title() not in VERBS: #We have our verbs in a title format.  Convert our action to that and see if it's in the list.
            action = "" # If it's not in the list, reset action to null and restart the loop
            print("Please select a different option") # Alert the user to make a new choice.

        elif action == "MOVE":
            move(direction)

        elif action == "SEARCH":
            search(undiscovered)
            return

        else:
            action=""
            print("Please select a different option")



"""We'll define the MOVE action here.  This is an option in the showStatus function"""
def move(direction):
    global LOC
    where=[] # Going to make a temporary list that we'll keep track of available directions
    for t in ROOMS[LOC]: #Check value of key in the ROOMS dict that matches user's location
        if t in ["North", "South","East","West"]:#Check if T is a cardinal direction
            where.append(t)#Add T as a possible path by appending our temporary list
    if direction in where: #If user entered a direction previously as a shortcut and it matches available paths
        dest=direction #Set the destination to that path
    else:#If the user hasn't already chosen a path or picked an incorrect one earlier
        dest=input(f"Move where? {where}\n>").title() #Give input to allow them to chose from a list of possible paths
    if dest in where: #Check the input and see if it matches our list of possibilities
        LOC=ROOMS[LOC][dest]#Update user's location.  LOC should match Rooms key and dest should match value-key associated.
        showStatus()#Restart the status with new location
    else:
        action=""#If user didn't provide a proper destination
        print("Please select a different option")#Alert them and restart while loop



"""We'll define the SEARCH action here.  This is an option in the showStatus function"""
def search(undiscovered):
    global INVENTORY
    talk('*Ruffling* "There\'s gotta be something here that can help me..."', .05)
    if undiscovered:
        item = random.choice(undiscovered)
        talk('"This is ... "',.05)
        talk(f'("I found this {item}!")',.01)
        INVENTORY.append(item)

        if item == "Lantern":
            talk('"I can see my way around with this..."',.05)
            VERBS.append("Move")#ALLOW USER TO MOVE

        showStatus()

    else:
        talk('"Darn it....there\'s nothing..."', .05)
        showStatus()



"""Story Function.  This will ultimately be what guides the player through the story."""
def story():
    global VERBS
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
    result = qte(["SHOUT","HIDE"], 8)
    if result=="SHOUT":
        talk('"HELP!  PLEASE HELP ME!!!!!!"',.05)
        talk("...", .5)
        talk("*pit..pat..pit..pat..pit..pat..pat..pit..pat..pit..pat*",0.01)
        talk('"Help I\'m -"', .1)
        talk("*Before you can finish your words, what emerges from the darkness before you terrifies you for the few moments you\'ve let to view it*", .03)
        talk("*Farewell*",.1)
        return
    talk("*There's too much you don't know.  You conceal yourself and let the footsteps fade away.*", .05)
    talk('"I\'ll look around and see what I can find out."',.08)
    #USER FREE TO EXPLORE
    VERBS.append("Search")#SET UP USER'S INITIAL POTENTIAL ACTIONS
    showStatus()#SEND THEM TO STATUS TO BE ABLE TO MAKE A MOVE



"""This will determine what will happen when the user runs into the monster"""
def monstermove():
    global LOC, MLOC
    if LOC == MLOC:
        print("AHHHHH!  REAL MONSTER!")



"""Default story ending for now"""
def ending():
    talk("You make it out of that wretched place",.05)
    talk("You look forward to the day this can all be seen as some weird twisted dream you've awoken from",.05)
    print("YOU LIVED")



"""This will potentially be the save function"""
def save():
    print("\n-GAME SAVED!\n")



"""Main function.  This will be the starting and guiding function for everything else."""
def main():
    story()



if __name__== "__main__": #If file is the one being ran
    main() #Execute main function

