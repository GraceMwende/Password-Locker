class AccountCredentials:
    """class that generates store user account credentials"""

    account_list = []

    def __init__(self, username, password, account):
        """create account object details"""
        self.username = username
        self.password = password
        self.acc = account

    def save_account(self):
        """save accountdetails in the account_list"""
        AccountCredentials.account_list.append(self)

    def delete_account(self):
        """method that deletes a saved account from the list"""
        AccountCredentials.account_list.remove(self)
