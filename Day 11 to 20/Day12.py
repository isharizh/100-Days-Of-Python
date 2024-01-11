import random
from art import logo3
import os 

os.system('clear')
print(logo3)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
num = random.randint(1, 100)
choice = input("Choose a difficulty.Type 'easy'or 'hard': ")

if choice == 'easy':
    a = 10
elif choice == 'hard':
    a = 5

while not a==0:
    print(f"You have {a} attempts remaining to guess the number.")
    guess = int(input("Make a guess : "))
    a -= 1
    if num == guess-1 or num == guess+1:
        print("You're Neareat to the answer.")
    elif guess == num:
        print("you got it! The answer was ", num)
        break
    elif guess > num:
        print("Too High!")
    elif guess < num:
        print("Too Low!")
if a==0:    
    print("You've run out of attempts to guess the number, so you lose")