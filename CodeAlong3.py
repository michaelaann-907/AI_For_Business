"""
Code Along 3 - In Class - Python
This is to make sure all students understand Python basics in order to apply to datasets.

Description:
This script covers various concepts such as function definitions, basic arithmetic
operations, working with user inputs, utilizing built-in functions, and implementing
simple ATM functionalities. The code demonstrates the usage of functions for addition,
handling user inputs for calculator operations and ATM transactions, generating random
numbers, and controlling program flow with loops and conditional statements.


#The remainder of the ATM Code is completed in another file since it was completed as
homework.

Date of Creation: August 30, 2023 (Initially, Google Colab was utilized as per the course requirements).
"""



# Functions
print("Hello Allie")
print("Hello Axel!")

def hello():
    print("Hello Axel! From my function!")

hello()

print("Addition from two numbers", 5+7)

# Addition function
def addition(a,b):
    print("Result from addition of two numbers: ", "a = ", a, "b = ", b, "is : ", a+b)

addition(5,8)
addition(5,10)

y = min(5,10,20)
print(y)

x = abs(5)
print(x)

x = pow(2,3)
print(x)

import math

x = math.ceil(1.7)
y = math.floor(1.7)

print(x)
print(y)

x = math.pi
print(x)

# Calculator with user input

# Addition function
def addition(a,b):
    print("Result from addition of two numbers: ", "a = ", a, "b = ", b, "is : ", a+b)

a = int(input("Please enter a value for a: "))  # remember to put 'int' otherwise it assumes a string is entered
b = int(input("Please enter a value for b: "))

addition(a,b)

import random

num = random.randint(1,5)  # guess a random number between 1-5
guess = None

while guess != num:
    guess = input("Guess number between 1-5: ")
    guess = int(guess)

    if guess == num:
        print("Congrats, it is correct!")
        print("Computer guessed: ", num)
        break
    else:
        print("Please try again!")
        print("Computer guessed: ", num)
        # use break if want to end program otherwise it will ask again

random.seed(42)  # seed value is the number I want the computer to use to generate a random #
random.randint(1,100)

# ATM Machine Software

password = str()

while password != "123":
    print("Please enter your password: ")
    password = input()

print("Login was successful!")

balance = 1000
withdrawal = 0
rem_balance = 1000

print("Welcome to Seahawk ATM")
print("Enter 1 for withdrawal, 2 for deposit: ")
print("How much do you want to withdrawal: ")
withdrawal = int(input())

if withdrawal <= balance:
    rem_balance = (balance) - (withdrawal)
    print("Remaining balance is: ", rem_balance)
else:
    # if user tries to enter more than what is in the account
    print("You cannot withdrawal more than your balance")
    print("Remaining balance is: ", rem_balance)

password = str()

while password != "123":
    print("Please enter your password: ")
    password = input()

print("Login was successful!")

balance = 1000
rem_balance = 1000

print("Welcome to Seahawk ATM")
print("Please select from the following options: ")
menu_options = ("1. Withdrawal 2. Deposit")
print(menu_options)
user_choice = int(input("Please enter the option you would like: "))

def withdrawal(w_amount):
    global rem_balance
    if w_amount <= balance:
        rem_balance = (balance) - (w_amount)
        print("Remaining balance is: ", rem_balance)
    else:
        # if user tries to withdrawal more than their account balance
        print("You cannot withdrawal more than your balance")
        print("Remaining balance is", rem_balance)

def deposit(d_amount):
    global rem_balance
    rem_balance = (balance) + (d_amount)
    print("Remaining balance is: ", rem_balance)

if user_choice == 1:
    # withdrawal function
    w_amount = int(input("Please enter the amount you would like to withdrawal: "))
    withdrawal(w_amount)
elif user_choice == 2:
    # deposit function
    d_amount = int(input("Please enter the amount you would like to deposit: "))
    deposit(d_amount)
else:
    print("Sorry, that option is unavailable. Please try again.")
