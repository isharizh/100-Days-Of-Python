# stuhi = input("Enter a list of students heights: ").split()
# for n in range(0, len(stuhi)):
#     stuhi[n] = int(stuhi[n])
# print(stuhi)
# sum = 0
# z = 0 
# for i in stuhi:
#     sum += i
#     z += 1
# avg = sum / z
# print("Average Height : ", round(avg))


# score = input("Enter a list of scores : ").split()
# for n in range(0, len(score)):
#     score[n] = int(score[n])
# print(score)
# max = 0
# for i in score:
#     if max < i:
#         max = i
# print(max)

# sum = 0
# for i in range(0, 101, 2):
#     sum += i
#     print(i)
# print(sum)


# for i in range(1, 101):
#     if (i%3 == 0) and (i%5 == 0):
#         print("FizzBuzz")
#     elif i%5 == 0:
#         print("Buzz")
#     elif i%3 == 0:
#         print("Fizz")
#     else:
#         print(i)

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
let = int(input("\n How many letters would you like in your password?\n")) 
sym = int(input(f"How many symbols would you like?\n"))
num = int(input(f"How many numbers would you like?\n"))

passlist = [random.choice(letters) for i in range(let)] + [random.choice(numbers) for i in range(num)] +[random.choice(symbols) for i in range(sym)]
random.shuffle(passlist)
password = ""
for i in passlist:
    password += i
print("Password: " + password)