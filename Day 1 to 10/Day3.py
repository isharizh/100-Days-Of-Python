# print("Check ODD or EVEN")
# n = int(input("Enter a Number: "))
# if n%2 == 0:
#   print("The Given Number is Even")
# else:
#   print("The Given Number is Odd")
###########################################

# height = input("Enter the height : ")
# weight = input("Enter the weight : ")
# bmi = round(int(weight)/(float(height)**2))
#
# if bmi < 18.5:
#   print(f"Your BMI is {bmi}, you are underweight")
# elif bmi==18.5 or bmi<25:
#   print(f"Your BMI is {bmi}, you have a normal weight.")
# elif bmi==25 or bmi<30:
#   print(f"Your BMI is {bmi}, you are slightly overweight")
# elif bmi==30 or bmi<35:
#   print(f"Your BMI is {bmi}, you are obese")
# else:
#   print(f"Your BMI is {bmi}, you are clinically obese")


###################################################################

# year = int(input("Enter a year to check : "))
# if year%4==0:
#   if year%100==0:
#     if year%400==0:
#       print("Leap Year")
#     else:
#       print("Not a Leap Year")
#   else:
#     print("Leap Year")
# else:
#   print("Not a Leap Year")


###################################################################

'''
print("Welcome to the Python Pizza Delz")
size = input("What size Pizza do you need? S, M, or L : ").lower()
add_pep = input("Do you want pepperoni? Y or N : ").lower()
ex_che = input("Do you need extra cheese? Y or N : ").lower()
bill = 0

if size == "s":
  bill += 15
elif size == "m":
  bill += 20
else:
  bill += 25

if add_pep == "y":
  if size == 's':
    bill+=2
  else:
    bill+=3

if ex_che == 'y':
  bill+=1

print(f"Your Total Bill is : ${bill}")
'''


###################################################################


# print("Welcome to the Love Calculator!")
# name1 = input("What is your name : ").lower()
# name2 = input("What is their name : ").lower()
# name = name1 + name2
#
# T = name.count("t")
# R = name.count("r")
# U = name.count("u")
# E =name.count("e")
# t_tot = T+R+U+E
#
# L = name.count("l")
# O = name.count("o")
# V = name.count("v")
# E1 = name.count("e")
# l_tot = L+O+V+E1
#
# tot = str(t_tot) + str(l_tot)
# tot = int(tot)
#
# if tot < 10 or tot > 90:
#   print(f"Your score is {tot}, you go together like coke and mentos")
# elif tot >= 40 and tot <= 50:
#   print(f"Your score is {tot}, you are alright together")
# else:
#   print(f"Your score is {tot}, you are made for each other")
#
  ##################################################################


from easygui import *

text = '''You're at a crossroad. Where do you want to go?'''

title = "🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆Tresure game🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆"

choices = [" ⬅️ Left ⬅️ ", " ➡️ Right ➡️ "]
output = choicebox(text, title, choices)

if output == " ⬅️ Left ⬅️ ":
  text1 = "You've come to a lake. There is an island in the middle of the lake."
  choice2 = ["Wait for a Boat ⛵️⛵️⛵️⛵️⛵️", "Swim across 🏊🏼🏊🏼🏊🏼🏊🏼🏊🏼"]
  output1 = choicebox(text1, title, choice2)
else:
  msg = msgbox("Game Over!", title)

if output1 == "Wait for a Boat ⛵️⛵️⛵️⛵️⛵️":
  text2 = "You arrive at the island unharmed. There is a house with 3 doors. Choose one from below"
  choice3 = ["🔴 Red 🔴", "🟡 Yellow 🟡", "🟣 Violet 🟣"]
  output2 = choicebox(text2, title, choice3)
else:
  msg = msgbox("Game Over!", title)

if output2 == "🔴 Red 🔴":
  msg = msgbox("It's a room full of fire. Game Over.", title)

elif output2 == "🟡 Yellow 🟡":
  msg = msgbox('''🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆
               
  You found the treasure! You Won!  
  
  🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆🔆''', title)
else:
  msg = msgbox("You enter a room of beasts. Game Over", title)

