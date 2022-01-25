#!/usr/bin/env python3.8
from credentials import AccountCredentials
import random
import string

# create account


def create_account(username, password, key, acc):
    new_account = AccountCredentials(username, password, acc, key)
    return new_account

# save account


def save_accounts(account):
    """function to save account"""
    account.save_account()

# Delete account


def delete_account(account):
    """function to delete account"""
    account.delete_account()

# find account


def find_account(acckey):
    """function that finds a key and returns the account"""

    return AccountCredentials.find_by_key(acckey)

# check if account exists


def check_existing_accounts(acckey):
    """function that checks if acount exists with that key and returns boolean"""

    return AccountCredentials.account_exist(acckey)

# display all accounts


def display_accounts():
    """function that returns all saved accounts"""

    return AccountCredentials.display_accounts()

# delete an account


def delete_account(account):
    """function that deletes an account"""
    account.delete_account()


def generate_random_password():
    source = string.ascii_letters + string.digits
    result_str = ''.join((random.choice(source) for i in range(8)))
    print(result_str)
    return result_str

# main function


def main():
    print("Hello Welcome to password locker...\nWHAT WOULD YOU LIKE TO DO\n")

    while True:
        print("Use these sort codes: \nsa - save Account, \nda -display accounts, \nfa - find account, \ndel - delete account, \nexit -exit the application\n")

        short_code = input().lower()

        if short_code == 'sa':
            print("New Account")
            print("-"*10)

            print("Username............")
            username = input()

            print("Create Password\n 1:create my own password 2:generate password")
            choice = input("Enter your choice: ")

            if(choice == "1"):
                print("Enter Password:")
                password = input()
            elif(choice == "2"):
                password = generate_random_password()
            else:
                print("Please choose an option")

            print("Name of the Account..")
            account = input()

            print("Key.................")
            key = input()

            save_accounts(create_account(username, password, account, key))
            print("\n")
            print(f"New {account} account created\n")

        elif short_code == 'da':

            if display_accounts():
                print("Here is a list of all your accounts\n")

                for account in display_accounts():
                    print(f"{account.acc} Account Credentials")
                    print(
                        f"username:{account.username} ... password:{account.password}...Key:{account.key}")
                    print("\n")
            else:
                print("\n You don't have any saved accounts yet\n")

        elif short_code == 'fa':
            print("Enter key for account you want to search")

            search_key = input()
            if check_existing_accounts(search_key):
                search_account = find_account(search_key)
                print(f"{search_account.acc}Account")
                print("-"*20)

                print(f"Username.....{search_account.username}")
                print(f"Password.....{search_account.password}")

            else:
                print("That account does not exist")

        elif short_code == "del":
            print("Enter the key of the account you want to delete")
            search_key = input()

            if check_existing_accounts(search_key):
                search_account = find_account(search_key)
                delete_account(search_account)
                print("Account deleted")
            else:
                print("Account does not exist")

        elif short_code == "exit":
            print("Password Locker exiting ....")
            break

        else:
            print("I did not understand that.Please use short codes")


if __name__ == "__main__":
    main()
