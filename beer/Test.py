#!/usr/bin/env python3

def main():
    while True:
        try:
            beer=int(input("How many bottles of beer on the wall are there?! (0-100)\n>"))
            if beer>100 or beer<0:
                print("I think you've had one too many.")
                again=input("Call it a night? y/n\n>").lower()
                if again != "n":
                    print("Let's get you home buddy...")
                    return
            else:
                break
        except Exception as err:
            print("I think you've had one too many.")
            again=input("Call it a night? y/n\n>").lower()
            if again != "n":
                print("Let's get you home buddy...")
                return
    print("Ohhhhhhhhhhhhh!")
    for num in range(beer,-1,-1):
        if num != 0:
            print(f"{num} bottles of beer on the wall!\n{num} bottles of beeer!  You take one down, pass it around!  {num-1} bottles of beer on the wall!")
        else:
            print("No more bottles of beer on the wall!\nNo more bottles of beer!  You go to the store and buy some more...")
            main()
"""
def mistake():
    print("I think you've had one too many.")
    again=input("Call it a night? y/n\n>").lower()
    if again != "n":
        print("Let's get you home buddy..")
"""

main()
