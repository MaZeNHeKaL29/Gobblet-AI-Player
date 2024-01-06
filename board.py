from gobblet import *
from square import *

class Board(object):
	def __init__(self):
		# Initialize a 4x4 matrix of Square objects
		self.matrix = [[Square() for _ in range(4)] for _ in range(4)]


	def appendGobbletToSquare(self, row, col, gobblet):
		# Check if the row and column indices are within bounds
		if (0 <= row < 4 and 0 <= col < 4):
			# Append the gobblet to the specified square
			self.matrix[row][col].appendGobblet(gobblet)
		else :
			print("Invalid row or column index.")

	def removeLastGobbletFromSquare(self, row, col):
		# Check if the row and column indices are within bounds
		if 0 <= row < 4 and 0 <= col < 4:
			# Remove the last added gobblet from the specified square
			return self.matrix[row][col].removeLastGobblet()
		else:
			print("Invalid row or column index.")


	def check_winner(self, color):
		# Check for four in a row horizontally
		for row in range(4):
			for col in range(4 - 3):  # We go up to the third column to check four in a row
				if all(self.matrix[row][col + i].getLastGobblet() is  not None for i in range(4)):
					if all(self.matrix[row][col + i].getLastGobblet().color == color for i in range(4)):
						return True

		# Check for four in a row vertically
		for col in range(4):
			for row in range(4 - 3):  # We go up to the third row to check four in a row
				if all(self.matrix[row + i][col].getLastGobblet() is  not None for i in range(4)):
					if all(self.matrix[row + i][col].getLastGobblet().color == color for i in range(4)):
						return True

		# Check for four in a row diagonally (from top-left to bottom-right)
		for row in range(4 - 3):
			for col in range(4 - 3):
				if all(self.matrix[row + i][col + i].getLastGobblet() is  not None for i in range(4)):
					if all(self.matrix[row + i][col + i].getLastGobblet().color == color for i in range(4)):
						return True

		# Check for four in a row diagonally (from top-right to bottom-left)
		for row in range(4 - 3):
			for col in range(3, 4):
				if all(self.matrix[row + i][col - i].getLastGobblet() is  not None for i in range(4)):
					if all(self.matrix[row + i][col - i].getLastGobblet().color == color for i in range(4)):
						return True

		# If no winner is found, return False
		return False
	    
	def get_empty_squares(self):
		empty_squares = []
		for row in range(4):
			for col in range(4):
				if not self.matrix[row][col].gobblets:
					square_number = row * 4 + col + 1  # Assuming square numbers start from 1
					empty_squares.append(square_number)
		return empty_squares
	

	def get_squares_by_color(self, color):
		matching_squares = []
		for row in range(4):
			for col in range(4):
				square = self.matrix[row][col]

				# Check if the square is not empty and the last gobblet has the specified color
				if square.gobblets and square.getLastGobblet().color == color:
					# Assuming square numbers start from 1
					square_number = row * 4 + col + 1  
					matching_squares.append(square_number)
		
		return matching_squares

	
	def get_squares_by_size(self,size):
		matching_squares = []
		for row in range(4):
			for col in range(4):
				square = self.matrix[row][col]

				# Check if the square is not empty and the last gobblet has the specified color
				if square.gobblets and (square.getLastGobblet().size == size or square.getLastGobblet().size > size):
					# Assuming square numbers start from 1
					square_number = row * 4 + col + 1  
					matching_squares.append(square_number)
		
		return matching_squares



	
	def get_gobblet(self, row, col):
		if 0 <= row < 4 and 0 <= col < 4:
			# Remove the last added gobblet from the specified square
			return self.matrix[row][col].getLastGobblet()
		


	def empty_board(self):
		self.matrix = [[Square() for _ in range(4)] for _ in range(4)]