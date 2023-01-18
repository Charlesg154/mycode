#!/usr/bin/env python3

"""
The purpose of the project is to present various functions incorporating newly learned python skills
    in the presentation of an RPG.
Functions will be made in a way that allows the game to be feasibly expanded without extensive effort.
User will have multiple actions to chose from that can be added or removed from a list.
User can be presented with quick-time-event style choices, where they must choose from a custom-list of options against a custom-set timer.
    They will be presented with timer warnings and have the option to fail.
User will have a map presented to them that will update based on changed location
User will be able to collect items that are available in traveled rooms
User will be able to save and load data.

TO DO:
INVENTORY DESCRIPTIONS-
STREAMLINE LOADING BY CHECKING IF VARIABLE NAME MATCHES LINE NAME, STRIPPING THAT FROM THE LINE AND LEAVING ONLY THE VALUE

-CHARLES GREEN JR. | TLG NDE COHORT
"""



from time import sleep #Sleep function required for various delays
from threading import Timer #Timer object required for quick-time events
import random #We're going to need this for an enemy to be able to randomly walk around and other gaming aspects



"""GLOBAL VARIABLES"""
HURRY=5 #We will use this variable for our quick time events.  It's read by multiple fuunctions simultaneously so we need it to be global
LOC="04" #We will use this variable to annotate our current location
MLOC="03" #Gonna make this the monster location
VERBS = [] #This will be a list of available options to the user each turn
INVENTORY = [] #This will be the items the user has on hand
#ASCII ART BELOW FOR GAME ENDERS
YOUDIED="""
 @@@ @@@  @@@@@@  @@@  @@@      @@@@@@@  @@@ @@@@@@@@ @@@@@@@ 
 @@! !@@ @@!  @@@ @@!  @@@      @@!  @@@ @@! @@!      @@!  @@@
  !@!@!  @!@  !@! @!@  !@!      @!@  !@! !!@ @!!!:!   @!@  !@!
   !!:   !!:  !!! !!:  !!!      !!:  !!! !!: !!:      !!:  !!!
   .:     : :. :   :.:: :       :: :  :  :   : :: ::: :: :  : 
"""

YOULIVED="""
 @@@@@@@@  @@@@@@  @@@@@@@  @@@@@@  @@@@@@@  @@@@@@@@ @@@@@@@ 
 @@!      !@@     !@@      @@!  @@@ @@!  @@@ @@!      @@!  @@@
 @!!!:!    !@@!!  !@!      @!@!@!@! @!@@!@!  @!!!:!   @!@  !@!
 !!:          !:! :!!      !!:  !!! !!:      !!:      !!:  !!!
 : :: ::: ::.: :   :: :: :  :   : :  :       : :: ::: :: :  :
"""

"""The Layout of the Map.  The player will later have view of this.  Customize to match the ROOMS variable."""
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


"""Each room and how they interconnect as a dictionary.  Customize to match the LAYOUT variable.  Include items here as well."""
ROOMS = {
        "00": {                         # ROOM NUMBER
            "South" : "03",             # DIRECTIONS AVAILABLE BASED ON LAYOUT : ASSOCIATED ROOM IN THAT DIRECTION
            "Item"  : ["Exit Key"]},    # ITEM: LIST OF ITEMS INSIDE OF THIS PARTICULAR LOCATION
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
        "05": {                         # ROOM NUMBER
            "North" : "02",             # DIRECTIONS AVAILABLE BASED ON LAYOUT : ASSOCIATED ROOM IN THAT DIRECTION
            "West" : "04",
            "Item"  : []},              # ITEM: LIST OF ITEMS INSIDE OF THIS PARTICULAR LOCATION
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
        "10": {                         # ROOM NUMBER
            "North" : "07",             # DIRECTIONS AVAILABLE BASED ON LAYOUT : ASSOCIATED ROOM IN THAT DIRECTION
            "East" : "11",
            "Item"  : []},              # ITEM: LIST OF ITEMS INSIDE OF THIS PARTICULAR LOCATION
        "11": {
            "East" : "12",
            "West" : "10",
            "Item"  : []},
        "12": {
            "North" : "09",
            "East" : "13",
            "West" : "11",
            "Item"  : []},
        "13": {
            "South" : "14",
            "West" : "12",
            "Item"  : []},
        "14": {
            "North" : "13",
            "Item" : ["Exit Location"]}
        }


"""LIST OF POTENTIAL ITEMS IN THE WORLD.  DEFINE THEM HERE.  PLACE THEIR LOCATIONS IN THE ROOMS VARIABLE ABOVE."""
ITEM_LIST = {
        "Lantern" : "I can MOVE around as long as I have this with me...",  #ITEM NAME (MATCHING WHAT'S AVAILABLE IN ROOMS) : ITEM DESCRIPTION
        "Exit Key" : "As long as I find the EXIT LOCATION, this should be able to get me out...",
        "Exit Location" : "I found where to leave....with an EXIT KEY I should be able to escape here..."
        }



"""This function's purpose is to allow for custom speed updating text.  DONE"""
def talk(text, spd=0, auto=False):#Parameters are text-string and speed we want it to update at.
                                #Auto parameter checks if we want the text to immediately continue or if we want to prompt the user instead.
    for i in text: #For each character in the string
        sleep(spd) #call sleep to pause
        print(i, end="", flush = True) #Print the text, character by character, with no separation.  Set flush to true to unbuffer or it'll all display at the same time.

    if auto: #If talk will continue regardless of input
        print(flush = True) #print new line when we're finished.

    else: #Otherwise prompt the user to hit enter.
        op=input("").upper()
        if op: #If the player actually provided some kind of text input instead
            options(op) #Pass off input to the options command.  This will read if we type in any special 'commands' for developer tools or extra player options



"""During talk functions, the player can chose to input information.  This could allow for certain tools and options"""
def options(sel):#Parameter will be text value
    #Check to see if the text value equals a keyword for special commands
    if sel == "MAP":
        global LAYOUT
        print(LAYOUT) #Print the map if you type in MAP.

    elif sel == "DEBUG": #Print global variables when we type debug
        print(f"LOC: {LOC}\nMLOC: {MLOC}\nVERBS: {VERBS}\nINVENTORY: {INVENTORY}")

    elif sel in ["QUIT", "EXIT", "LEAVE"]:#If the user types anything relating to leaving
        print('"Farewell...until next time."')#Let the user know the exited successfully
        exit()#Exit the script



"""Quick-Time Event Function.  This allows us to give the player a set of choices.
Function returns a value of a selected choice or expired timer.  DONE"""
def qte(choices, clock): #Parameters are a list of choices and a time for our timer
    global HURRY#Allow editing of HURRY variable.  When this hits 0, the player is out of time.

    talk(f"\n What will you do?!", .08, True) #Let the user know they're about to have to make a choice
    talk(f"--------------------\n {choices}\n--------------------", .01, True) #Give the player their list of options.  Also automatically continue once text is displayed.

    HURRY=3 #This value will countdown once the timer starts.  Later as it decreases, the player will be warned of the time left.
    t = Timer(clock/3, qteresult, args=[clock]) #Create the imported timer object.
                                                ##Pass it with a third of the time requested.  This says we want it to call a function when it expires.
                                                ##We use a third because we want to restart it 3 times and give a warning before the player's options expire.
                                                ###qteresult is the function we want the timer to call when time elapses
                                                ####args are the arguments we pass to our qteresult function.  In this case, we want it to know the total time we're asking for
    t.start() #Starts the timer.

    choice = "" #Create an empty string variable called choice.
    while not choice and HURRY: #While choice is not empty and there is still time
        choice=input("> ").upper() #Have the user input a choice and uppercase it
        for c in choices: #Loop through list of available choices
            if c.upper() in choice: #Check if the string entered contains your word.  We're also going to capitalize the choice list to match our capitalied input
                choice=c #Set choice to the proper word from the list

        if choice not in choices: #If they succeeded previously, their choice should be in the list.  If not, they entered something improper.
            choice="" #Since they made a bad choice, we're setting this to null to keep the loop going.

    if HURRY and choice: # If Hurry has not reduced to 0 and we our input was in the choice list
        print(f"\nYou chose: {choice}\n")#Display successful choice to player

    else: #If they ran out of time
        choice = "EXPIRED" #Set choice to a value of expired.

    HURRY=5 #Reset to default value.  This also helps ensure the qteresult function will stop if it's still running.
    t.cancel() #Halt the timer.
    sleep(1)
    return choice #Return results



"""This goes hand in hand with the qte function.  This is what the timer calls whenever it expires.
Will repeat itself until all warnings expire.  DONE"""
def qteresult(clock): #Pass the total time for the qte as a parameter
    global HURRY #Allow editing of HURRY variable.  When this hits 0, the player is out of time.
    if HURRY == 5: #If hurry equals the default value, we're going to stop this function by returning nothing and ensuring the timer doesn't repeat
        return

    elif HURRY in range (1,5): #If HURRY is between 1 and 4, we'll begin the countdown process
        print("",end="")#Output a new line.
        for num in range(1,HURRY+1): #Get a set of numbers from 1 to where the HURRY timer currently is.
            print("Hurry! ", end="") #Output "Hurry!" to the player multiple times depending on how high the variable is.  Remove \n so text warning is back to back.
        print("\n> ", end="") #Create a new line with input arrow to maintain readability

        HURRY-=1 #Decrease our HURRY time variable.
        t = Timer(clock/3, qteresult, args=[clock]) #Start a new timer, once again to go off in a third of the total time requested.
                                                    ##Rerun this function, qteresult, when time runs out.
                                                    ###argument for qteresult is once again the total time allotted
        t.start() #Start timer

    else: # If HURRY has decreased to 0 and this function is called
       print("There's no more time for a decision...") #Let the player know time expired
       return #return nothing to end the function



"""Give user a list of actions and show theirs and threat's location"""
def showStatus(restart=False): #Restart parameter is for when this function is being restarted and we don't want certain things to happen
    global LOC, VERBS, INVENTORY#Declare global variables so we can edit these

    #This is currently our game ending scenario.
    if LOC=="14" and "Exit Key" in INVENTORY and "Exit Location" in INVENTORY:#If  the user has the key to the exit, found the exit, and in the door's location.
        ending()#Trigger ending
        return #Don't go any further in this function

    if not restart: #If this function wasn't called as a restart
        monstermove()#This function will move the monster's location and also check for an encounter

    print('\n---------------------------')
    print("   What's my next move?")##We're going to output a neat banner here for the player to show a new phase
    print('---------------------------')
    #Now we're going to output the current map status to the player
    floor=LAYOUT.replace(LOC, "PL") #Replace the name of the room user is in with text "PL" to indicate where they are on map
    print(floor.replace(MLOC, "MO")) #Print map to user but also add the monster's location "MO"
    print("---------------------------")

    undiscovered=[]#We'll use this list to check for any items we haven't found yet
    for i in ROOMS[LOC]["Item"]:#Check the item key in this location to see if it has an associated item
        if i not in INVENTORY:#Check if we have that item in our inventory yet
            undiscovered.append(i)#If we do not, we're going to add it to the list of undiscovered items

    if undiscovered and random.randrange(0,10) < 7 and not restart: #If there's an item in our undiscovered list and we randomly get a number less than 7 out of 10
                                                                    #And if this function isn't being restarted due to saving, loading, etc.
        talk('"...maybe there\'s something here."',.05) #Give the user a hint to search the area

    action="" #Creating a string variable called action.  This will keep track of what the player wants to do.

    while not action:#While action variable is empty (User hasn't chosen to do something properly yet)
        action=input(f"Choose an action: {VERBS}\n>").upper()#Prompt user for input.  Show them the list of available actions from Global variables VERBS

        #We're going to make some special checks for if the user does some shortcut commands to move around or check items
        shortcut = "" #We'll need this variable for later in the MOVE and INVENTORY functions
        cardinal = ["NORTH", "SOUTH", "EAST", "WEST"] #list of directions
        if " " in action: #Check action has a space so we know there's two words
            shortcut = action.split(" ", 1)#Split if it does.  Set shortcut to equal this list
            for d in shortcut: #Check the new list
                if d in cardinal: #If either of the words match a directional value
                    action = d #Set the action variable to specifically equal this value
                if d.title() in INVENTORY:#If either of the words match an item in your inventory
                    action = d.title() #Set the action variable specifically to this
    
        options(action)#This is just for some debug options.  Won't advance anything but will check for keywords to give specific outputs
                        #I'll also use this to check for input indicating user wants to quit.  That way they can do it mid-story or on the status screen

        if action in cardinal: #If the user entered a cardinal value, or if the above if statement turned the action variable into this value [North, South, East West]
            shortcut = action.title() #Set the shortcut value equal to action (which should be North, South, East, or West).  This will allow us to keep track later where the user wanted to move.
            action = "MOVE" #Now set action to move.  This will allow it to pass when we check if the action is in our approved VERBS list.

        if action.title() in INVENTORY: #If the user typed the name of an item in the inventory value, or our above if statement forced the action variable to be the name of one
            shortcut = action.title()#Set the shortcut value equal to the action (which is the name of an item)
            action = "INVENTORY"#Set our action value to inventory.  This will allow it to pass when we check if the action is in our approved VERBS list

        if action.title() not in VERBS: #We have our verbs in a title format.  Convert our action to that and see if it's in the list.
            action = "" # If it's not in the list, reset action to null and restart the loop
            print("Please select a different option") # Alert the user to make a new choice.

        elif action == "MOVE":#If the user chose to move
            move(shortcut, False)#Call the move function.  Pass the direction shortcut if you have it.
                                #Second value of monster is false since this is the player calling move.

        elif action == "INVENTORY":#If the user chose the inventory option
            inventory_check(shortcut)#Call the inventory_check function.  Pass the item shortcut if we have it.

        elif action == "SEARCH":#If the user chose to search
            search(undiscovered) #Call the search function.  Pass on the undiscovered items in the area.

        elif action == "SAVE":#If the user chose to save the game
            save()#Run the save function
            showStatus(True)#Rerun showstatus.  Show that we're restarting the loop by setting restart to True

        elif action == "LOAD":#If the user chose to save the game
            load()#Run the save function
            showStatus(True)#Rerun showstatus.  Show that we're restarting the loop by setting restart to True

        else:#If the user did not type in a valid action
            action=""#Reset action to null to continue the loop
            print("Please select a different option")#Prompt the user to try again



"""This will determine what will happen when the user runs into the monster"""
def monstermove(whoops=False): #Function that controls monster.  Whoops is true when user runs into the monster instead of vice versa
    global LOC, MLOC #Make monster location and user location editable

    if not whoops:#If this being run because the monster needs to move and not because the user walked into it's space
        move("", True) #Use the move function but call it for monster.

    if MLOC == LOC: #Check if new location matches the user's location
        talk("*pit..pat..pit..*", .15)
        talk("*pit..pat..pit..pat..pit..pat..pat..pit..pat..pit..pat*",0.01)#Prompt the user that a monster encounter has been triggered!
        talk(" Fear Faces You",.1)
        options=["RUN","BEG","STRUGGLE"]#List of [potential options you'll have to use against the monster]
                                        #In expanding this, you can even make checks to see if certain options are available to add based on things the player has done.
        while len(options) > 2: #Check if the list of options is greater than two
            options.remove(random.choice(options)) #While there is, remove a random option from the list
                                                   ##We don't need to do this, and can make as many choices as we want
                                                   #But it'll make the chances of escape vary based on what choices get offered to the player
        result=qte(options, 7)#Start a QTE Event.  Use the options above as the player's list of choices.  Set the timer to 7 seconds.
        #Results of player choice
        if result == "EXPIRED":                 #If time runs out
            talk('"Before I knew what happened"',.1)
            talk('"...It was all over..."',.1)
            death()                             #They lose
        elif result == "BEG":   #If they chose this option
            talk('"Please!!!"',.03)
            talk('"PLEASE I BEG YOU!  I -"', .03)
            talk("...",1)
            death()             #They lose
        elif result == "STRUGGLE":          #If they chose the "Struggle" option
            talk("*YOU SCRAPE SCREAM AND PUSH LOOKING FOR ANY ESCAPE FROM THE TERRIFYING BEING BEFORE YOU*",.02)
            talk('"No...no...no!!!!  NO!!!!"', .03)
            if random.randrange(0,10) < 5: #If they get less than a 5 between 0-10
                talk("...but escape was impossible...",.05)
                death()                     #They lose
            else:                           #If they roll a 5 or higher, however, they break free.
                talk("...You break free and hide from the unknown!",.05)
                talk("...pit...pat...pit...",.1)

        elif result == "RUN":              #If they chose the "Run" option
            talk("*As footsteps approach you immediately push to another direction*", .03)
            if random.randrange(0,10) < 3: #If they get less than a 3 between 0-10
                talk("...but escape was impossible...",.05)
                death() #They lose
            else:                           #But if they roll a 3 or higher they break free.
                talk("*You manage to break away and hide from the entity!*",.05)
                talk("...pit...pat...pit...",.1)



"""We'll define the MOVE action here.  This is an option in the showStatus function"""
def move(direction="", monster=False):
    global LOC, MLOC
    if monster: #If the monster is moving
        l=MLOC  #Set location value "l" to monster location
    else: #If user is moving
        l=LOC #Set location value "l" to user location

    where=[] # Going to make a temporary list that we'll keep track of available directions
    for t in ROOMS[l]: #Check value of key in the ROOMS dict that matches user's/monster's location
        if t in ["North", "South","East","West"]:#Check if T is a cardinal direction
            where.append(t)#Add T as a possible path by appending our temporary list "where"

    if direction in where: #If user entered a direction previously as a shortcut and it matches available paths
        dest=direction #Set the destination to that path

    else:#If the user hasn't already chosen a path or picked an incorrect one earlier
        if not monster:#If they're not the monster
            dest=input(f"Move where? {where}\n>").title() #Give user input to allow them to chose from a list of possible paths
        else:
            dest=random.choice(where) #Randomly chose a destination if your a monster

    if dest in where: #Check the input and see if it matches our list of possibilities
        if(monster):
            MLOC=ROOMS[MLOC][dest]#Update monster's location.  MLOC should match ROOMS dict key and dest should match value-key associated.
        else:
            LOC=ROOMS[LOC][dest]#Update user's location.  LOC should match ROOMS dict key and dest should match value-key associated.
            if LOC==MLOC:
                monstermove(True)#If the player walked into the monster....trigger an encounter
            showStatus()#Run ShowStatus function for new round

    else:#If user didn't provide a proper destination (our input didn't match one of the available options)
        print("\nNO GOOD!  TRY A DIFFERENT ROUTE!")#Alert them
        showStatus(True)#Restart the showStatus function without starting a new round



def inventory_check(item):
    choice=""
    if item and item in INVENTORY: #If item isn't null and is an item in our inventory
        choice=item #Set our choice to this item
    else: #If there isn't an item already chosen as a shortcut
        choice=input(f"Which item would you like to investigate? {INVENTORY}\n>").title()#Have the user choose what item they'd like to investigate

    if choice in INVENTORY:#One last check make sure the choice is valid
        talk(f"{choice}: {ITEM_LIST[choice]}",.03)#Output the choice as well as the associated description from the ITEM_LIST dictionary which should match names
    else:
        talk(f"{choice}... I don't think that's something I have on me.",.05)#Output failed choice

    showStatus(True)#Restart the showStatus function without starting a new round


"""We'll define the SEARCH action here.  This is an option in the showStatus function.  DONE"""
def search(undiscovered):#Pass with a parameter of undiscovered items in this location
    talk('*Ruffling* "There\'s gotta be something here that can help me..."', .05)#Show that the user is searching

    if undiscovered:#Check to see if there is anything in the area undiscovered by the value we've passed to the function's parameter
        global INVENTORY #Call global variable "INVENTORY" so we can edit it
        item = random.choice(undiscovered)#In case there's multiple items here, pick one at random.
        talk('"This is ... "',.05)
        talk(f'("I found this {item}!")',.01)#Show the user what item they've found.
        INVENTORY.append(item)#Add the item to the user's inventory

        #Check for special items that'll cause for some kind of change
        if item == "Lantern":
            talk('"I can see my way around with this..."',.05)
            VERBS.append("Move")#Add movement to the user's potential actions
            VERBS.sort()

        if len(INVENTORY) and "Inventory" not in VERBS:#Check if the inventory is greater than zero and if the player is able to use the Check Inventory action.
            VERBS.append("Inventory")#Add the Inventory option since they an item now.

        showStatus()#End turn and return user to status menu

    else:#If there is no item here that has yet to be discovered
        talk('"Darn it....there\'s nothing..."', .05)#Prompt the user of failure
        showStatus()#End turn and return user to status menu



"""Story Function.  This will ultimately be what guides the player through the story."""
def story():
    global VERBS#We'll add some actions the user can do at the end of this section, so we need to make sure it's editable.
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
    result = qte(["SHOUT","HIDE"], 8) # Trigger a QTE.  The choice or expiration will be saved to this "result" variable.
    if result=="SHOUT":#If the result from the encounter is that you decide to shout
        talk('"HELP!  PLEASE HELP ME!!!!!!"',.05)
        talk("...", .5)
        talk("*pit..pat..pit..pat..pit..pat..pat..pit..pat..pit..pat*",0.01)
        talk('"Help I\'m -"', .1)
        talk("*Before you can finish your words, what emerges from the darkness before you terrifies you for the few moments you\'ve let to view it*", .03)
        talk("*Farewell*",.1)
        death()#Run death function and end game
        return
    #If the result is that time expires or you actively chose the "Hide" option, continue through the story.
    talk("*There's too much you don't know.  You conceal yourself and let the footsteps fade away.*", .05)
    talk('"I\'ll look around and see what I can find out."',.08)
    #USER FREE TO EXPLORE.  SET UP THEIR INITIAL ACTIONS
    VERBS.append("Search")
    VERBS.append("Save")
    VERBS.append("Quit")
    showStatus() # SEND THEM TO STATUS SCREEN TO BE ABLE TO MAKE A MOVE FOR FIRST ROUND.



"""Function for when the user dies."""
def death():
    talk(YOUDIED, .02)#Display ASCII art
    exit()#Exit the script



"""Story ending for now"""
def ending():
    talk("*You have the key.  The door is in sight.  What seemed impossible is now before you.*",.08)
    talk("*You can feel the tears fall down your face in relief.*",.05)
    talk("*pit..pat..pit..pat..pit..pat*", .15)
    talk('"No..no no!  I need to leave now!"',.03)
    talk("*You rapidly approach the door, desperately fumbling with the key*",.05)
    talk("*pit..pat..pit..pat..piT..PAT..PIT..PAT..PIT..PAT..PIT*",0.01)
    talk("*C L I N K*",.15)
    talk("*The key falls*",.05)
    talk("What's your priority?",.05)
    result=qte(["Hide", "Key"], 8) # Start a QTE and save results to a variable called result
    if result in ["Expired","Key"]: # If result is that time expired or they chose to get the key
        talk("*You desperately attempt to grab the key!  Freedom lies right th-*",.05)
        talk('"It\'s not fair..."',.1)
        death() # They Lose
    #If user chose to "Hide" continue on
    talk("*You hide...and hope...and for what seems like an eternity...*",.05)
    talk("...pit...pat...pit...",.1)
    talk("*It leaves...*",.05)
    talk("*You don't know why and you don't ask questions.  You grab the key and bolt for the door!*",.05)
    talk("*You make it out of that wretched place!  Your mind not thinking of anything as you continue to run.*",.05)
    talk("*You look forward to the day this can all be seen as some weird twisted dream you've awoken from...*",.05)
    talk(YOULIVED, .02)#Display ASCII art saying they win
    exit()#Exit the script



"""This will check for save data when starting the game"""
def savecheck():
    try:
        with open("savefile.txt", "r") as save:#Try to open savefile data if it exists

            line = save.readline().rstrip('\n')#Read the first line and strip the new line character
            if "RPGSAVEFILE" not in line: #Check to see if first line of save file is what we expect
                return "NEW"#If it isn't, return NEW for new game

            else:#If we find save data file, and the first line is what we expect
                print("--------------------\n SAVE FILE DETECTED\n--------------------")#State that we've detected a valid save file
                inp=input("Would you like to load this save data?  y/n\n>").upper()#Ask user if they'd like to load data

                if inp in ["Y","YES","LOAD", "L"]:#If they answer yes
                    return "LOAD"#Return LOAD to load data

                else: #If they answer anything other than yes to loading their save data...
                    VERBS.append("Load")#Since they have available save data, go ahead and give them the load action for later to recall it when they'd like
                    return "NEW"#Return the value of NEW to start a new game

    except: #If the save data can't be found
        return "NEW" #Return "NEW" for new game



"""THIS WILL WRITE SAVE DATA TO A NEW FILE"""
def save():
    global LOC, MLOC, VERBS, INVENTORY #Call all the global variables we intend to save

    with open("savefile.txt", "w") as save:#Open save file as a writable file
        save.write(f"RPGSAVEFILE\n{LOC}\n{MLOC}\n{VERBS}\n{INVENTORY}")#Write save data values to their own individual lines

    talk("\n(-GAME SAVED!-)\n",.05)#Prompt the user that the game has been saved

    if "Load" not in VERBS: #After saving, check to see if they have the LOAD action yet
        VERBS.append("Load")#If they don't, add it to their available actions, as they now have saved data that can be loaded.



"""THIS WILL LOAD SAVED DATA FROM A PREVIOUSLY WRITTEN FILE"""
def load():
    try:
        with open("savefile.txt", "r") as save:#Try and open save file data if it exists

            global LOC, MLOC, VERBS, INVENTORY #We'll be changing all our global variables.
            x=0 #Going to create this variable to count up and indicate what line we're on

            for line in save:#For each line in this save file
                line=line.rstrip("\n")#Strip new line character from each line

                if x == 0 and "RPGSAVEFILE" not in line: #If the first line is NOT what we expect
                    break   #Break from the loop.  This isn't a compatible file.

                if x==1:        #If this is the second line
                    LOC=line    #This should be our LOC variable, so set it equal to the line.

                if x == 2:      #If this is the third line
                    MLOC=line   #This should our MLOC variable, so set it equal to the line

                if x == 3:      #If this is the fourth line
                    VERBS = []  #Start by emptying our VERBS list so we can repopulate it

                    line=line.rstrip("]'")#Strip the brackets and apostrophes from the edges
                    line=line.lstrip("['")#This is being read as a string, not a list, so we want all that list syntax off of it

                    if "', '" in line:  #Each element in the list will be seprated by a ', '| (IE, 'Talk', 'Move', ').  Here we're checking if there's multiple elements
                        VERBS = line.split("', '") #If there are multiple elements, split this string into a list.  Save that to our VERBS global variable.

                    elif line != "":        #If there aren't multiple elements but the line also isn't blank
                        VERBS.append(line)  #Then that should mean there's only one entry.  Let's append that to our currently empty list.

                if x == 4:          #If this is the fith line
                    INVENTORY=[]    #Start by emptying our INVENTORY list so we can repopulate it

                    line=line.rstrip("]'")#Strip the brackets and apostrophes from the edges
                    line=line.lstrip("['")#This is being read as a string, not a list, so we want all that list syntax off of it

                    if "', '" in line:#Each element in the list will be seprated by a ', '| (IE, 'Lantern', 'Dagger', ').  Here we're checking if there's multiple elements
                        INVENTORY = line.split("', '")#If there are multiple elements, split this string into a list.  Save that to our INVENTORY global variable.

                    elif line != "":            #If there aren't multiple elements but the line also isn't blank
                        INVENTORY.append(line)  #Then that should mean there's only one entry.  Let's append that to our currently empty list.
                x+=1 #Increase x to indicate the next line

        talk("\n(-GAME LOADED!-)\n",.05)    #Prompt the user that the game has been loaded
    except:
        talk('(No save data located.)',.05) #If they user is attempting this but no save data is found, prompt the user.



"""Main function.  This will be the starting and guiding function for everything else."""
def main():
    check=savecheck()   #Before we start the game, we'll check for save data and return a value to a temporary variable called "check"

    if check=="LOAD":       #If the save data check returns a value of load
        load()              #Load the game
        showStatus(True)    #Bring user to the status screen

    else:       #If the save data check returns anything other than LOAD
        story() #Run the story function.  We're starting a new game.



if __name__== "__main__":   #If this script is what's being run
    main()                  #Execute main function
