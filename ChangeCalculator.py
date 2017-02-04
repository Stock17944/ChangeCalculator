from termcolor import colored
import time
while True:
    user_input=input("Enter change:\n")
    try:
        f=float(user_input)
        break
    except ValueError:
        print("Please enter a " + colored("number", "magenta", attrs=["underline"]) + ".")
        time.sleep(1)
while True:
    quarters = f // .25
    quartersv = quarters * .25
    dimes = round(f-quartersv, 2) // .10
    dimesv = dimes * .10
    nickels = round(f-quartersv-dimesv, 2) // .05
    nickelsv = nickels * 0.05
    pennies = round(f-quartersv-dimesv-nickelsv, 2) // .01
    penniesv = pennies * 0.01
    if round(f-quartersv, 2) == 0:
        print("You need {} quarters.".format(int(quarters)))
        break
    elif round(f-quartersv-dimesv, 2) == 0:
        print("You need {} quarters, and {} dimes.".format(int(quarters), int(dimes)))
        break
    elif round(f-quartersv-dimesv-nickelsv, 2) == 0:
        print("You need {} quarters, {} dimes, and {} nickels.".format(int(quarters), int(dimes), int(nickels)))
        break
    elif round(f-quartersv-dimesv-nickelsv-penniesv, 2) == 0:
        print("You need {} quarters, {} dimes, {} nickels, and {} pennies".format(int(quarters), int(dimes), int(nickels), int(pennies)))
        break
        print("You need {} quarters, {} dimes, and {} nickels.".format(int(quarters), int(dimes), int(nickels)))
        break
