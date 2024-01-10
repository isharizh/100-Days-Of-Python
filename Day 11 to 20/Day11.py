import random
from os import system
from art import logo2

def card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
 
def call():
    print(logo2)
    user = [card(), card()]
    print(f"Your Cards : {user}, current score: {sum(user)}")
    comp = [card(), card()]
    
    while True:
        print(f"Computer's first card: {comp[0]}")
        if sum(user) == 21:
            print("BlackJack! You Win")
            break
        ask = input("Type 'y' to get another card, type 'n' to pass: ")
        while ask == 'y':
            user.append(card())
            print(f"Your Cards : {user}, current score: {sum(user)}")
            if 11 in user and sum(user) > 21:
                user[user.index(11)] == 1
            print(f"Computer's first card: {comp[0]}")
            if 11 in comp and sum(comp) > 21:
                comp[comp.index(11)] == 1
            if sum(comp) == 21:
                print("You Lose")
                break
            ask = input("Type 'y' to get another card, type 'n' to pass: ")
                
        else:
            while sum(comp) < 17:
                comp.append(card())
            print(f"Your final hand : {user}, final score: {sum(user)}")
            print(f"Computer's final hand: {comp}, current score: {sum(comp)}")
            if sum(user) < sum(comp) and sum(comp) > 21:
                print("Opponent went over. You win ")
            elif sum(comp) < sum(user) and sum(user) > 21:
                print("You went over. You lose ")
            elif sum(comp) > sum(user) and sum(comp) <= 21:
                print("You Lose")
            elif sum(user) > sum(comp) and sum(user) <= 21:
                print("You Win")
            elif sum(user) == sum(comp):
                print("Its a Draw")
                
        break
    yn = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if yn == 'y':
        system("clear")
        call()
            
system("clear")
call()
