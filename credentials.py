class AccountCredentials:
    """class that generates store user account credentials"""

    account_list = []

    def __init__(self, username, password, phone_number, account):
        """create account object details"""
        self.username = username
        self.password = password
        self.phone = phone_number
        self.acc = account

    def save_account(self):
        """save accountdetails in the account_list"""
        AccountCredentials.account_list.append(self)
