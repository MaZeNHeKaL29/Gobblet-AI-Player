import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QTabWidget, QVBoxLayout, QWidget, QRadioButton
from PyQt5.QtGui import QFont
from PyQt5 import uic
from PyQt5 import QtTest
from PyQt5.QtCore import QThread, pyqtSignal
from gobblet import *
from board import *
from ai import *


from app import Ui_Form


# Class representing the main window of the application
class MyMainWindow(QMainWindow,Ui_Form):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        # Load the UI file
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # Initialize the game board
        self.board = Board()


        # Add Labels in GUI
        self.label_1 = self.findChild(QLabel, "label_1")
        self.label_2 = self.findChild(QLabel, "label_2")
        self.label_3 = self.findChild(QLabel, "label_3")
        self.label_1.setText("Player 1 : Choose White Gobblet")


        # Buttons for Squares in Board
        self.b = []


        # Initialize Buttons for Squares in Board in Tab 2
        for i in range(1, 17):
            button_name = f"buttonboard_{i + 19}"
            button = self.findChild(QPushButton, button_name)
            self.b.append(button)
            self.b[i-1].clicked.connect(self.square_button_clicked)

        # Buttons for Squares in Board
        self.b = []

        # Initialize Buttons for Squares in Board in Tab 3
        for i in range(1, 17):
            button_name = f"buttonboard_{i + 49}"
            button = self.findChild(QPushButton, button_name)
            self.b.append(button)
            self.b[i-1].clicked.connect(self.square_button_clicked)

        # Buttons for Squares in Board
        self.b = []

        # Initialize Buttons for Squares in Board in Tab 1
        for i in range(1, 17):
            button_name = f"buttonboard_{i}"
            button = self.findChild(QPushButton, button_name)
            self.b.append(button)
            self.b[i-1].clicked.connect(self.square_button_clicked)

        # Initialize Buttons for New Gobblets Stack(WHITE and BLACK) in Tab 2
        self.b_WG1 = self.findChild(QPushButton, "gobbletWhite_7")
        self.b_WG1.clicked.connect(self.gobblet_button_clicked)
        self.b_WG2 = self.findChild(QPushButton, "gobbletWhite_8")
        self.b_WG2.clicked.connect(self.gobblet_button_clicked)
        self.b_WG3 = self.findChild(QPushButton, "gobbletWhite_9")
        self.b_WG3.clicked.connect(self.gobblet_button_clicked)

        self.b_BG1 = self.findChild(QPushButton, "gobbletBlack_7")
        self.b_BG1.clicked.connect(self.gobblet_button_clicked)
        self.b_BG2 = self.findChild(QPushButton, "gobbletBlack_8")
        self.b_BG2.clicked.connect(self.gobblet_button_clicked)
        self.b_BG3 = self.findChild(QPushButton, "gobbletBlack_9")
        self.b_BG3.clicked.connect(self.gobblet_button_clicked)

        # Initialize Buttons for New Gobblets Stack(WHITE and BLACK) in Tab 3
        self.b_WG1 = self.findChild(QPushButton, "gobbletWhite_10")
        self.b_WG1.clicked.connect(self.gobblet_button_clicked)
        self.b_WG2 = self.findChild(QPushButton, "gobbletWhite_11")
        self.b_WG2.clicked.connect(self.gobblet_button_clicked)
        self.b_WG3 = self.findChild(QPushButton, "gobbletWhite_12")
        self.b_WG3.clicked.connect(self.gobblet_button_clicked)

        self.b_BG1 = self.findChild(QPushButton, "gobbletBlack_10")
        self.b_BG1.clicked.connect(self.gobblet_button_clicked)
        self.b_BG2 = self.findChild(QPushButton, "gobbletBlack_11")
        self.b_BG2.clicked.connect(self.gobblet_button_clicked)
        self.b_BG3 = self.findChild(QPushButton, "gobbletBlack_12")
        self.b_BG3.clicked.connect(self.gobblet_button_clicked)

        # Initialize Buttons for New Gobblets Stack(WHITE and BLACK) in Tab 1
        self.b_WG1 = self.findChild(QPushButton, "gobbletWhite_1")
        self.b_WG1.clicked.connect(self.gobblet_button_clicked)
        self.b_WG2 = self.findChild(QPushButton, "gobbletWhite_2")
        self.b_WG2.clicked.connect(self.gobblet_button_clicked)
        self.b_WG3 = self.findChild(QPushButton, "gobbletWhite_3")
        self.b_WG3.clicked.connect(self.gobblet_button_clicked)

        self.b_BG1 = self.findChild(QPushButton, "gobbletBlack_1")
        self.b_BG1.clicked.connect(self.gobblet_button_clicked)
        self.b_BG2 = self.findChild(QPushButton, "gobbletBlack_2")
        self.b_BG2.clicked.connect(self.gobblet_button_clicked)
        self.b_BG3 = self.findChild(QPushButton, "gobbletBlack_3")
        self.b_BG3.clicked.connect(self.gobblet_button_clicked)

        # Display to show Which Gobblet Player has Chosen
        self.display_1 = self.findChild(QPushButton, "display_1")
        self.display_2 = self.findChild(QPushButton, "display_2")

        self.display = self.display_1

        # Initialize Buttons for New Game
        self.newGame_1 = self.findChild(QPushButton, "newGame_1")
        self.newGame_2 = self.findChild(QPushButton, "newGame_2")
        self.newGame_3 = self.findChild(QPushButton, "newGame_3")

        self.newGame_1.clicked.connect(self.new_game)
        self.newGame_2.clicked.connect(self.new_game)
        self.newGame_3.clicked.connect(self.new_game)

        self.newGame = self.newGame_1

        self.newGame.clicked.connect(self.new_game)

        # Hide Display Buttons
        self.display.hide()

        # Initialize Gobblets Stack
        self.WG1 = Gobblet("WHITE",4)
        self.WG2 = Gobblet("WHITE",4)
        self.WG3 = Gobblet("WHITE",4)

        self.BG1 = Gobblet("BLACK",4)
        self.BG2 = Gobblet("BLACK",4)
        self.BG3 = Gobblet("BLACK",4)

        self.board.WG1 = self.WG1
        self.board.WG2 = self.WG2
        self.board.WG3 = self.WG3
        self.board.BG1 = self.BG1
        self.board.BG2 = self.BG2
        self.board.BG3 = self.BG3

        self.color = "WHITE"
        self.click = "CHOOSEGOBBLET"
        self.WHITEAI = False
        self.BLACKAI = False

        # Initialize Tabs
        self.tabWidget = self.findChild(QTabWidget, "tabWidget")

        self.tabWidget.setCurrentIndex(0)

        self.tabWidget.currentChanged.connect(self.on_tab_changed)


        # Initialize Combo Box for Choosing Difficulity
        self.comboBoxBlack_1 = self.findChild(QComboBox,"comboBoxdiff_1")
        self.comboBoxBlack_2 = self.findChild(QComboBox,"comboBoxdiff_2")
        self.comboBoxWhite_2 = self.findChild(QComboBox, "comboBoxdiff_3")
        self.comboBoxWhite_1 = self.findChild(QComboBox, "comboBoxdiff_4")
        self.comboBoxBlack = self.comboBoxBlack_1
        self.comboBoxWhite = self.comboBoxWhite_1

        # Initialize Draw Button
        self.draw_1 = self.findChild(QPushButton,"draw_1")
        self.draw_2 = self.findChild(QPushButton,"draw_2")
        self.draw_3 = self.findChild(QPushButton,"draw_3")

        self.draw_1.clicked.connect(self.draw_clicked)
        self.draw_2.clicked.connect(self.draw_clicked)
        self.draw_3.clicked.connect(self.draw_clicked)

        self.draw = self.draw_1

        self.draw_b = 0

        # Initialize Resume/Pause Button
        self.resume_pause = self.findChild(QPushButton, "resume_pause")
        self.resume_pause.clicked.connect(self.resumePause)

        self.resume_pause_b = 0

        # Initialize Radio Buttons for choosing Which Color Player want to play with
        self.playAsBlack = self.findChild(QRadioButton, "radioButton")
        self.playAsWhite = self.findChild(QRadioButton, "radioButton_2")

        self.playAsWhite.setChecked(True)
        self.comboBoxBlack.setEnabled(True)
        self.comboBoxWhite.setEnabled(False)

        self.playAsBlack.clicked.connect(self.changePlayer)
        self.playAsWhite.clicked.connect(self.changePlayer)


        self.label_1.setText("Player 1 : Choose White Gobblet")
        self.label_2.setText("")
        self.label_3.setText("")

        self.label = self.label_1

        self.size = (4+1)*10

        self.disable_buttons()
        self.restart()
        self.stop = False
        self.ai = AI(self.color)
        self.new_game_b = 0
        self.gameRunning = 0

        self.draw.setEnabled(False)
        self.resume_pause.setEnabled(False)

    # Method to handle tab changes in the application
    def on_tab_changed(self, index):
        # Check if the specified tab is clicked (e.g., Tab 2 with index 1)
        if index == 0:
            # Reset variables and UI components for Tab 1
            self.gameRunning = 0
            self.new_game_b = 0
            self.WHITEAI = False
            self.BLACKAI = False  
            self.label = self.label_1
            self.newGame = self.newGame_1
            self.draw = self.draw_1
            self.label_1.setText("Player 1 : Choose White Gobblet")
            self.b = []

            for i in range(1, 17):
                button_name = f"buttonboard_{i}"
                button = self.findChild(QPushButton, button_name)
                self.b.append(button)


            self.b_WG1 = self.findChild(QPushButton, "gobbletWhite_1")
            self.b_WG2 = self.findChild(QPushButton, "gobbletWhite_2")
            self.b_WG3 = self.findChild(QPushButton, "gobbletWhite_3")

            self.b_BG1 = self.findChild(QPushButton, "gobbletBlack_1")
            self.b_BG2 = self.findChild(QPushButton, "gobbletBlack_2")
            self.b_BG3 = self.findChild(QPushButton, "gobbletBlack_3")

            self.display = self.display_1
            self.disable_buttons()
            self.restart()
            self.WHITEAI = False
            self.BLACKAI = False
            self.show_buttons()
            self.draw.setEnabled(False)
            self.resume_pause.setEnabled(False)
        elif index == 1:
            # Reset variables and UI components for Tab 2
            self.gameRunning = 0
            self.new_game_b = 0
            self.WHITEAI = False
            self.BLACKAI = False
            self.label = self.label_2
            self.newGame = self.newGame_2
            self.draw = self.draw_2
            self.label_2.setText("Player 1 : Choose White Gobblet")
            self.b = []

            for i in range(1, 17):
                button_name = f"buttonboard_{i + 19}"
                button = self.findChild(QPushButton, button_name)
                self.b.append(button)

            
            self.b_WG1 = self.findChild(QPushButton, "gobbletWhite_7")
            self.b_WG2 = self.findChild(QPushButton, "gobbletWhite_8")
            self.b_WG3 = self.findChild(QPushButton, "gobbletWhite_9")

            self.b_BG1 = self.findChild(QPushButton, "gobbletBlack_7")
            self.b_BG2 = self.findChild(QPushButton, "gobbletBlack_8")
            self.b_BG3 = self.findChild(QPushButton, "gobbletBlack_9")


            self.comboBoxBlack = self.comboBoxBlack_1
            self.comboBoxWhite = self.comboBoxWhite_1
            self.display = self.display_2
            self.disable_buttons()
            self.restart()
            self.WHITEAI = False
            self.BLACKAI = True
            self.show_buttons()
            self.draw.setEnabled(False)
            self.resume_pause.setEnabled(False)
            self.changePlayer()
        elif index == 2:
            # Reset variables and UI components for Tab 3
            self.gameRunning = 0
            self.new_game_b = 0
            self.WHITEAI = False
            self.BLACKAI = False
            self.newGame = self.newGame_3
            self.draw = self.draw_3
            self.b = []

            for i in range(1, 17):
                button_name = f"buttonboard_{i + 49}"
                button = self.findChild(QPushButton, button_name)
                self.b.append(button)

            
            self.b_WG1 = self.findChild(QPushButton, "gobbletWhite_10")
            self.b_WG2 = self.findChild(QPushButton, "gobbletWhite_11")
            self.b_WG3 = self.findChild(QPushButton, "gobbletWhite_12")

            self.b_BG1 = self.findChild(QPushButton, "gobbletBlack_10")
            self.b_BG2 = self.findChild(QPushButton, "gobbletBlack_11")
            self.b_BG3 = self.findChild(QPushButton, "gobbletBlack_12")

            self.disable_buttons()
            self.restart()
            self.WHITEAI = True
            self.BLACKAI = True
            self.disable_all_buttons()
            self.label = self.label_3
            self.label.setText("")
            self.comboBoxBlack = self.comboBoxBlack_2
            self.comboBoxWhite = self.comboBoxWhite_2
            self.show_buttons()
            self.draw.setEnabled(False)
            self.resume_pause.setEnabled(False)

         # Pause for a short duration to ensure proper UI updates
        QtTest.QTest.qWait(100)

    # Method to restart the game
    def restart(self):
        # Set stop flag to True to pause ongoing processes
        self.stop = True
        # Set the initial click state to "CHOOSEGOBBLET"
        self.click = "CHOOSEGOBBLET"

        # Clear the text on the square buttons
        for i in range(1, 17):
            self.b[i-1].setText("")

        # Set font properties and display "O" on gobblet buttons
        font = QFont("Segoe UI", 50)
        font.setBold(True)
        self.b_BG1.setFont(font)
        self.b_BG1.setText("O")
        self.b_BG2.setFont(font)
        self.b_BG2.setText("O")
        self.b_BG3.setFont(font)
        self.b_BG3.setText("O")
        self.b_WG1.setFont(font)
        self.b_WG1.setText("O")
        self.b_WG2.setFont(font)
        self.b_WG2.setText("O")
        self.b_WG3.setFont(font)
        self.b_WG3.setText("O")

        # Reset player colors and sizes
        self.color = "WHITE"
        self.click = "CHOOSEGOBBLET"
        self.BG1.setSize(4)
        self.BG2.setSize(4)
        self.BG3.setSize(4)
        self.WG1.setSize(4)
        self.WG2.setSize(4)
        self.WG3.setSize(4)

        # Empty the game board
        self.board.empty_board()

        # Disable square buttons and hide the display button
        self.disable_buttons()
        self.display.hide()

        # Set the size variable
        self.size = (4 + 1) * 10

        # Create new gobblets for both players
        self.WG1 = Gobblet("WHITE", 4)
        self.WG2 = Gobblet("WHITE", 4)
        self.WG3 = Gobblet("WHITE", 4)

        self.BG1 = Gobblet("BLACK", 4)
        self.BG2 = Gobblet("BLACK", 4)
        self.BG3 = Gobblet("BLACK", 4)

        # Update the board with the new gobblets
        self.board.WG1 = self.WG1
        self.board.WG2 = self.WG2
        self.board.WG3 = self.WG3
        self.board.BG1 = self.BG1
        self.board.BG2 = self.BG2
        self.board.BG3 = self.BG3

        # Reset draw and resume/pause flags
        self.draw_b = 0
        self.resume_pause_b = 0

        # Show the square buttons
        self.show_buttons()

    def new_game(self):
        # Disable the "Draw" button and "Resume/Pause" button
        self.draw.setEnabled(False)
        self.resume_pause.setEnabled(False)

        # Reset flags for draw and resume/pause
        self.resume_pause_b = 0
        self.draw_b = 0

        # Display the game board
        self.show_buttons()

        # Restart the game board
        self.restart()

        # If the current tab is the second tab, switch players
        if self.tabWidget.currentIndex() == 1:
            self.changePlayer()

        # Check if both players are AI-controlled and the game is running
        if self.WHITEAI and self.BLACKAI and self.gameRunning:
            self.new_game_b = 1
            return
        # If both players are AI-controlled, start the game and disable player selection
        elif self.WHITEAI and self.BLACKAI:
            self.gameRunning = 1
            self.comboBoxBlack.setEnabled(False)
            self.comboBoxWhite.setEnabled(False)

        # If it's White player's turn and they are AI-controlled, make the AI move
        if self.color == "WHITE":
            if self.WHITEAI:
                self.label.setText("Player 1 Thinking....")
                self.playAI()
        # If it's Black player's turn and they are AI-controlled, make the AI move
        elif self.color == "BLACK":
            if self.BLACKAI:
                self.label.setText("Player 2 Thinking....")
                self.playAI()
