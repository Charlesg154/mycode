#!/usr/bin/env python3

while True:
    try:
        print("Let's divide x by y!")
        x = int(input("What is the integer value of x? "))
        y = int(input("What is the integer value of y? "))
        print("The value of x/y: ", x/y)
    except ZeroDivisionError as zerr:
        print("Handling run-time error:", zerr)
    
    except ValueError as err:
            print("That was not a legal value for division:", err)
    except Exception as err:
        print("We did not anticipate that:", err)
    else:
        print("\nThanks for learning to handle errors!")
        break
