# two = input("Enter a two digit number:")
# tot = int(two[0])+ int(two[1])
# print("The sum is ",two[0]," + ", two[1],  " = ",tot)

# BMI Calculator

# height = input("Enter the height : ")
# weight = input("Enter the weight : ")
# bmi = int(weight)/(float(height)**2)
# print(int(bmi))

# age = int(input("Enter your age : "))
# reage = 90-age
# mon = reage * 12
# weeks = int(reage * 52.143)
# days = int(reage*365.25)
# print(f"You have {days} Days, {weeks} Weeks, {mon} Months left.")

# print("Welcome to the Tip Calculator")

# bill = float(input("What was the total bill? $"))
# tip = int(input("How much tip would you like to give? 10, 12 or 15? "))
# n = int(input("How many people to split the bill? "))

# tot_cost = bill * (1+(tip/100))
# splitup = round((tot_cost/n),2)

# print(f"Each person should pay : ${splitup}")

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"The {cipher_direction} text is {end_text}")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
shoul_continue = True
while shoul_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift,cipher_direction=direction)
    result = input("Type 'yes' if you want to do again. Otherwise type 'no'.\n")
    if result == "no":
        shoul_continue = False
        print("Goodbye")