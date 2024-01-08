# import math
# def can(height, width):
#     cans = math.ceil((height + width) / 5)
#     print("You'll need ",cans, " cans of paint")
    
    
# height = int(input("Enter Height:"))
# width = int(input("Enter Width:"))
# can(height, width)


# def prime(n):
#     for i in range(2,n):
#         if n % i ==0 :
#             print("Its not a Prime number!")
#             break
#         else:
#             print("Its a Prime number!")
#             break
    
# n = int(input("Enter Number:"))
# prime(n)


# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message:\n").lower()
# shift = int(input("Type the shift number:\n"))

# def encode(text,shift):
#     textt = ""
#     for i in text:
#         if i in alphabet:
#              a = alphabet.index(i) + shift
#              textt += alphabet[a]
#         else:
#             textt += i
#     print("Encrypted message: ",textt)
    


# def decode(text,shift):
#     textt = ""
#     for i in text:
#         if i in alphabet:
#             a = alphabet.index(i) - shift
#             textt += alphabet[a]
#         else:
#             textt += i
#     print("Decrypted message: ",textt)

# if direction == 'encode':
#     encode(text,shift)
# else:
#     decode(text,shift)


import Day7
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
  textt = ""
  for i in text:
        if i in alphabet:
            if direction == 'encode':
                a = alphabet.index(i) + shift
            elif direction == 'decode':
                a = alphabet.index(i) - shift
            textt += alphabet[a]
        else:
            textt += i  
  if direction == 'encode':
        print("Encrypted message: ", textt)
  elif direction == 'decode':
        print("Decrypted message: ", textt)

    
  print(f"Here's the {direction}d result: {text}")


print(Day7.logo)

def call():
  direction = input("Type 'encode' to encrypt, type 'decode' to  decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  caesar(text, shift, direction)
call()
ask = input("Type 'yes' if you want to go again. Otherwise type 'no' : ").lower()
while ask == "yes":
  call()