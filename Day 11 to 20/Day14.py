import random
from os import system
from art import logo4, logo5
from data import data

def A(data):
    return random.choice(data)

def game(data):
    c = 0
    a = A(data)
    while True:
        system("clear")
        print(logo4)
        if c > 0:
            print(f"You're right! Current Score: {c}.")
        print(f"Compare A: {a['name']}, {a['description']}, {a['country']}.")
        print(logo5)
        print(f"Compare b: {b['name']}, {b['description']}, {b['country']}.")
        ask = input("Who has more followers? Type 'A' or 'B': ")
        if ask == "A" :
            if a['follower_count'] > b['follower_count']:
                c += 1
                a = b
            else:
                system('clear')
                print(logo4)
                print(f"Sorry that's wrong. Final score: {c}.")
                break
        elif ask == "B" :
            if a['follower_count'] < b['follower_count']:
                c += 1
                a = b
            else:
                system('clear')
                print(logo4)
                print(f"Sorry that's wrong. Final score: {c}.")
                break
                
game(data)