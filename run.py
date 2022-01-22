#!/usr/bin/env python3.8
from credentials import AccountCredentials


def create_account(username, password, key, acc):
    new_account = AccountCredentials(username, password, key, acc)
    return new_account


def save_accounts(account):
    """function to save account"""
    account.save_account()


def delete_account(account):
    """function to delete account"""
    account.delete_account()


def find_account(acckey):
    """function that finds a key and returns the account"""

    return AccountCredentials.find_by_key(acckey)


def check_existing_accounts(acckey):
    """function that checks if acounr exists with that key and returns boolean"""

    return AccountCredentials.account_exist(acckey)


def display_accounts():
    """function that returns all saved accounts"""

    return AccountCredentials.display_accounts()

def delete_account(account):
  """function that deletes an account"""
  account.delete_account()
