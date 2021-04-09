import datetime
import random

allowed_users = {'Seyi': {'password': 'seyi', 'account_number': 123456789, 'current_balance': 0}}


# Helper functions


def register(username, password):
	print(f"****Registering {username}*****")
	allowed_users[username] = {'password': password, 'current_balance': 0, 'account_number': generateAccountNumber()}
	return True

def login(username, password):
	if username in allowed_users:
		if password == allowed_users[username]['password']:
			return True
	return False

def generateAccountNumber():
	return int(''.join([str(random.randint(0, 9)) for i in range(10)]))

def operations():
	global exited
	print("Here are the available options:")
	print("1. Withdrawal")
	print("2. Cash deposit")
	print("3. Complaint")

	selected_option = int(input("Please select an option: "))
	if selected_option == 1:
		try:
			amount = int(input("How much would you like to withdraw: "))
		except:
			print("Sorry, invalid input. Please try again.")
		else:
			allowed_users[username]['current_balance'] -= amount
			print("Take your cash!")
			exited = True
	elif selected_option == 2:
		try:
			amount = int(input("How much would you like to deposit: "))
		except:
			print("Sorry, invalid input. Please try again.")
		else:
			allowed_users[username]['current_balance'] += amount
			current_balance = allowed_users[username]['current_balance']
			print(f"Your current balance is, {current_balance} dollars")
			exited = True
	elif selected_option == 3:
		issue = input("What issue would you like to report: ")
		print("Thank you for contacting us!")
		exited = True
	else:
			print("Sorry, invalid selection. Please try again.")

exited = False
while(exited != True):
	print("****Welcome to the bank****")
	print("Let's get you logged in!")
	username = input("What is your username? ")
	password = input("What is your password? ")
	if login(username, password):
		# Get the user's password
		print(f"Welcome, {username}")
		print(f"You logged in at {datetime.datetime.now()}")
		operations()
				
	else:
		print('Sorry, invalid credentials')
		option = input('Would you like to register or try logging in again( input r for register, l for login or e to exit: ' )
		if option.lower() == 'r':
			username = input("What is your username? ")
			password = input("What is your password? ")
			register(username, password)
			print("You have been registered successfully")
		elif option.lower() == 'e':
			exited = True

