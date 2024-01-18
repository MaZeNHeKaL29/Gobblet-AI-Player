
# A class for Gobblet
class Gobblet(object):
    def __init__(self, color, size):
        # Constructor to initialize the Gobblet with a specified color and size
        self.color = color
        self.size = size

    def setSize(self, size):
        # Method to set the size of the Gobblet with certain conditions
        if size > 4:
            # If size is greater than 4, set it to the maximum allowed size (4)
            self.size = 4
        elif size < 0:
            # If size is less than 0, set it to the minimum allowed size (0)
            self.size = 0
        else:
            # Otherwise, set the size to the specified value
            self.size = size

    def getColor(self):
        # Method to retrieve the color of the Gobblet
        return self.color

    def getSize(self):
        # Method to retrieve the size of the Gobblet
        return self.size
