class AccountCredentials:
    """class that generates store user account credentials"""

    account_list = []

    def __init__(self, username, password, key, account):
        """create account object details"""
        self.username = username
        self.password = password
        self.key = key
        self.acc = account

    def save_account(self):
        """save accountdetails in the account_list"""
        AccountCredentials.account_list.append(self)

    def delete_account(self):
        """method that deletes a saved account from the list"""
        AccountCredentials.account_list.remove(self)

    @classmethod
    def find_by_key(cls, acckey):
        """"
        takes key and returns an account that matches that key

        Args:
          key: key to search for
        Returns:
          Account that matches the key
        """

        for account in cls.account_list:
            if account.key == acckey:
                return account

    @classmethod
    def account_exist(cls, acckey):
        """
        check if account exists from the account list
        Args:
          key:key to search if it exists
        Returns:
          Boolean:True or false if the contact exists
        """

        for account in cls.account_list:
            if account.key == acckey:
                return True
