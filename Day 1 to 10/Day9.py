from art import logo
import os

print(logo)
print("Welcome to the secret auction program")
biders = {}
def ask():
    name = input("What is Your Name? : ")
    bid = int(input("What's your Bid? : "))
    biders[name] = bid
    next = input("Are there any other bidders? Type 'Yes' or 'No' : ").lower()
    if next == "yes":
        os.system('clear')
        ask()
    else:
        max = 0
        for i in biders:
            if max < biders[i]:
                max = biders[i]
        print(f"The winner is {i} with a bid of {max}")
ask()