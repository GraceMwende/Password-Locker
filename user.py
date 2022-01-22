class User:
    "Class that generates new instances of user"

    user_list = []

    def __init__(self, username, password, phone_number):
        """define propertie for our object"""
        self.username = username
        self.password = password
        self.phone = phone_number
