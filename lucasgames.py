import random

chips = 10

print("--------------------------------")
print("| Welcome to the Lucas Casino! |")
print("|     Credits: Lucas S. O.     |")
print("--------------------------------")

while chips > 0:
    print("You have " + str(chips) + " chips.")
    print("What game do you want to play today?")
    print("")
    print("Dice (1)")
    print("Roulette (2)")
    print("Exit (3)")
    print("")
    question = input("Choose the game-mode you want to play: ")

    if question == "1":
        print("")
        print("Welcome to the Dice Game!")
        print("")
        bet = int(input("How many chips do you want to bet? "))

        if bet > chips:
            print("You don't have enough chips!")
            continue
        print("")
        print("You have " ,str(chips) ,"chips.")

        diceg = input("Under or Over 3.5?: ").lower()
        dicevalue = random.randint(1, 6)
        print("The dice rolled: " ,str(dicevalue))

        if diceg == "over" and dicevalue > 3.5:
            print("Congrats, you won!")
            chips += bet
            print("")
        elif diceg == "under" and dicevalue < 3.5:
            print("Congrats, you won!")
            chips += bet
            print("")
        else:
            print("Sorry, you lost!")
            chips -= bet
            print("")
        print("")
        print("You have " ,str(chips) ,"chips left.")

    elif question == "2":
        print("")
        print("Welcome to the Roulette Game!")
        print("")
        bet = int(input("How many chips do you want to bet? "))

        if bet > chips:
            print("You don't have enough chips!")
            continue

        print("You have " ,str(chips) ,"chips left.")

        brguess = input("Black or Red? ").lower()
        brvalue = random.randint(1, 2)
        color = "black" if brvalue == 1 else "red"
        print("")
        print("It landed on" ,str(color),".")

        if (brguess == "black" and brvalue == 1) or (brguess == "red" and brvalue == 2):
            print("Congrats, you won!")
            chips += bet
            print("")
        else:
            print("Sorry, you lost!")
            chips -= bet
            print("")
        print("")
        print("You have " ,str(chips) ,"chips left.")

    elif question == "3":
        print("Thanks for playing! You ended with", chips, "chips.")
        break

    elif question == "lucaspython":
            print("Secret code redeemed!")
            chips += 10

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")