from gobblet import *

class Square(object):
    def __init__(self):
        self.gobblets = []

    def appendGobblet(self, gobblet):
        self.gobblets.append(gobblet)

    def removeLastGobblet(self):
        if self.gobblets:
            return self.gobblets.pop()
        else:
            print("No gobblets to remove.")

    def getLastGobblet(self):
        if self.gobblets:
            return self.gobblets[-1]
        else:
            print("No gobblets in the square.")