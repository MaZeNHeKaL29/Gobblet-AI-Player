from gobblet import *

# A Class for Each Square in Board
class Square(object):
    def __init__(self):
        # Constructor to initialize a Square object with an empty list to store Gobblets
        self.gobblets = []

    def appendGobblet(self, gobblet):
        # Method to add a Gobblet to the list of Gobblets in the Square
        self.gobblets.append(gobblet)

    def removeLastGobblet(self):
        # Method to remove and return the last added Gobblet from the list
        if self.gobblets:
            return self.gobblets.pop()

    def getLastGobblet(self):
        # Method to retrieve the last added Gobblet without removing it
        if self.gobblets:
            return self.gobblets[-1]
