#!/usr/bin/env python3
"""
An input asking the user's name.
An input asking what day of the week it is.
A print statement that reads:
Hello, <name>! Happy <day of the week>!
"""
def main():

    name = input("\nPardon me, but what is your name?  ")

    print("\nI see. ", name, end="") 

    day = input(", might you tell me what today is?  ")

    print("\nHello,", name + "!  Happy", day + "!\n")

main()
