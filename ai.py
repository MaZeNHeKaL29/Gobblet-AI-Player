from board import *
from square import *
from gobblet import *
import math

import copy



# AI Class
class AI(object):
    def __init__(self, color):
        #Constructor to initialize AI with a specified color (either "WHITE" or "BLACK")
        self.color = color

    #Method to evaluate the current state of the game board for the AI player.
    def evaluate(self, board, level, color, eval):


        # Determine the opponent's color based on the current player's color
        if self.color == "WHITE":
            color2 = "BLACK"
        elif self.color == "BLACK":
            color2 = "WHITE"

        # Initialize the evaluation score with the provided initial value
        evaluation_no = eval

        # Iterate through the rows and columns of the game board
        for row in range(4):
            for col in range(4):
                # Retrieve the last Gobblet in the current cell
                gobblet = board.matrix[row][col].getLastGobblet()
                # Check if the cell contains a Gobblet of the current player's color
                if board.matrix[row][col].getLastGobblet() and board.matrix[row][col].getLastGobblet().color == self.color:
                    # Update the evaluation score by adding twice the size of the Gobblet
                    evaluation_no += 2 * gobblet.size
                # Check if the cell contains a Gobblet of the opponent's color
                elif board.matrix[row][col].getLastGobblet() and board.matrix[row][col].getLastGobblet().color == color2:
                    # Update the evaluation score by subtracting twice the size of the Gobblet
                    evaluation_no -= 2 * gobblet.size

        # Check for three-in-a-row patterns and adjust the evaluation score accordingly
        if level > 1:
            evaluation_no += 2 * board.check_three_rows_count(self.color)

        # Check for three-in-a-row patterns of the opponent and adjust the evaluation score accordingly
        if level > 1:
            evaluation_no -= 2 * board.check_three_rows_count(color2)

       
        return evaluation_no
    



    

    
