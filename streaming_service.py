'''This file contains the constructor and methods for StreamingService objects.
These objects contain the name of the streaming service, the programs it offers, and its
subscriber information.'''

# sort function for program title
def sort_program(e):
    return e.get_title()

#sort function for subscriber name
def sort_subscriber(e):
    return e.get_name()

# A class for creating StreamingService objects.
class StreamingService:

    # init method or constructor
    def __init__(self,name="", program_list=[], subscriber_list=[]):
        self._name = name
        self._programs = program_list
        self._subscribers = subscriber_list

    # getter method for name(string)
    def get_name(self):
        return self._name

    # getter method for programs(list of Program)
    def get_programs(self):
        return self._programs

    # getter method for subscribers(list of Subscribes)
    def get_subscribers(self):
        return self._subscribers

    # getter method for program title
    def get_program(self,title):
        for prog_title in self._programs:
            if title ==  prog_title.get_title():
                return prog_title
        return None

    # getter method for subscriber name
    def get_subscriber(self,name):
        for subc_name in self._subscribers:
            if name ==  subc_name.get_name():
                return subc_name
        return None

    # setter method for name
    def set_name(self, name):
        self._name = name

    # A method adds the given Program object to the service's list of programs
    def add_program(self, program):
        self._programs.append(program)

    # A method adds the given Subscriber to the service's list of subscribers
    def add_subscriber(self,subscriber):
        self._subscribers.append(subscriber)

    # A method given a program's title, removes the Program with that title from the service's list of programs
    def remove_program(self,title):
        for prog_title in self._programs:
            if title == prog_title.get_title():
                self._programs.remove(prog_title)

    # A method given a subscriber's name, removes the Subscriber with that name from the service's list of subscribers
    def remove_subscriber(self,name):
        for subc_name in self._subscribers:
            if name == subc_name.get_name():
                self._subscribers.remove(subc_name)

    # A method given a Program object's information, updates that Program object in the service's list of programs
    def update_program(self, title, genre, creator, date):
        for update_prog in self._programs:
            if title == update_prog.get_title():
                self._title = genre
                self._title = creator
                self._title = date

    # A method given a Subscriber object's information, updates that Subscriber object in the service's list of
    # subscribers
    def update_subscriber(self, name, userid, password):
        for subc_name in self._subscribers:
            if name ==subc_name.get_name():
                self._name= userid
                self._name = password

    # A method sorts the service's program list by title and the service's subscriber list by name;
    def sort(self):
        self._programs = sorted(self._programs, key=sort_program)
        self._subscribers = sorted(self._subscribers, key=sort_subscriber)

    # generates a string representation of a StreamingService
    def __repr__(self):
        return f'Streaming Service("{self._name}", {self._programs}, {self._subscribers})'
