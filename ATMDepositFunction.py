# Michaela Pierce
# Partner: Jordan Bell
# Completed as a group homework assignment
# Date of Creation: September 1, 2023 (Initially, Google Colab was utilized as per the course requirements).


"""
This code simulates a simple ATM system. It first prompts the user to enter
a password and then allows them to either withdraw or deposit money. It
maintains an account balance and ensures that withdrawals do not exceed
the balance.
"""

password = str()

while password != "123":
    print("Please enter your password: ")
    password=input()

print("Login was successful!")

balance = 1000
rem_balance= 1000

print("Welcome to Seahawk ATM")
print("Please select from the following options: ")
menu_options=("1. Withdrawal 2. Deposit")
print(menu_options)
user_choice= int(input("Please enter the option you would like: "))

def withdrawal(w_amount):
    global rem_balance
    if w_amount<=balance:
        rem_balance=(balance)-(w_amount)
        print("Remaining balance is: ", rem_balance)
    else:
        # if user tries to withdrawal more than their account balance
        print("You cannot withdrawal more than your balance")
        print("Remaining balance is", rem_balance)


def deposit(d_amount):
    global rem_balance
    rem_balance = (balance)+(d_amount)
    print("Remaining balance is: ", rem_balance)


if user_choice == 1:
    # withdrawal function
    w_amount=int(input("Please enter the amount you would like to withdrawal: "))
    withdrawal(w_amount)
elif user_choice == 2:
    # deposit function
    d_amount=int(input("Please enter the amount you would like to deposit: "))
    deposit(d_amount)
else:
    print("Sorry, that option is unavailable. Please try again.")




