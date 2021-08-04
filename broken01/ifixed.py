#!/usr/bin/python3
calc1 = 0.0
calc2 = 0.0
operation = ""
while (calc1 != "q"):
    print("\nWhat is the first operator? or, enter q to quit: ")
    calc1 = input() 
    if calc1 == "Q":     
        break
    calc1 = float(calc1)
    print("\nwhat is the second operator? or, enter q to quit: ")
    calc2 = input()
    if calc2 == "q":
        break
    calc2 = float(calc2)
    print("enter an operation to perform on the two operators (+ or -): ")
    operation = input()
    if operation == "+":
        print("\n" + str(calc1) + " + " + str(calc2) + " = " + str(calc1 + calc2))
    elif operation == '-':
        print("\n" + str(calc1) + " - " + str(calc2) + " = " + str(calc1 - calc2))
    else:
        print("\n not a valid entry. Restarting...")
