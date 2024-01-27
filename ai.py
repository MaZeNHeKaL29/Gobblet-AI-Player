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
    

    def minimax(self,depth,maximizingPlayer,color, board):
        if(depth == 0 or board.check_winner(color)):
            return self.evaluate(board,color),0,0
        

        if(color == "WHITE"):
            color2 = "BLACK"
        elif(color == "BLACK"):
            color2 = "WHITE"


        if (maximizingPlayer):
            maxEval = -math.inf
            if(color == "WHITE"):
                if(board.WG1.size != 0):
                    for square in board.get_valid_moves(True,board,board.WG1):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.WG1)
                        max = self.minimax(depth - 1, False, color2,new_board)[0]
                        if(max > maxEval):
                            maxEval = max
                            gobblet_move = 20
                            square_to_append = square

                if(board.WG2.size != 0):
                    for square in board.get_valid_moves(True,board,board.WG2):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.WG2)
                        max = self.minimax(depth - 1, False, color2,new_board)[0]
                        if(max > maxEval):
                            maxEval = max
                            gobblet_move = 21
                            square_to_append = square

                
                if(board.WG3.size != 0):
                    for square in board.get_valid_moves(True,board,board.WG3):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.WG3)
                        max = self.minimax(depth - 1, False, color2,new_board)[0]
                        if(max > maxEval):
                            maxEval = max
                            gobblet_move = 22
                            square_to_append = square

            elif(color == "BLACK"):

                if(board.BG1.size != 0):
                    for square in board.get_valid_moves(True,board,board.BG1):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.BG1)
                        max = self.minimax(depth - 1, False, color2,new_board)[0]
                        if(max > maxEval):
                            maxEval = max
                            gobblet_move = 30
                            square_to_append = square

                if(board.BG2.size != 0):
                    for square in board.get_valid_moves(True,board,board.BG2):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.BG2)
                        max = self.minimax(depth - 1, False, color2,new_board)[0]
                        if(max > maxEval):
                            maxEval = max
                            gobblet_move = 31
                            square_to_append = square

                
                if(board.BG3.size != 0):
                    for square in board.get_valid_moves(True,board,board.BG3):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.BG3)
                        max = self.minimax(depth - 1, False, color2,new_board)[0]
                        if(max > maxEval):
                            maxEval = max
                            gobblet_move = 32
                            square_to_append = square


            print("Color ", color)
            print(board.get_non_empty_squares_color(color))
            for square in board.get_non_empty_squares_color(color):
                row,col = get_row_column(square)
                gobblet = board.get_gobblet(row,col)
                if(gobblet is not None and gobblet.size != 0 and gobblet.color == color):
                    new_board = copy.deepcopy(board)
                    for square2 in board.get_valid_moves(False,board,gobblet):
                        new_board = copy.deepcopy(board)
                        row2, col2 = get_row_column(square)
                        new_board.appendGobbletToSquare(row2,col2,gobblet)
                        new_board.removeLastGobbletFromSquare(row,col)
                        max = self.minimax(depth - 1, False, color2,new_board)[0]
                        if(max > maxEval):
                            maxEval = max
                            gobblet_move = square
                            square_to_append = square2

            eval = maxEval

        
        else:
            minEval = math.inf
            if(color == "WHITE"):
                if(board.WG1.size != 0):
                    for square in board.get_valid_moves(True,board,board.WG1):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.WG1)
                        min = self.minimax(depth - 1, True, color2,new_board)[0]
                        if(min < minEval):
                            minEval = min
                            gobblet_move = 20
                            square_to_append = square

                if(board.WG2.size != 0):
                    for square in board.get_valid_moves(True,board,board.WG2):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.WG2)
                        min = self.minimax(depth - 1, True, color2,new_board)[0]
                        if(min < minEval):
                            minEval = min
                            gobblet_move = 21
                            square_to_append = square

                
                if(board.WG3.size != 0):
                    for square in board.get_valid_moves(True,board,board.WG3):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.WG3)
                        min = self.minimax(depth - 1, True, color2,new_board)[0]
                        if(min < minEval):
                            minEval = min
                            gobblet_move = 22
                            square_to_append = square

            elif(color == "BLACK"):

                if(board.BG1.size != 0):
                    for square in board.get_valid_moves(True,board,board.BG1):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.BG1)
                        min = self.minimax(depth - 1, True, color2,new_board)[0]
                        if(min < minEval):
                            minEval = min
                            gobblet_move = 30
                            square_to_append = square

                if(board.BG2.size != 0):
                    for square in board.get_valid_moves(True,board,board.BG2):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.BG2)
                        min = self.minimax(depth - 1, True, color2,new_board)[0]
                        if(min < minEval):
                            minEval = min
                            gobblet_move = 31
                            square_to_append = square

                
                if(board.BG3.size != 0):
                    for square in board.get_valid_moves(True,board,board.BG3):
                        new_board = copy.deepcopy(board)
                        row, col = get_row_column(square)
                        new_board.appendGobbletToSquare(row,col,board.BG3)
                        min= self.minimax(depth - 1, True, color2,new_board)[0]
                        if(min < minEval):
                            minEval = min
                            gobblet_move = 32
                            square_to_append = square

            print("Color ", color)
            print(board.get_non_empty_squares_color(color))
            for square in board.get_non_empty_squares_color(color):
                row,col = get_row_column(square)
                gobblet = board.get_gobblet(row,col)
                if(gobblet is not None and gobblet.size != 0 and gobblet.color == color):
                    new_board = copy.deepcopy(board)
                    for square2 in board.get_valid_moves(False,board,gobblet):
                        new_board = copy.deepcopy(board)
                        row2, col2 = get_row_column(square)
                        new_board.appendGobbletToSquare(row2,col2,gobblet)
                        new_board.removeLastGobbletFromSquare(row,col)
                        min = self.minimax(depth - 1, True, color2,new_board)[0]
                        if(min < minEval):
                            minEval = min
                            gobblet_move = square
                            square_to_append = square2

            eval = minEval

        print("Depth is ", depth)
        print("Color of Gobblet", color)
        print("Maximizing is ", maximizingPlayer)
        print("Eval is ", eval)
        print("Gobblet to move is ", gobblet_move)
        print("Square to Append",square_to_append)
        return eval, gobblet_move, square_to_append
    

    # Minimax algorithm with alpha-beta pruning
    def minimax_alpha_beta(self, level, depth, alpha, beta, maximizingPlayer, color, board):
        # Determine the opponent's color based on the current player's color
        if self.color == "WHITE":
            color2 = "BLACK"
        elif self.color == "BLACK":
            color2 = "WHITE"

        # Check if the current player has won, return the evaluation and placeholder moves
        if self.check_winner(board, self.color):
            return self.evaluate(board, level, color2, 2000), 0, 0

        # Check if the opponent has won, return the evaluation and placeholder moves
        if self.check_winner(board, color2):
            return self.evaluate(board, level, color2, -2000), 0, 0

        # Base case: if depth is 0, return the evaluation and placeholder moves
        if depth == 0:
            return self.evaluate(board, level, color2, 0), 0, 0

        # Update color2 based on the current player's color for recursive calls
        if color == "WHITE":
            color2 = "BLACK"
        elif color == "BLACK":
            color2 = "WHITE"

        gobblet_move = 0
        square_to_append = 0

        if maximizingPlayer:
            maxEval = -math.inf

            # Process moves for each Gobblet based on the current player's color
            if color == "WHITE":
                maxEval, gobblet_move, square_to_append = self.process_max_gobblet_alpha_beta(board, level, board.WG1, 20, color, depth, alpha, beta, maxEval, gobblet_move, square_to_append)
                if board.WG1.size != board.WG2.size:
                    maxEval, gobblet_move, square_to_append = self.process_max_gobblet_alpha_beta(board, level, board.WG2, 21, color, depth, alpha, beta, maxEval, gobblet_move, square_to_append)
                if board.WG2.size != board.WG3.size or board.WG1.size != board.WG3.size:
                    maxEval, gobblet_move, square_to_append = self.process_max_gobblet_alpha_beta(board, level, board.WG3, 22, color, depth, alpha, beta, maxEval, gobblet_move, square_to_append)

            elif color == "BLACK":
                maxEval, gobblet_move, square_to_append = self.process_max_gobblet_alpha_beta(board, level, board.BG1, 30, color, depth, alpha, beta, maxEval, gobblet_move, square_to_append)
                if board.BG1.size != board.BG2.size:
                    maxEval, gobblet_move, square_to_append = self.process_max_gobblet_alpha_beta(board, level, board.BG2, 31, color, depth, alpha, beta, maxEval, gobblet_move, square_to_append)
                if board.BG2.size != board.BG3.size:
                    maxEval, gobblet_move, square_to_append = self.process_max_gobblet_alpha_beta(board, level, board.BG3, 32, color, depth, alpha, beta, maxEval, gobblet_move, square_to_append)

            # Iterate through non-empty squares of the current player's color
            for square in board.get_non_empty_squares_color(color):
                row, col = get_row_column(square)
                gobblet = board.get_gobblet(row, col)

                # Check if the Gobblet is of the current player's color
                if gobblet is not None and gobblet.size != 0 and gobblet.color == color:
                    # Iterate through valid moves for the current Gobblet
                    for square2 in board.get_valid_moves(False, board, gobblet):
                        row2, col2 = get_row_column(square2)
                        board.appendGobbletToSquare(row2, col2, gobblet)
                        board.removeLastGobbletFromSquare(row, col)
                        # Recursively call minimax with the updated board
                        eval = self.minimax_alpha_beta(level, depth - 1, alpha, beta, False, color2, board)[0]
                        board.appendGobbletToSquare(row, col, gobblet)
                        board.removeLastGobbletFromSquare(row2, col2)
                        # Update maxEval, gobblet_move, and square_to_append based on the evaluation
                        if eval > maxEval:
                            maxEval = eval
                            gobblet_move = square
                            square_to_append = square2
                        if eval > alpha:
                            alpha = eval
                        if beta <= alpha:
                            break  # Beta cut-off

            eval = maxEval

        else:
            minEval = math.inf

            # Process moves for each Gobblet based on the current player's color
            if color == "WHITE":
                minEval, gobblet_move, square_to_append = self.process_min_gobblet_alpha_beta(board, level, board.WG1, 20, color, depth, alpha, beta, minEval, gobblet_move, square_to_append)
                if board.WG1.size != board.WG2.size:
                    minEval, gobblet_move, square_to_append = self.process_min_gobblet_alpha_beta(board, level, board.WG2, 21, color, depth, alpha, beta, minEval, gobblet_move, square_to_append)
                if board.WG2.size != board.WG3.size or board.WG1.size != board.WG3.size:
                    minEval, gobblet_move, square_to_append = self.process_min_gobblet_alpha_beta(board, level, board.WG3, 22, color, depth, alpha, beta, minEval, gobblet_move, square_to_append)

            elif color == "BLACK":
                minEval, gobblet_move, square_to_append = self.process_min_gobblet_alpha_beta(board, level, board.BG1, 30, color, depth, alpha, beta, minEval, gobblet_move, square_to_append)
                if board.BG1.size != board.BG2.size:
                    minEval, gobblet_move, square_to_append = self.process_min_gobblet_alpha_beta(board, level, board.BG2, 31, color, depth, alpha, beta, minEval, gobblet_move, square_to_append)
                if board.BG2.size != board.BG3.size or board.BG1.size != board.BG3.size:
                    minEval, gobblet_move, square_to_append = self.process_min_gobblet_alpha_beta(board, level, board.BG3, 32, color, depth, alpha, beta, minEval, gobblet_move, square_to_append)

            # Iterate through non-empty squares of the current player's color
            for square in board.get_non_empty_squares_color(color):
                row, col = get_row_column(square)
                gobblet = board.get_gobblet(row, col)

                # Check if the Gobblet is of the current player's color
                if gobblet is not None and gobblet.size != 0 and gobblet.color == color:
                    # Iterate through valid moves for the current Gobblet
                    for square2 in board.get_valid_moves(False, board, gobblet):
                        row2, col2 = get_row_column(square2)
                        board.appendGobbletToSquare(row2, col2, gobblet)
                        board.removeLastGobbletFromSquare(row, col)
                        # Recursively call minimax with the updated board
                        eval = self.minimax_alpha_beta(level, depth - 1, alpha, beta, True, color2, board)[0]
                        board.appendGobbletToSquare(row, col, gobblet)
                        board.removeLastGobbletFromSquare(row2, col2)
                        # Update minEval, gobblet_move, and square_to_append based on the evaluation
                        if eval < minEval:
                            minEval = eval
                            gobblet_move = square
                            square_to_append = square2
                        if eval < beta:
                            beta = eval
                        if beta <= alpha:
                            break  # Alpha cut-off

            eval = minEval

        # Uncomment the following lines for debugging purposes
        # print("")
        # print("Depth is", depth)
        # print("Color", color)
        # print("Eval is ", eval)
        # print("Gobblet to move is ", gobblet_move)
        # print("Square to Append", square_to_append)

        return eval, gobblet_move, square_to_append

    


    # Process moves for minimizing player with alpha-beta pruning
    def process_min_gobblet_alpha_beta(self, board, level, player, move_id, color, depth, alpha, beta, minEval, gobblet_move, square_to_append):
        # Check if the player has any Gobblets left
        if player.size != 0:
            # Create a new Gobblet to add to the board
            gobblet_add = Gobblet(color, 4)

            # Determine the opponent's color
            if color == "WHITE":
                color2 = "BLACK"
            elif color == "BLACK":
                color2 = "WHITE"

            # Iterate through valid moves for the current player's Gobblet
            for square in board.get_valid_moves(True, board, player):
                row, col = get_row_column(square)

                # Set the size of the new Gobblet to match the size of the current player's Gobblet
                gobblet_add.setSize(player.size)
                # Add the Gobblet to the square on the board
                board.appendGobbletToSquare(row, col, gobblet_add)
                # Decrease the size of the player's Gobblet
                player.setSize(player.size - 1)

                # Recursively call minimax with the updated board for the maximizing player
                min_val = self.minimax_alpha_beta(level, depth - 1, alpha, beta, True, color2, board)[0]

                # Undo the move by removing the Gobblet from the square and restoring the size of the player's Gobblet
                board.removeLastGobbletFromSquare(row, col)
                player.setSize(player.size + 1)

                # Update minEval, gobblet_move, and square_to_append based on the evaluation
                if min_val < minEval:
                    minEval = min_val
                    gobblet_move = move_id
                    square_to_append = square

                # Alpha-beta pruning: Update beta
                beta = min(beta, minEval)

                # If beta is less than or equal to alpha, prune the rest of the branches
                if alpha >= beta:
                    break

        return minEval, gobblet_move, square_to_append

    


    # Process moves for maximizing player with alpha-beta pruning
    def process_max_gobblet_alpha_beta(self, board, level, player, move_id, color, depth, alpha, beta, maxEval, gobblet_move, square_to_append):
        # Check if the player has any Gobblets left
        if player.size != 0:
            # Create a new Gobblet to add to the board
            gobblet_add = Gobblet(color, 4)

            # Determine the opponent's color
            if color == "WHITE":
                color2 = "BLACK"
            elif color == "BLACK":
                color2 = "WHITE"

            # Iterate through valid moves for the current player's Gobblet
            for square in board.get_valid_moves(True, board, player):
                row, col = get_row_column(square)

                # Set the size of the new Gobblet to match the size of the current player's Gobblet
                gobblet_add.setSize(player.size)
                # Add the Gobblet to the square on the board
                board.appendGobbletToSquare(row, col, gobblet_add)
                # Decrease the size of the player's Gobblet
                player.setSize(player.size - 1)

                # Recursively call minimax with the updated board for the minimizing player
                max_val = self.minimax_alpha_beta(level, depth - 1, alpha, beta, False, color2, board)[0]

                # Undo the move by removing the Gobblet from the square and restoring the size of the player's Gobblet
                board.removeLastGobbletFromSquare(row, col)
                player.setSize(player.size + 1)

                # Update maxEval, gobblet_move, and square_to_append based on the evaluation
                if max_val > maxEval:
                    maxEval = max_val
                    gobblet_move = move_id
                    square_to_append = square

                # Alpha-beta pruning: Update alpha
                alpha = max(alpha, maxEval)

                # If alpha is greater than or equal to beta, prune the rest of the branches
                if alpha >= beta:
                    break

        return maxEval, gobblet_move, square_to_append




    # Check if the specified color has won the game on the given board
    def check_winner(self, board, color):
        # Check for four in a row horizontally
        for row in range(4):
            col = 0
            # Check if all Gobblets in the row have the specified color
            if all(board.matrix[row][col + i].getLastGobblet() is not None and board.matrix[row][col + i].getLastGobblet().color == color for i in range(4)):
                return True

        # Check for four in a row vertically
        for col in range(4):
            row = 0
            # Check if all Gobblets in the column have the specified color
            if all(board.matrix[row + i][col].getLastGobblet() is not None and board.matrix[row + i][col].getLastGobblet().color == color for i in range(4)):
                return True

        # Check for four in a row diagonally (from top-left to bottom-right)
        row = 0
        col = 0
        # Check if all Gobblets in the diagonal have the specified color
        if all(board.matrix[row + i][col + i].getLastGobblet() is not None and board.matrix[row + i][col + i].getLastGobblet().color == color for i in range(4)):
            return True

        # Check for four in a row diagonally (from top-right to bottom-left)
        row = 0
        col = 3
        # Check if all Gobblets in the diagonal have the specified color
        if all(board.matrix[row + i][col - i].getLastGobblet() is not None and board.matrix[row + i][col - i].getLastGobblet().color == color for i in range(4)):
            return True

        # If no winner is found, return False
        return False



    

    
