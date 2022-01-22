import unittest  # importing the unittest module
# importing the AccountCredentials class
from credentials import AccountCredentials


class TestAccount(unittest.TestCase):
    """Test class that defines test cases for the acoount details credentials saving"""

    def setUp(self):
        """setup method thats runs before each test case"""
        self.new_account = AccountCredentials(
            "Grace", "4225", "github1", "Github")

    def tearDown(self):
        """method thats cleanup after each test case has run"""
        AccountCredentials.account_list = []

    def test_init(self):
        """test case to check if the object is initialized properly"""

        self.assertEqual(self.new_account.username, "Grace")
        self.assertEqual(self.new_account.password, "4225")
        self.assertEqual(self.new_account.key, "github1")
        self.assertEqual(self.new_account.acc, "Github")

    def test_save_accountDetails(self):
        """check if credentials are saved into the accounts list"""
        self.new_account.save_account()  # saving the account details

        self.assertEqual(len(AccountCredentials.account_list), 1)

    def test_save_multiple_account(self):
        """method to check if we can save multiple accounts"""
        self.new_account.save_account()
        test_account = AccountCredentials(
            "Faith", "220220", "fb1", "facebook")
        test_account.save_account()

        self.assertEqual(len(AccountCredentials.account_list), 2)

    def test_delete_account(self):
        """test to check if an account is removed from the list"""
        self.new_account.save_account()
        test_account = AccountCredentials(
            "Faith", "220220", "fb1", "facebook")
        test_account.save_account()

        self.new_account.delete_account()  # deleting an account

        self.assertEqual(len(AccountCredentials.account_list), 1)

    def test_find_account_by_key(self):
        """checks if we can find account by key and display information"""
        self.new_account.save_account()
        test_account = AccountCredentials(
            "Faith", "220220", "fb1", "facebook")
        test_account.save_account()

        found_account = AccountCredentials.find_by_key("fb1")

        self.assertEqual(found_account.key, test_account.key)


if __name__ == "__main__":
    unittest.main()
