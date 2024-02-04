'''This file contains the constructor and methods for Subscriber objects. These
objects contain the information about a streaming service's subscribers.
'''

# A class for creating Subscriber objects.
class Subscriber:

    # init method or constructor
    def __init__(self,name, userid, password):
        self._name =str(name)
        self._userid =str(userid)
        self._password = str(password)

    # getter method for name
    def get_name(self):
        return self._name

    # getter method for userid
    def get_userid(self):
        return self._userid

    # getter method for password
    def get_password(self):
        return self._password

    # setter method for name
    def set_name(self, name):
        self._name = name

    # setter method for userid
    def set_userid(self, userid):
        self._userid = userid

    # setter method for password
    def set_password(self, password):
        self._password = password

    # generates a string representation of a Subscriber
    def __repr__(self):
        return f'Subscriber(("{self._name}", "{self._userid}", "{self._password}")'
