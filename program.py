# First Name : Fehmi
# Last Name : Karaalioglu
# Student Number : 251255449

'''
 This file contains the constructor and methods for Program objects. These
objects contain the information about a streaming service's shows and movies.
'''

# A class for creating Program objects.
class Program:

    # init method or constructor
    def __init__(self,title,genre,creator,release_date):
        self._title =str(title)
        self._genre =str(genre)
        self._creator = str(creator)
        self._release_date=str(release_date)

    # getter method for title
    def get_title(self):
        return self._title

    # getter method for genre
    def get_genre(self):
        return self._genre

    # getter method for creator
    def get_creator(self):
        return self._creator

    # getter method for release_date
    def get_release_date(self):
        return self._release_date

    # setter method for title
    def set_title(self, title):
        self._title = title

    # setter method for genre
    def set_genre(self, genre):
        self._genre = genre

    # setter method for creator
    def set_creator(self, creator):
        self._creator = creator

    # setter method for release_date
    def set_release_date(self, release_date):
        self._release_date = release_date

    # generates a string representation of a Program
    def __repr__(self):
        return f'Program("{self._title}", "{self._genre}", "{self._creator}, "{self._release_date}")'
