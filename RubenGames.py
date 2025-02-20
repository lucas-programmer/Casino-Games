import random

# Define the ranks and suits of a deck of cards
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Initialize total chips
total_chips = 5

# Function to create a deck of cards
def create_deck():
    deck = [{'rank': r, 'suit': s} for r in ranks for s in suits]
    random.shuffle(deck)
    return deck

# Function to deal a card from the deck
def deal_card(deck):
    return deck.pop()

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    total = sum([get_card_value(card) for card in hand])
    # Adjust for Aces
    for card in hand:
        if card['rank'] == 'A' and total > 21:
            total -= 10
    return total

# Function to get the value of a card
def get_card_value(card):
    if card['rank'] in ['J', 'Q', 'K']:
        return 10
    elif card['rank'] == 'A':
        return 11
    else:
        return int(card['rank'])

# Function to play Blackjack
def play_blackjack():
    global total_chips
    print("\n" + "="*40)
    print("Blackjack Game")
    print("Made By Ruben")
    print("="*40)
    
    while total_chips > 0:
        print(f"\nYou have {total_chips} chips.")
        bet = int(input("How many chips would you like to bet? "))
        while bet > total_chips or bet <= 0:
            print("Invalid bet. Please enter a number between 1 and", total_chips)
            bet = int(input("How many chips would you like to bet? "))
        
        deck = create_deck()
        player_hand = [deal_card(deck), deal_card(deck)]
        dealer_hand = [deal_card(deck), deal_card(deck)]
        
        print("\nYour Hand:")
        for card in player_hand:
            print(f"{card['rank']} of {card['suit']}")
        print(f"Total: {calculate_hand_value(player_hand)}")
        
        print("\nDealer's Up Card:")
        print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")
        
        while True:
            action = input("\nDo you want to 'hit' or 'stand'? ")
            if action.lower() == 'hit':
                player_hand.append(deal_card(deck))
                print("\nYour Hand:")
                for card in player_hand:
                    print(f"{card['rank']} of {card['suit']}")
                print(f"Total: {calculate_hand_value(player_hand)}")
                if calculate_hand_value(player_hand) > 21:
                    print("\nYou busted! Dealer wins.")
                    total_chips -= bet
                    break
            elif action.lower() == 'stand':
                break
            elif action.lower() == 'rubengames':
                print("\nSecret code accepted! You have been awarded 10 extra chips.")
                total_chips += 10
                break
            else:
                print("Invalid action. Please enter 'hit' or 'stand'.")
        
        if calculate_hand_value(player_hand) <= 21:
            print("\nDealer's Hand:")
            for card in dealer_hand:
                print(f"{card['rank']} of {card['suit']}")
            print(f"Total: {calculate_hand_value(dealer_hand)}")
            while calculate_hand_value(dealer_hand) < 17:
                dealer_hand.append(deal_card(deck))
                print("\nDealer's Hand:")
                for card in dealer_hand:
                    print(f"{card['rank']} of {card['suit']}")
                print(f"Total: {calculate_hand_value(dealer_hand)}")
            if calculate_hand_value(dealer_hand) > 21:
                print("\nDealer busted! You win.")
                total_chips += bet
            elif calculate_hand_value(dealer_hand) < calculate_hand_value(player_hand):
                print("\nYour total is higher. You win.")
                total_chips += bet
            elif calculate_hand_value(dealer_hand) > calculate_hand_value(player_hand):
                print("\nDealer's total is higher. Dealer wins.")
                total_chips -= bet
            else:
                print("\nIt's a tie. Your bet is returned.")
        
        print("\nDo you want to play another round of Blackjack or quit to the main menu? (1 for another round, 2 to quit)")
        choice = int(input("Enter your choice: "))
        while choice < 1 or choice > 2:
            print("Invalid choice. Please enter 1 or 2.")
            choice = int(input("Enter your choice: "))
        if choice == 2:
            break
    
    print("\nYou've run out of chips. Game over.")

# Function to play Roulette
def play_roulette():
    global total_chips
    print("\n" + "="*40)
    print("Roulette Game")
    print("Made By Ruben")
    print("="*40)
    
    while total_chips > 0:
        print(f"\nYou have {total_chips} chips.")
        bet = int(input("How many chips would you like to bet? "))
        while bet > total_chips or bet <= 0:
            print("Invalid bet. Please enter a number between 1 and", total_chips)
            bet = int(input("How many chips would you like to bet? "))
        
        print("\nPlace Your Bet:")
        print("1. Red")
        print("2. Black")
        print("3. Odd")
        print("4. Even")
        print("5. High (19-36)")
        print("6. Low (1-18)")
        choice = int(input("Enter your choice: "))
        while choice < 1 or choice > 6:
            print("Invalid choice. Please enter a number between 1 and 6.")
            choice = int(input("Enter your choice: "))
        
        winning_number = random.randint(1, 36)
        print(f"\nThe winning number is: {winning_number}")
        
        if choice == 1:
            if winning_number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
                print("\nYou win!")
                total_chips += bet
            else:
                print("\nYou lose.")
                total_chips -= bet
        elif choice == 2:
            if winning_number in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]:
                print("\nYou win!")
                total_chips += bet
            else:
                print("\nYou lose.")
                total_chips -= bet
        elif choice == 3:
            if winning_number % 2 != 0:
                print("\nYou win!")
                total_chips += bet
            else:
                print("\nYou lose.")
                total_chips -= bet
        elif choice == 4:
            if winning_number % 2 == 0:
                print("\nYou win!")
                total_chips += bet
            else:
                print("\nYou lose.")
                total_chips -= bet
        elif choice == 5:
            if winning_number >= 19:
                print("\nYou win!")
                total_chips += bet
            else:
                print("\nYou lose.")
                total_chips -= bet
        elif choice == 6:
            if winning_number <= 18:
                print("\nYou win!")
                total_chips += bet
            else:
                print("\nYou lose.")
                total_chips -= bet
        
        print("\nDo you want to play another round of Roulette or quit to the main menu? (1 for another round, 2 to quit)")
        choice = int(input("Enter your choice: "))
        while choice < 1 or choice > 2:
            print("Invalid choice. Please enter 1 or 2.")
            choice = int(input("Enter your choice: "))
        if choice == 2:
            break
    
    print("\nYou've run out of chips. Game over.")

# Function to play Dice
def play_dice():
    global total_chips
    print("\n" + "="*40)
    print("Dice Game")
    print("Made By Ruben")
    print("="*40)
    
    while total_chips > 0:
        print(f"\nYou have {total_chips} chips.")
        bet = int(input("How many chips would you like to bet? "))
        while bet > total_chips or bet <= 0:
            print("Invalid bet. Please enter a number between 1 and", total_chips)
            bet = int(input("How many chips would you like to bet? "))
        
        print("\nPlace Your Bet:")
        print("1. Over 3.5")
        print("2. Under 3.5")
        choice = int(input("Enter your choice: "))
        while choice < 1 or choice > 2:
            print("Invalid choice. Please enter 1 or 2.")
            choice = int(input("Enter your choice: "))
        
        roll = random.randint(1, 6)
        print(f"\nThe roll is: {roll}")
        
        if choice == 1:
            if roll > 3.5:
                print("\nYou win!")
                total_chips += bet
            else:
                print("\nYou lose.")
                total_chips -= bet
        elif choice == 2:
            if roll < 3.5:
                print("\nYou win!")
                total_chips += bet
            else:
                print("\nYou lose.")
                total_chips -= bet
        
        print("\nDo you want to play another round of Dice or quit to the main menu? (1 for another round, 2 to quit)")
        choice = int(input("Enter your choice: "))
        while choice < 1 or choice > 2:
            print("Invalid choice. Please enter 1 or 2.")
            choice = int(input("Enter your choice: "))
        if choice == 2:
            break
    
    print("\nYou've run out of chips. Game over.")

# Main function
def main():
    global total_chips
    print("\n" + "="*40)
    print("Casino Games")
    print("Made By Ruben")
    print("="*40)
    
    while True:
        print(f"\nYou have {total_chips} chips.")
        print("1. Blackjack")
        print("2. Roulette")
        print("3. Dice")
        print("4. Quit")
        choice = input("Enter your choice: ")
        if choice == "rubengames":
            print("\nSecret code accepted! You have been awarded 10 extra chips.")
            total_chips += 10
        elif choice == "1":
            play_blackjack()
        elif choice == "2":
            play_roulette()
        elif choice == "3":
            play_dice()
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# Call the main function
main()
