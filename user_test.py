import unittest
from user import User



class TestUser(unittest.TestCase):
    def setUp(self):
        # create password
        self.new_pass = User("1277")

    def test_init(self):
        self.assertEqual(self.new_pass.password, "1277")

    def test_save_password(self):
        self.new_pass.save_password()
        self.assertEqual(len(User.user_list), 1)


if __name__ == "__main__":
    unittest.main()
