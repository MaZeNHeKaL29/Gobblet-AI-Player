import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QComboBox, QTabWidget, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5 import uic
from gobblet import *
from board import *


class MyMainWindow(QMainWindow):
    def __init__(self):
        super(MyMainWindow, self).__init__()

        # Load the UI file
        uic.loadUi('app.ui', self)

        self.board = Board()

        self.label_1 = self.findChild(QLabel, "label_1")
        self.label_2 = self.findChild(QLabel, "label_2")
        self.label_3 = self.findChild(QLabel, "label_3")
        self.label_1.setText("Choose White Gobblet")

        self.b = []



        for i in range(1, 17):
            button_name = f"buttonboard_{i + 19}"
            button = self.findChild(QPushButton, button_name)
            self.b.append(button)
            self.b[i-1].clicked.connect(self.square_button_clicked)

        self.b = []

        for i in range(1, 17):
            button_name = f"buttonboard_{i + 49}"
            button = self.findChild(QPushButton, button_name)
            self.b.append(button)
            self.b[i-1].clicked.connect(self.square_button_clicked)

        self.b = []

        for i in range(1, 17):
            button_name = f"buttonboard_{i}"
            button = self.findChild(QPushButton, button_name)
            self.b.append(button)
            self.b[i-1].clicked.connect(self.square_button_clicked)

        
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

        self.display = self.findChild(QPushButton, "display_1")

        self.newGame_1 = self.findChild(QPushButton, "newGame_1")
        self.newGame_2 = self.findChild(QPushButton, "newGame_2")
        self.newGame_3 = self.findChild(QPushButton, "newGame_3")

        self.newGame = self.newGame_1

        self.newGame.clicked.connect(self.new_game)
        self.newGame_1.clicked.connect(self.new_game)
        self.newGame_2.clicked.connect(self.new_game)
        self.newGame_3.clicked.connect(self.new_game)

        self.display.hide()

        self.WG1 = Gobblet("WHITE",4)
        self.WG2 = Gobblet("WHITE",4)
        self.WG3 = Gobblet("WHITE",4)

        self.BG1 = Gobblet("BLACK",4)
        self.BG2 = Gobblet("BLACK",4)
        self.BG3 = Gobblet("BLACK",4)

        self.color = "WHITE"
        self.click = "CHOOSEGOBBLET"
        self.WHITEAI = False
        self.BLACKAI = False

        self.tabWidget = self.findChild(QTabWidget, "tabWidget")
        self.tabWidget.currentChanged.connect(self.on_tab_changed)


        self.label_1.setText("Player 1 : Choose White Gobblet")
        self.label_2.setText("")
        self.label_3.setText("")

        self.label = self.label_1

        self.size = (4+1)*10

        self.disable_buttons()
       
    def on_tab_changed(self, index):
        # Check if the specified tab is clicked (e.g., Tab 2 with index 1)
        if index == 0:
            self.label = self.label_1
            self.newGame = self.newGame_1
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

            self.disable_buttons()
            self.restart()
            self.WHITEAI = False
            self.BLACKAI = False
        elif index == 1:
            self.label = self.label_2
            self.newGame = self.newGame_2
            self.label_2.setText("Choose White Gobblet")
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

            self.disable_buttons()
            self.restart()
            self.WHITEAI = False
            self.BLACKAI = True
        elif index == 2:
            self.newGame = self.newGame_3
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

    def restart(self):
        self.click = "CHOOSEGOBBLET"
        for i in range(1, 17):
            self.b[i-1].setText("")
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
        self.color = "WHITE"
        self.click = "CHOOSEGOBBLET"
        self.BG1.setSize(4)
        self.BG2.setSize(4)
        self.BG3.setSize(4)
        self.WG1.setSize(4)
        self.WG2.setSize(4)
        self.WG3.setSize(4)
        self.label.setText("Player 1 : Choose White Gobblet")
        self.board.empty_board()
        self.disable_buttons()
        self.display.hide()
        self.size = (4+1)*10
        self.WG1 = Gobblet("WHITE",4)
        self.WG2 = Gobblet("WHITE",4)
        self.WG3 = Gobblet("WHITE",4)

        self.BG1 = Gobblet("BLACK",4)
        self.BG2 = Gobblet("BLACK",4)
        self.BG3 = Gobblet("BLACK",4)



    def enable_buttons(self):
        for i in range(1, 17):
            self.b[i-1].setEnabled(True)
        self.b_BG1.setEnabled(True)
        self.b_BG2.setEnabled(True)
        self.b_BG3.setEnabled(True)
        self.b_WG1.setEnabled(True)
        self.b_WG2.setEnabled(True)
        self.b_WG3.setEnabled(True)

    def disable_buttons(self):
        self.enable_buttons()
        if(self.color == "WHITE" or self.click == "CHOOSESQUARE"):
            self.b_BG1.setEnabled(False)
            self.b_BG2.setEnabled(False)
            self.b_BG3.setEnabled(False)

        if(self.color == "BLACK" or self.click == "CHOOSESQUARE"):
            self.b_WG1.setEnabled(False)
            self.b_WG2.setEnabled(False)
            self.b_WG3.setEnabled(False)

        if(self.click == "CHOOSEGOBBLET"):
            empty_squares = self.board.get_empty_squares()

            for square_number in empty_squares:
                # Access the corresponding button using self.b[square_number - 1]
                button = self.b[square_number - 1]

                # Now you can perform any operations on the button
                button.setEnabled(False)

        if(self.color == "WHITE" and self.click == "CHOOSEGOBBLET"):
            black_squares = self.board.get_squares_by_color("BLACK")

            for square_number in black_squares:
                # Access the corresponding button using self.b[square_number - 1]
                button = self.b[square_number - 1]

                # Now you can perform any operations on the button
                button.setEnabled(False)
        

        if(self.color == "BLACK" and self.click == "CHOOSEGOBBLET"):
            white_squares = self.board.get_squares_by_color("WHITE")

            for square_number in white_squares:
                # Access the corresponding button using self.b[square_number - 1]
                button = self.b[square_number - 1]

                # Now you can perform any operations on the button
                button.setEnabled(False)
        
        if(self.BG1.size == 0):
            self.b_BG1.setEnabled(False)

        if(self.BG2.size == 0):
            self.b_BG2.setEnabled(False)

        if(self.BG2.size == 0):
            self.b_BG2.setEnabled(False)
        
        if(self.WG1.size == 0):
            self.b_WG1.setEnabled(False)
        
        if(self.WG2.size == 0):
            self.b_WG2.setEnabled(False)

        if(self.WG3.size == 0):
            self.b_WG3.setEnabled(False)
        
        
        


    def square_button_clicked(self):
        if(self.click == "CHOOSESQUARE"):
            button_sender = self.sender()
            font = QFont("Segoe UI", self.size)
            font.setBold(True)
            button_sender.setFont(font)
            button_sender.setText("O")
            for i in range(1,17):
                if button_sender.objectName() == self.b[i - 1].objectName():
                    row = (i - 1) // 4
                    col = (i - 1) % 4
                    self.board.appendGobbletToSquare(row,col,Gobblet(self.color,(self.size-1)//10))
            if(self.color == "WHITE"):
                button_sender.setStyleSheet("background-color: rgb(170, 170, 127); color: white;")
                self.color = "BLACK"
                self.label.setText("Player 2 : Choose Black Gobblet")
            elif(self.color == "BLACK"):
                button_sender.setStyleSheet("background-color: rgb(170, 170, 127); color: black;")
                self.color = "WHITE"
                self.label.setText("Player 1 : Choose White Gobblet")
            self.display.hide()
            self.click = "CHOOSEGOBBLET"
            self.disable_buttons()
            self.check_winner()

        elif(self.click == "CHOOSEGOBBLET"):
            button_sender = self.sender()

            for i in range(1,17):
                print("Hi")
                if button_sender.objectName() == self.b[i - 1].objectName():
                    row = (i - 1) // 4
                    col = (i - 1) % 4
                    gobblet = self.board.get_gobblet(row,col)
                    print("hi2")
                    print(gobblet.size)
                    


            button = self.display

            self.size = gobblet.size*10 + 10

            large_squares = self.board.get_squares_by_size((self.size - 1) // 10)

            if(len(large_squares) >= 16):
                self.label.setText(self.label.Text() + " No Available Moves")
                return

            self.display.show() 
            font = QFont("Segoe UI", gobblet.size * 10 +10)
            font.setBold(True)
            button.setFont(font)
            button.setText("O")
            if(self.color == "WHITE"):
                button.setStyleSheet("background-color: rgb(170, 170, 127); color: white;")
                self.label.setText("Player 1 : Choose a Position for Gobblet")
            elif(self.color == "BLACK"):
                button.setStyleSheet("background-color: rgb(170, 170, 127); color: black;")
                self.label.setText("Player 2 : Choose a Position for Gobblet")

            self.board.removeLastGobbletFromSquare(row,col)
            gobblet = self.board.get_gobblet(row,col)
            if (gobblet is not None):
                font = QFont("Segoe UI", (gobblet.size) * 10 + 10)
                font.setBold(True)
                button_sender.setFont(font)
                if(gobblet.color == "WHITE"):
                    button_sender.setStyleSheet("background-color: rgb(170, 170, 127); color: white;")
                elif(gobblet.color == "BLACK"):
                    button_sender.setStyleSheet("background-color: rgb(170, 170, 127); color: black;")
            else:
                button_sender.setText("")

            self.click = "CHOOSESQUARE"

            self.disable_buttons()


            for square_number in large_squares:
                # Access the corresponding button using self.b[square_number - 1]
                button_f = self.b[square_number - 1]

                # Now you can perform any operations on the button
                button_f.setEnabled(False)



    def gobblet_button_clicked(self):
        button_sender = self.sender()
        if(button_sender.objectName() == "gobbletBlack_1"):
            if(self.BG1.size > 0):
                self.BG1.setSize(self.BG1.size - 1)
            if(self.BG1.size == 0):
                button_sender.setText("")
            font = QFont("Segoe UI", self.BG1.size * 10 + 10)
            font.setBold(True)
            size = (self.BG1.size+1)*10 + 10

        elif(button_sender.objectName() == "gobbletBlack_2"):
            if(self.BG2.size > 0):
                self.BG2.setSize(self.BG2.size - 1)
            if(self.BG2.size == 0):
                button_sender.setText("")
            font = QFont("Segoe UI", self.BG2.size * 10 + 10)
            font.setBold(True)
            size = (self.BG2.size+1)*10 + 10
            
        elif(button_sender.objectName() == "gobbletBlack_3"):
            if(self.BG3.size > 0):
                self.BG3.setSize(self.BG3.size - 1)
            if(self.BG3.size == 0):
                button_sender.setText("")
            font = QFont("Segoe UI", self.BG3.size * 10 + 10)
            font.setBold(True)
            size = (self.BG3.size+1)*10 + 10

        elif(button_sender.objectName() == "gobbletWhite_1"):
            if(self.WG1.size > 0):
                self.WG1.setSize(self.WG1.size - 1)
            if(self.WG1.size == 0):
                button_sender.setText("")
            font = QFont("Segoe UI", self.WG1.size * 10 + 10)
            font.setBold(True)
            size = (self.WG1.size+1)*10 + 10

        elif(button_sender.objectName() == "gobbletWhite_2"):
            if(self.WG2.size > 0):
                self.WG2.setSize(self.WG2.size - 1)
            if(self.WG2.size == 0):
                button_sender.setText("")
            font = QFont("Segoe UI", self.WG2.size * 10 + 10)
            font.setBold(True)
            size = (self.WG2.size+1)*10 + 10

        elif(button_sender.objectName() == "gobbletWhite_3"):
            if(self.WG3.size > 0):
                self.WG3.setSize(self.WG3.size - 1)
            if(self.WG3.size == 0):
                button_sender.setText("")
            font = QFont("Segoe UI", self.WG3.size * 10 + 10)
            font.setBold(True)
            size = (self.WG3.size+1)*10 + 10

        button_sender.setFont(font)

        button = self.display

        self.size = size


        large_squares = self.board.get_squares_by_size((size - 1) // 10)

        if(len(large_squares) >= 16):
            self.label.setText(self.label.Text() + " No Available Moves")
            return

        self.display.show()
        font = QFont("Segoe UI", size)
        font.setBold(True)
        button.setFont(font)
        button.setText("O")
        if(self.color == "WHITE"):
            button.setStyleSheet("background-color: rgb(170, 170, 127); color: white;")
            self.label.setText("Player 1 : Choose a Position for Gobblet")
        elif(self.color == "BLACK"):
            button.setStyleSheet("background-color: rgb(170, 170, 127); color: black;")
            self.label.setText("Player 2 : Choose a Position for Gobblet")

        self.click = "CHOOSESQUARE"

        self.disable_buttons()

        non_empty_squares = self.board.get_non_empty_squares()

        for square_number in non_empty_squares:
            # Access the corresponding button using self.b[square_number - 1]
            button = self.b[square_number - 1]

            # Now you can perform any operations on the button
            button.setEnabled(False)

        if(self.color == "WHITE"):
            three_in_row__squares = self.board.check_three_rows("BLACK", (size - 1) // 10)
        elif(self.color == "BLACK"):
            three_in_row__squares = self.board.check_three_rows("WHITE", (size - 1) // 10)

        for square_number in three_in_row__squares:
            # Access the corresponding button using self.b[square_number - 1]
            button = self.b[square_number - 1]

            # Now you can perform any operations on the button
            button.setEnabled(True)



    def disable_all_buttons(self):
        for i in range(1, 17):
            self.b[i-1].setEnabled(False)
        self.b_BG1.setEnabled(False)
        self.b_BG2.setEnabled(False)
        self.b_BG3.setEnabled(False)
        self.b_WG1.setEnabled(False)
        self.b_WG2.setEnabled(False)
        self.b_WG3.setEnabled(False)


    def check_winner(self):
        if(self.board.check_winner("WHITE")):
            self.label.setText("Game Over. White Wins")
            self.disable_all_buttons()

        elif(self.board.check_winner("BLACK")):
            self.label.setText("Game Over. Black Wins")
            self.disable_all_buttons()


    def new_game(self):
        self.restart()
        

    

    #def playAI(self):
        
        






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
