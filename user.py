import random
import string


class User:
    "Class that generates new instances of user"

    user_list = []

    def __init__(self, password):
        """define properties for our object"""
        # self.username = username
        self.password = password

    def save_password(self):
        User.user_list.append(self)


# # get random string of letters and digits
# source = string.ascii_letters + string.digits
# result_str = ''.join((random.choice(source) for i in range(4)))
# print(result_str)
