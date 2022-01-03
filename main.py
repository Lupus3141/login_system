# cmd login system using hash

import json
import hashlib
import random

def hash(to_hash):
	return hashlib.sha256(str(to_hash).encode('utf-8')).hexdigest()


def load_userdata(file):
	global userdata
	with open(file) as f:
		userdata = json.load(f)

def store_userdata(file):
	with open(file, "w") as f:
		json.dump(userdata, f, sort_keys=True, indent=4)

def login():
	print("\nPlease enter your credentials: ")
	while True:
		user_name = input("Username: ")
		password = input("Password: ")
		if user_name in userdata: # does the user exist?
			if userdata[user_name][0] == hash(password+userdata[user_name][1]): # Is the hash from password+salt equal to hash in database?
				print("\nLogin succesfull!")
				break
		print("\nUsername or password incorrect, try again!\n")
		
def sign_up():
	print("\nPlease create an account: ")
	while True:
		user_name = input("Username: ")
		password = input("Password: ")
		password2 = input("Password (validation): ")
		if password == password2:
			if user_name not in userdata:
				create_user(user_name, password)
				print("You've signed up succesfully")
				break
			else:
				print("\nPlease use another username\n")
		else:
			print("\nCheck your passwords\n")

def create_user(user_name, password):
	salt = str(random.randint(10000000000000, 99999999999999))
	userdata[user_name] = [hash(password+salt), salt]

userdata = {}
load_userdata("userdata.json")
print("What would you like to do?")
print("1. Login")
print("2. Sign up")

while True:
	choice = input("Your choice: ")
	if (choice == "1"):
		login()
		break
	elif (choice == "2"):
		sign_up()
		break
	else:
		print("Invalid input, try again")
store_userdata("userdata.json")
