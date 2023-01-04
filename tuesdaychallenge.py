#!/usr/bin/env python3
#Needed to update Shebang

number= 2

name= input("What is your name?\n>")#Needed quotes

# This is what you should see when print runs-
# Hi <name>! Welcome to Day 2 of Python Training!

print(f"Hi {name.capitalize()}! Welcome to Day {number} of Python Training!")
#Needed to add paren for the method used
#That was the last fix to get the code to run but you also need to call the variable 'number' properly.  Otherwise, it's a string.
