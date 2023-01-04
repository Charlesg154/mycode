#!/usr/bin/env python3

marvelchars= {
"Starlord":
  {"real name": "peter quill",
  "powers": "dance moves",
  "archenemy": "Thanos"},

"Mystique":
  {"real name": "raven darkholme",
  "powers": "shape shifter",
  "archenemy": "Professor X"},

"Hulk":
  {"real name": "bruce banner",
  "powers": "super strength",
  "archenemy": "adrenaline"}
             }

def main():
    name=input(f"Please enter the character's name. Choose between {marvelchars.keys()}\n>")
    name=name.title()
    print(f"You chose {name}")
    stat=input(f"\nPlease enter a statistic between {marvelchars['Starlord'].keys()}\n>")
    stat=stat.lower()
    print(f"You chose {stat}")
    print(f"\n{name}'s {stat} is: {marvelchars[name][stat].title()}")
    repeat=input("\nWould you like to play again?  y/n\n>")
    repeat=repeat.lower()
    if repeat == "y":
        main()
    else:
        print("Goodbye")



main()
