import random
from replit import clear
from art import logo


# USED TO GENERATE A HAND
def deal_card(hand):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    hand.append(card)
    if 11 in hand and calculate_score(hand) > 21:
        for i in range(len(hand)):
            # instead of using remove/append, this for loop keeps card location in hand intact
            if hand[i] == 11:
                hand[i] = 1
    return hand


# USED TO GET THE SUM OF THE CARDS TO COMPARE AT THE END OF THE GAME
def calculate_score(hand):
    if sum(hand) == 21 and len(hand) == 2:
        return 0
    return sum(hand)


# USED TO DETERMINE WINNER AND INFORM USER OF THE RESULT
def compare_scores(user_score, dealer_score):
    if dealer_score > 21 and user_score > 21:
        return "You busted. You lose."
    if dealer_score == user_score:
        return "It's a draw.\n"
    elif dealer_score == 0:
        return "The dealer got Blackjack! You lose.\n"
    elif user_score == 0:
        return "You got Blackjack! You win.\n"
    elif user_score > 21:
        return "You busted. You lose.\n"
    elif dealer_score > 21:
        return "The dealer busted. You win.\n"
    elif dealer_score > user_score:
        return "The dealer had a higher score than you. You lose.\n"
    return "You had a higher score than the dealer. You win.\n"


# MAIN GAME
def blackjack():
    user_cards = []
    dealer_cards = []
    is_game_over = False

    print(logo)

    for i in range(2):
        deal_card(user_cards)
        deal_card(dealer_cards)

    print(f"Dealer's first card: {dealer_cards[0]}")
    print(f"Your cards: {user_cards}. Current score: {calculate_score(user_cards)}.\n")

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            hit_or_stand = input("Do you want to '(h)it' or '(s)tand'? \n").lower()
            print("\n")
            if hit_or_stand == "hit" or hit_or_stand == "h":
                deal_card(user_cards)
                print(f"Dealer's first card: {dealer_cards[0]}")
                print(f"Your cards: {user_cards}. Current score: {calculate_score(user_cards)}.\n")
            elif hit_or_stand == "stand" or hit_or_stand == "s":
                is_game_over = True

    while dealer_score != 0 and dealer_score < 17:
        deal_card(dealer_cards)
        dealer_score = calculate_score(dealer_cards)

    print("\n")
    if dealer_score == 0:
        print(f"Dealer's final hand: {dealer_cards}, final score: 21.")
    else:
        print(f"Dealer's final hand: {dealer_cards}, final score: {dealer_score}.")
    if user_score == 0:
        print(f"Your final hand: {user_cards}, final score: 21.\n")
    else:
        print(f"Your final hand: {user_cards}, final score: {user_score}.\n")
    print(compare_scores(user_score, dealer_score))


# START OF THE PROGRAM. ALLOWS GAME TO LOOP INSTEAD OF ENDING THE PROGRAM IF USER CHOOSES
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': \n") == "y":
    clear()
    blackjack()