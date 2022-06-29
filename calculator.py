#Created by Derias https://github.com/Derias20
from secrets import choice


def add(a, b):
    return a + b 
def subsract(a, b):
    return a - b
def divide(a,b):
    return a / b
def multiply (a, b):
    return a * b
print("Hello! Give me two numbers please!")
a = int(float(input("Enter your first number: ")))
b = int(float(input("Enter your second number: ")))
print("What should i do? Here are the options below")
print("1.Add")
print("2.Subtract")
print("3.Divide")
print("4.Multiply")  
choice = str(input(""))
if choice == "1":
    print(add(a,b))
elif choice == "2":
    print(subsract(a,b))
elif choice == "3":
    print(divide(a,b))
elif choice == "4":
    print(multiply(a,b))    
         