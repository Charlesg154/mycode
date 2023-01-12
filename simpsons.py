#!/usr/bin/env python3

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [
{"slappy": "a",
"text": "b",
"kumquat": "goggles",
"user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},
"banana": 15,
"d": "nothing"}
]



"My eyes! The goggles do nothing!"
#Eyes, googles, nothing
def main():
    #challenge
    eyes = challenge[2][1]
    goggles = challenge[2][0]
    nothing = challenge[3]
    print(f"My {eyes}!  The {goggles} do {nothing}!")

    #trial
    eyes = trial[2]["goggles"]
    goggles = trial[2]["eyes"]
    nothing = trial[3]
    print(f"My {eyes}!  The {goggles} do {nothing}!")

    #nightmare
    eyes = nightmare[0]["user"]["name"]["first"]
    goggles = nightmare[0]["kumquat"]
    nothing = nightmare[0]["d"]
    print(f"My {eyes}!  The {goggles} do {nothing}!")



if __name__=="__main__":
    main()


