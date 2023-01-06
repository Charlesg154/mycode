#!/usr/bin/env python3
"""
Find Lines w/ Vampire in Dracula!
"""
def main():
    v=0
    with open('vampytimes.txt',"w") as vampy:
            vampy.write(" ")
    with open('dracula.txt',"r") as book:
        for line in book:
            if "vampire" in line.lower():
                print(line)
                v+=1
                with open('vampytimes.txt',"a") as vampy:
                    vampy.write(line)
    print(f"Vampire is written on {v} lines in Dracula!")
main()

