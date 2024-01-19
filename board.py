from gobblet import *
from square import *


# A Class for Board in Game
class Board(object):
	def __init__(self):
		# Initialize a 4x4 matrix of Square objects to represent the game board
		self.matrix = [[Square() for _ in range(4)] for _ in range(4)]

		# Initialize Gobblets for the White player with different sizes
		self.WG1 = Gobblet("WHITE", 4)
		self.WG2 = Gobblet("WHITE", 4)
		self.WG3 = Gobblet("WHITE", 4)

		# Initialize Gobblets for the Black player with different sizes
		self.BG1 = Gobblet("BLACK", 4)
		self.BG2 = Gobblet("BLACK", 4)
		self.BG3 = Gobblet("BLACK", 4)



	# Method to append a Gobblet to a specific square on the game board
	def appendGobbletToSquare(self, row, col, gobblet):
		# Check if the row and column indices are within bounds (0 to 3)
		if 0 <= row < 4 and 0 <= col < 4:
			# Append the gobblet to the specified square in the board matrix
			self.matrix[row][col].appendGobblet(gobblet)
		else:
			# Print an error message for invalid row or column index
			print("Invalid row or column index.")


	# Method to remove the last added Gobblet from a specific square on the game board
	def removeLastGobbletFromSquare(self, row, col):
		# Check if the row and column indices are within bounds (0 to 3)
		if 0 <= row < 4 and 0 <= col < 4:
			# Remove and return the last added gobblet from the specified square
			return self.matrix[row][col].removeLastGobblet()
		else:
			# Print an error message for invalid row or column index
			print("Invalid row or column index.")


	# Method to check if a player with a specific color has achieved four in a row on the game board
	def check_winner(self, color):
		# Check for four in a row horizontally
		for row in range(4):
			col = 0
			# Check if the last Gobblet in each column of the current row has the specified color
			if all(self.matrix[row][col + i].getLastGobblet() is not None and self.matrix[row][col + i].getLastGobblet().color == color for i in range(4)):
				return True

		# Check for four in a row vertically
		for col in range(4):
			row = 0
			# Check if the last Gobblet in each row of the current column has the specified color
			if all(self.matrix[row + i][col].getLastGobblet() is not None and self.matrix[row + i][col].getLastGobblet().color == color for i in range(4)):
				return True

		# Check for four in a row diagonally (from top-left to bottom-right)
		row = 0
		col = 0
		# Check if the last Gobblet in each diagonal position has the specified color
		if all(self.matrix[row + i][col + i].getLastGobblet() is not None and self.matrix[row + i][col + i].getLastGobblet().color == color for i in range(4)):
			return True

		# Check for four in a row diagonally (from top-right to bottom-left)
		row = 0
		col = 3
		# Check if the last Gobblet in each diagonal position has the specified color
		if all(self.matrix[row + i][col - i].getLastGobblet() is not None and self.matrix[row + i][col - i].getLastGobblet().color == color for i in range(4)):
			return True

		# If no winner is found, return False
		return False



	# Method to get the list of squares that form a winning combination for a player with a specific color
	def get_winner(self, color):
		matching_squares = []

		# Check for four in a row horizontally
		for row in range(4):
			col = 0
			# Check if the last Gobblet in each column of the current row has the specified color
			if all(self.matrix[row][col + i].getLastGobblet() is not None and self.matrix[row][col + i].getLastGobblet().color == color for i in range(4)):
				for i in range(4):
					square = row * 4 + col + i + 1
					matching_squares.append(square)
				return matching_squares

		# Check for four in a row vertically
		for col in range(4):
			row = 0
			# Check if the last Gobblet in each row of the current column has the specified color
			if all(self.matrix[row + i][col].getLastGobblet() is not None and self.matrix[row + i][col].getLastGobblet().color == color for i in range(4)):
				for i in range(4):
					square = (row + i) * 4 + col + 1
					matching_squares.append(square)
				return matching_squares

		# Check for four in a row diagonally (from top-left to bottom-right)
		row = 0
		col = 0
		# Check if the last Gobblet in each diagonal position has the specified color
		if all(self.matrix[row + i][col + i].getLastGobblet() is not None and self.matrix[row + i][col + i].getLastGobblet().color == color for i in range(4)):
			for i in range(4):
				square = (row + i) * 4 + col + i + 1
				matching_squares.append(square)
			return matching_squares

		# Check for four in a row diagonally (from top-right to bottom-left)
		row = 0
		col = 3
		# Check if the last Gobblet in each diagonal position has the specified color
		if all(self.matrix[row + i][col - i].getLastGobblet() is not None and self.matrix[row + i][col - i].getLastGobblet().color == color for i in range(4)):
			for i in range(4):
				square = (row + i) * 4 + col - i + 1
				matching_squares.append(square)
			return matching_squares

		# If no winner is found, return an empty list
		return matching_squares





	# Method to get a list of square numbers representing empty squares on the game board
	def get_empty_squares(self):
		empty_squares = []

		# Iterate through each row and column of the game board
		for row in range(4):
			for col in range(4):
				# Check if the current square does not contain any Gobblets
				if not self.matrix[row][col].gobblets:
					# Calculate the square number (assuming square numbers start from 1)
					square_number = row * 4 + col + 1
					empty_squares.append(square_number)

		# Return the list of empty square numbers
		return empty_squares

	

	# Method to get a list of square numbers representing squares containing Gobblets of a specific color
	def get_squares_by_color(self, color):
		matching_squares = []

		# Iterate through each row and column of the game board
		for row in range(4):
			for col in range(4):
				square = self.matrix[row][col]

				# Check if the square is not empty and the last Gobblet has the specified color
				if square.gobblets and square.getLastGobblet().color == color:
					# Calculate the square number (assuming square numbers start from 1)
					square_number = row * 4 + col + 1  
					matching_squares.append(square_number)

		# Return the list of square numbers containing Gobblets of the specified color
		return matching_squares


	
	# Method to get a list of square numbers representing squares containing Gobblets of a certain size or larger
	def get_squares_by_size(self, size):
		matching_squares = []

		# Iterate through each row and column of the game board
		for row in range(4):
			for col in range(4):
				square = self.matrix[row][col]

				# Check if the square is not empty and the last Gobblet has the specified size or larger
				if square.gobblets and (square.getLastGobblet().size == size or square.getLastGobblet().size > size):
					# Calculate the square number (assuming square numbers start from 1)
					square_number = row * 4 + col + 1  
					matching_squares.append(square_number)

		# Return the list of square numbers containing Gobblets of the specified size or larger
		return matching_squares

	
	# Method to get a list of square numbers representing squares containing Gobblets smaller than a specified size
	def get_smaller_squares_by_size(self, size):
		matching_squares = []

		# Iterate through each row and column of the game board
		for row in range(4):
			for col in range(4):
				square = self.matrix[row][col]

				# Check if the square is not empty and the last Gobblet has a size smaller than the specified size
				if square.gobblets and (square.getLastGobblet().size < size):
					# Assuming square numbers start from 1
					square_number = row * 4 + col + 1  
					matching_squares.append(square_number)

		# Return the list of square numbers containing Gobblets smaller than the specified size
		return matching_squares



	
	# Method to get the Gobblet from a specified square on the game board
	def get_gobblet(self, row, col):
		if 0 <= row < 4 and 0 <= col < 4:
			# Return the last added gobblet from the specified square
			return self.matrix[row][col].getLastGobblet()


	# Method to empty the game board by creating a new 4x4 matrix of empty Square objects
	def empty_board(self):
		self.matrix = [[Square() for _ in range(4)] for _ in range(4)]



	# Method to check for squares with three consecutive Gobblets in a row, column, or diagonally
	def check_three_rows_consecutive(self, color, size):
		matching_squares = []

		# Check horizontally
		for row in range(4):
			for col in range(4 - 2):
				if all(self.matrix[row][col + i].getLastGobblet() is not None for i in range(3)):
					if all(self.matrix[row][col + i].getLastGobblet().color == color for i in range(3)):
						for i in range(3):
							if row < 4 and col + i < 4:
								if self.matrix[row][col + i].getLastGobblet() is not None:
									if self.matrix[row][col + i].getLastGobblet().size < size:
										r = row
										c = col + i
										square_number = r * 4 + c + 1
										matching_squares.append(square_number)

		# Check vertically
		for col in range(4):
			for row in range(4 - 2):
				if all(self.matrix[row + i][col].getLastGobblet() is not None for i in range(3)):
					if all(self.matrix[row + i][col].getLastGobblet().color == color for i in range(3)):
						for i in range(3):
							if row + i < 4 and col < 4:
								if self.matrix[row + i][col].getLastGobblet() is not None:
									if self.matrix[row + i][col].getLastGobblet().size < size:
										r = row + i
										c = col
										square_number = r * 4 + c + 1
										matching_squares.append(square_number)

		# Check diagonally (top-left to bottom-right)
		for row in range(4 - 2):
			for col in range(4 - 2):
				if all(self.matrix[row + i][col + i].getLastGobblet() is not None for i in range(3)):
					if all(self.matrix[row + i][col + i].getLastGobblet().color == color for i in range(3)):
						for i in range(3):
							if row + i < 4 and col + i < 4:
								if self.matrix[row + i][col + i].getLastGobblet() is not None:
									if self.matrix[row + i][col + i].getLastGobblet().size < size:
										r = row + i
										c = col + i
										square_number = r * 4 + c + 1
										matching_squares.append(square_number)

		# Check diagonally (top-right to bottom-left)
		for row in range(4 - 2):
			for col in range(3, 4):
				if all(self.matrix[row + i][col - i].getLastGobblet() is not None for i in range(3)):
					if all(self.matrix[row + i][col - i].getLastGobblet().color == color for i in range(3)):
						for i in range(3):
							if row + i < 4 and col - i < 4:
								if self.matrix[row + i][col - i].getLastGobblet() is not None:
									if self.matrix[row + i][col - i].getLastGobblet().size < size:
										r = row + i
										c = col - i
										square_number = r * 4 + c + 1
										matching_squares.append(square_number)

		return matching_squares


	# Method to check for squares with three Gobblets in a row, column, or diagonally
	def check_three_rows_all(self, color, size):
		matching_squares = []

		# Check horizontally
		for row in range(4):
			count = 0
			for col in range(4):
				if self.matrix[row][col].getLastGobblet() is None:
					count = count
				elif self.matrix[row][col].getLastGobblet().color == color:
					count = count + 1
				else:
					count = 0
					break
			if count == 3:
				for col in range(4):
					if self.matrix[row][col].getLastGobblet() is not None:
						if self.matrix[row][col].getLastGobblet().size < size:
							r = row
							c = col
							square_number = r * 4 + c + 1
							matching_squares.append(square_number)

		# Check vertically
		for col in range(4):
			count = 0
			for row in range(4):
				if self.matrix[row][col].getLastGobblet() is None:
					count = count
				elif self.matrix[row][col].getLastGobblet().color == color:
					count = count + 1
				else:
					count = 0
					break
			if count == 3:
				for row in range(4):
					if self.matrix[row][col].getLastGobblet() is not None:
						if self.matrix[row][col].getLastGobblet().size < size:
							r = row
							c = col
							square_number = r * 4 + c + 1
							matching_squares.append(square_number)


		# Check diagonally (top-left to bottom-right)
		count = 0
		for i in range(4):
			if self.matrix[i][i].getLastGobblet() is None:
				count = count
			elif self.matrix[i][i].getLastGobblet().color == color:
				count = count + 1
			else:
				count = 0
				break

		if count == 3:
			for i in range(4):
				if self.matrix[i][i].getLastGobblet() is not None:
					if self.matrix[i][i].getLastGobblet().size < size:
						r = i
						c = i
						square_number = r * 4 + c + 1
						matching_squares.append(square_number)


		
		# Check diagonally (top-left to bottom-right)
		count = 0
		for i in range(4):
			if self.matrix[i][3 - i].getLastGobblet() is None:
				count = count
			elif self.matrix[i][3 - i].getLastGobblet().color == color:
				count = count + 1
			else:
				count = 0
				break

		if count == 3:
			for i in range(4):
				if self.matrix[i][3 - i].getLastGobblet() is not None:
					if self.matrix[i][3 - i].getLastGobblet().size < size:
						r = i
						c = 3 - i
						square_number = r * 4 + c + 1
						matching_squares.append(square_number)

		return matching_squares

	


	# Method to count the number of rows (horizontal, vertical, and diagonal) with three Gobblets of the specified color
	def check_three_rows_count(self, color):
		no = 0

		# Check horizontally
		for row in range(4):
			count = 0
			for col in range(4):
				if self.matrix[row][col].getLastGobblet() is None:
					count = count
				elif self.matrix[row][col].getLastGobblet().color == color:
					count = count + 1
				else:
					count = 0
					break
			if count == 3:
				no += 1

		# Check vertically
		for col in range(4):
			count = 0
			for row in range(4):
				if self.matrix[row][col].getLastGobblet() is None:
					count = count
				elif self.matrix[row][col].getLastGobblet().color == color:
					count = count + 1
				else:
					count = 0
					break
			if count == 3:
				no += 1

		# Check diagonal from top-left to bottom-right
		count = 0
		for i in range(4):
			if self.matrix[i][i].getLastGobblet() is None:
				count = count
			elif self.matrix[i][i].getLastGobblet().color == color:
				count = count + 1
			else:
				count = 0
				break
		if count == 3:
			no += 1

		# Check diagonal from top-right to bottom-left
		count = 0
		for i in range(4):
			if self.matrix[i][3 - i].getLastGobblet() is None:
				count = count
			elif self.matrix[i][3 - i].getLastGobblet().color == color:
				count = count + 1
			else:
				count = 0
				break
		if count == 3:
			no += 1

		return no

	
	# Method to count the number of rows (horizontal, vertical, and diagonal) with two consecutive Gobblets of the specified color
	def check_two_consecutive_count(self, color):
		no = 0

		# Check horizontally for two consecutive Gobblets
		for row in range(4):
			for col in range(4 - 1):
				if all(self.matrix[row][col + i].getLastGobblet() and
					self.matrix[row][col + i].getLastGobblet().color == color for i in range(2)):
					no += 1

		# Check vertically for two consecutive Gobblets
		for col in range(4):
			for row in range(4 - 1):
				if all(self.matrix[row + i][col].getLastGobblet() and
					self.matrix[row + i][col].getLastGobblet().color == color for i in range(2)):
					no += 1

		# Check diagonally (top-left to bottom-right) for two consecutive Gobblets
		for row in range(4 - 1):
			for col in range(4 - 1):
				if all(self.matrix[row + i][col + i].getLastGobblet() and
					self.matrix[row + i][col + i].getLastGobblet().color == color for i in range(2)):
					no += 1

		# Check diagonally (top-right to bottom-left) for two consecutive Gobblets
		for row in range(4 - 1):
			for col in range(1, 4):
				if all(self.matrix[row + i][col - i].getLastGobblet() and
					self.matrix[row + i][col - i].getLastGobblet().color == color for i in range(2)):
					no += 1

		return no


	# Method to count the number of squares with exactly one Gobblet of the specified color
	def check_one_count(self, color):
		no = 0

		# Check horizontally for one Gobblet
		for row in range(4):
			for col in range(4):
				# Check if the square has exactly one Gobblet of the specified color
				if self.matrix[row][col].getLastGobblet() and self.matrix[row][col].getLastGobblet().color == color:
					no += 1

		return no

	# Method to count the total size of Gobblets on squares with exactly one Gobblet of the specified color
	def check_one_count_size(self, color):
		no = 0

		# Check horizontally for one Gobblet
		for row in range(4):
			for col in range(4):
				gobblet = self.matrix[row][col].getLastGobblet()
				# Check if the square has exactly one Gobblet of the specified color
				if gobblet and gobblet.color == color:
					no += gobblet.size

		return no

	# Method to get a list of square numbers that are non-empty
	def get_non_empty_squares(self):
		non_empty_squares = []
		for row in range(4):
			for col in range(4):
				# Check if the square is non-empty
				if self.matrix[row][col].gobblets:
					square_number = row * 4 + col + 1  # Assuming square numbers start from 1
					non_empty_squares.append(square_number)
		return non_empty_squares

	# Method to get a list of square numbers that are non-empty and contain Gobblets of the specified color
	def get_non_empty_squares_color(self, color):
		non_empty_squares = []
		for row in range(4):
			for col in range(4):
				# Check if the square is non-empty and contains Gobblets of the specified color
				if self.matrix[row][col].gobblets and self.matrix[row][col].getLastGobblet().color == color:
					square_number = row * 4 + col + 1  # Assuming square numbers start from 1
					non_empty_squares.append(square_number)
		return non_empty_squares

	
	


	# Method to get a list of valid square numbers for placing a new Gobblet or moving an existing Gobblet
	def get_valid_moves(self, new_gooblet, board, gobblet):
		valid_squares = []
		#v_squares = []

		# Get a list of empty squares on the board
		for square in board.get_empty_squares():
			valid_squares.append(square)

		
		#v_squares.append(board.get_empty_squares())

		# If it's a new Gobblet, check for potential winning moves based on the Gobblet's color
		if new_gooblet:
			if gobblet.color == "WHITE":
				# Check for potential winning moves for the BLACK color
				for square in board.check_three_rows_all("BLACK", gobblet.size):
					valid_squares.append(square)
				#v_squares.append(board.check_three_rows_all("BLACK", gobblet.size))
			elif gobblet.color == "BLACK":
				# Check for potential winning moves for the WHITE color
				for square in board.check_three_rows_all("WHITE", gobblet.size):
					valid_squares.append(square)
				#v_squares.append(board.check_three_rows_all("WHITE", gobblet.size))
		else:
			# For moving an existing Gobblet, consider squares with Gobblets smaller than the current one
			for square in board.get_smaller_squares_by_size(gobblet.size):
				valid_squares.append(square)
			#v_squares.append(board.get_smaller_squares_by_size(gobblet.size))

		# Uncomment the following line if you want to print the valid squares for debugging and previous v_squares
		# print("Valid Squares for", gobblet.color, v_squares)

		return valid_squares

	

# Method to get the row and column indices from a square number
def get_row_column(number):
    if number < 1:
        print(number)
        raise ValueError("Number should be greater than or equal to 1")

    # Calculate the row (assuming 0-based indexing)
    row = (number - 1) // 4
    # Calculate the column (assuming 0-based indexing)
    column = (number - 1) % 4

    return row, column


		