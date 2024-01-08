from os import system
import sys
from art import logo1



def calculator():
    
    system('clear')
    print(logo1)
    def add(a,b):
        return a+b

    def sub(a,b):
        return a-b

    def mul(a,b):
        return a*b

    def div(a,b):
        return a/b

    sym = {'+':add,
        '-':sub,
        '*':mul,
        '/':div}

    a = float(input("Enter the first number :"))

    for keys in sym:
        print(keys)
    ans = 0
    test = True
    while test:
        op = input("Pick an opertion : ")
        b = float(input("Enter next number : "))
        value = sym[op]
        ans = value(a, b)
        print(f"{a} {op} {b} = {ans}")  
    
        ask = input(f"Type 'y' to continue calculating with {ans}, or type 'n' to exit. : ")
    
        if ask == 'y':
            a = ans
        else:
            test = False
            system('clear')   
            calculator()
            
calculator()
        