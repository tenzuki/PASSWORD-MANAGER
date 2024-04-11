""" A SIMPLE PASSWORD MANAGER IN PYTHON """
from cryptography.fernet import Fernet
import os 

def write_key():
    key = Fernet.generate_key()
    with open(("key.key"), "wb") as key_files:
        key_files.write(key)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key 

key = load_key() 
fer = Fernet(key)

def add ():
    name = input("USERNAME :- ")
    passw = input("PASSWORD :- ")

    with open("password.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(passw.encode()).decode() + "\n")

def view():
    if os.path.getsize("password.txt") == 0:
        print("There are no active records to show.")
        return "empty"
    else:
        # Create a dictionary to store usernames and passwords
        user_pass_dict = {}

        with open("password.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                data = line.rstrip()
                if "|" in data:
                    user, passw = data.split("|")
                    user_pass_dict[user] = passw

        # Print all usernames
        print("Usernames:")
        for user in user_pass_dict.keys():
            print(user)

        # Ask the user for the username they want to view
        selected_user = input("Enter the username you want to view: ")

        # Check if the selected username exists in the dictionary
        if selected_user in user_pass_dict:
            try:
                decrypted_passw = fer.decrypt(user_pass_dict[selected_user].encode()).decode()
                print("USERNAME :- ", selected_user, " PASSWORD :- ", decrypted_passw)
            except:
                print("Error: Could not decrypt the password for user", selected_user)
        else:
            print("Error: The selected username does not exist.")

        return "not empty"


    
while True:
    mode = input("what would you like to do view , add or quit (q) :- ")
    if mode == "q":
        break
    elif mode == "view":
        result = view()
        if result == "empty":
            mode = input("if you want to add a record type add or q to quit :- ")
            if mode == "add":
                add()
            elif mode == "q":
                break
    elif mode == "add":
        add()
    else:
        print("invalid input")
        continue