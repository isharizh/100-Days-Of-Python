import random
# lis = ["Head", "Tail"]
# rani = random.randint(0,1)
# print(lis[rani])

# inname = input("Enter list of names : ")
# name =  inname.split(", ")
# ranname = random.choice(name)
# print(ranname," is going to by the meal today")

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# col = int(position[0])
# row = int(position[1])
# map[row-1][col-1] = "X"
# print(f"{row1}\n{row2}\n{row3}")


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
handlis = [rock, paper, scissors]
hucho = int(input( " \n \n What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors : "))
print(handlis[hucho])
macho = random.randint(0, 2)
print("Computer Choice: ", handlis[macho])
if (hucho == 0 and macho == 0) or (hucho == 1 and macho == 1) or (hucho == 2 and macho == 2):
    print("Draw")
elif (hucho == 0 and macho == 2) or (hucho == 1 and macho == 0) or (hucho == 2 and macho == 1):
    print("You Won")
else:
    print("You Lose")