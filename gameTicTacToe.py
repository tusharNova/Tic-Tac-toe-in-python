import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon
from gameUI import Ui_MainWindow


class clsGame(QMainWindow):
    def __init__(self):
        super(clsGame, self).__init__()
        self.winner = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.clicked = True
        self.count = 0

        self.setWindowIcon(QIcon("icon/python.png"))

        self.btn1 = self.ui.b1
        self.btn2 = self.ui.b2
        self.btn3 = self.ui.b3
        self.btn4 = self.ui.b4
        self.btn5 = self.ui.b5
        self.btn6 = self.ui.b6
        self.btn7 = self.ui.b7
        self.btn8 = self.ui.b8
        self.btn9 = self.ui.b9
        self.btn1.clicked.connect(lambda: self.btn_Clicked(self.ui.b1))
        self.btn2.clicked.connect(lambda: self.btn_Clicked(self.ui.b2))
        self.btn3.clicked.connect(lambda: self.btn_Clicked(self.ui.b3))
        self.btn4.clicked.connect(lambda: self.btn_Clicked(self.ui.b4))
        self.btn5.clicked.connect(lambda: self.btn_Clicked(self.ui.b5))
        self.btn6.clicked.connect(lambda: self.btn_Clicked(self.ui.b6))
        self.btn7.clicked.connect(lambda: self.btn_Clicked(self.ui.b7))
        self.btn8.clicked.connect(lambda: self.btn_Clicked(self.ui.b8))
        self.btn9.clicked.connect(lambda: self.btn_Clicked(self.ui.b9))
        self.btn1.setStyleSheet("background:white")
        self.btn2.setStyleSheet("background:white")
        self.btn3.setStyleSheet("background:white")
        self.btn4.setStyleSheet("background:white")
        self.btn5.setStyleSheet("background:white")
        self.btn6.setStyleSheet("background:white")
        self.btn7.setStyleSheet("background:white")
        self.btn8.setStyleSheet("background:white")
        self.btn9.setStyleSheet("background:white")
        self.ui.actionExit.triggered.connect(self.close)
        self.ui.actionRestart.triggered.connect(self.restart)

    def restart(self):
        self.btn1.setDisabled(0)
        self.btn2.setDisabled(0)
        self.btn3.setDisabled(0)
        self.btn4.setDisabled(0)
        self.btn5.setDisabled(0)
        self.btn6.setDisabled(0)
        self.btn7.setDisabled(0)
        self.btn8.setDisabled(0)
        self.btn9.setDisabled(0)
        self.btn1.setText("")
        self.btn2.setText("")
        self.btn3.setText("")
        self.btn4.setText("")
        self.btn5.setText("")
        self.btn6.setText("")
        self.btn7.setText("")
        self.btn8.setText("")
        self.btn9.setText("")
        self.btn1.setStyleSheet("background:white")
        self.btn2.setStyleSheet("background:white")
        self.btn3.setStyleSheet("background:white")
        self.btn4.setStyleSheet("background:white")
        self.btn5.setStyleSheet("background:white")
        self.btn6.setStyleSheet("background:white")
        self.btn7.setStyleSheet("background:white")
        self.btn8.setStyleSheet("background:white")
        self.btn9.setStyleSheet("background:white")

        self.winner = False
        self.winner = None
        self.clicked = True
        self.count = 0

    def disableBtn(self):
        self.btn1.setDisabled(1)
        self.btn2.setDisabled(1)
        self.btn3.setDisabled(1)
        self.btn4.setDisabled(1)
        self.btn5.setDisabled(1)
        self.btn6.setDisabled(1)
        self.btn7.setDisabled(1)
        self.btn8.setDisabled(1)
        self.btn9.setDisabled(1)

    def checkIfWon(self):
        self.winner = False
        if self.btn1.text() == "X" and self.btn2.text() == "X" and self.btn3.text() == "X":
            self.btn1.setStyleSheet("background:red")
            self.btn2.setStyleSheet("background:red")
            self.btn3.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("X is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn4.text() == "X" and self.btn5.text() == "X" and self.btn6.text() == "X":
            self.btn4.setStyleSheet("background:red")
            self.btn5.setStyleSheet("background:red")
            self.btn6.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("X is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn7.text() == "X" and self.btn8.text() == "X" and self.btn9.text() == "X":
            self.btn7.setStyleSheet("background:red")
            self.btn8.setStyleSheet("background:red")
            self.btn9.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("X is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn1.text() == "X" and self.btn4.text() == "X" and self.btn7.text() == "X":
            self.btn1.setStyleSheet("background:red")
            self.btn4.setStyleSheet("background:red")
            self.btn7.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("X is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn2.text() == "X" and self.btn5.text() == "X" and self.btn8.text() == "X":
            self.btn2.setStyleSheet("background:red")
            self.btn5.setStyleSheet("background:red")
            self.btn8.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("X is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn3.text() == "X" and self.btn6.text() == "X" and self.btn9.text() == "X":
            self.btn3.setStyleSheet("background:red")
            self.btn6.setStyleSheet("background:red")
            self.btn9.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("X is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn1.text() == "X" and self.btn5.text() == "X" and self.btn9.text() == "X":
            self.btn1.setStyleSheet("background:red")
            self.btn5.setStyleSheet("background:red")
            self.btn9.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("X is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn3.text() == "X" and self.btn5.text() == "X" and self.btn7.text() == "X":
            self.btn3.setStyleSheet("background:red")
            self.btn5.setStyleSheet("background:red")
            self.btn7.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("X is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn1.text() == "O" and self.btn2.text() == "O" and self.btn3.text() == "O":
            self.btn1.setStyleSheet("background:red")
            self.btn2.setStyleSheet("background:red")
            self.btn3.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("O is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn4.text() == "O" and self.btn5.text() == "O" and self.btn6.text() == "O":
            self.btn4.setStyleSheet("background:red")
            self.btn5.setStyleSheet("background:red")
            self.btn6.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("O is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn7.text() == "O" and self.btn8.text() == "O" and self.btn9.text() == "O":
            self.btn7.setStyleSheet("background:red")
            self.btn8.setStyleSheet("background:red")
            self.btn9.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("O is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn1.text() == "O" and self.btn4.text() == "O" and self.btn7.text() == "O":
            self.btn1.setStyleSheet("background:red")
            self.btn4.setStyleSheet("background:red")
            self.btn7.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("O is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn2.text() == "O" and self.btn5.text() == "O" and self.btn8.text() == "O":
            self.btn2.setStyleSheet("background:red")
            self.btn5.setStyleSheet("background:red")
            self.btn8.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("O is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn3.text() == "O" and self.btn6.text() == "O" and self.btn9.text() == "O":
            self.btn3.setStyleSheet("background:red")
            self.btn6.setStyleSheet("background:red")
            self.btn9.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("O is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn1.text() == "O" and self.btn5.text() == "O" and self.btn9.text() == "O":
            self.btn1.setStyleSheet("background:red")
            self.btn5.setStyleSheet("background:red")
            self.btn9.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("O is Winner !")
            msg.exec_()
            self.disableBtn()

        elif self.btn3.text() == "O" and self.btn5.text() == "O" and self.btn7.text() == "O":
            self.btn3.setStyleSheet("background:red")
            self.btn5.setStyleSheet("background:red")
            self.btn7.setStyleSheet("background:red")
            self.winner = True
            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setText("O is Winner !")
            msg.exec_()
            self.disableBtn()
        if self.count == 9 and self.winner == False:
            msg = QMessageBox(self)
            msg.setWindowTitle("Tic Tac Toe")
            msg.setText("It's A Tie !")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            self.restart()

    def btn_Clicked(self, b):
        if b.text() == "" and self.clicked == True:
            b.setText("X")
            self.clicked = False
            self.count += 1
            self.checkIfWon()
        elif b.text() == "" and self.clicked == False:
            b.setText("O")
            self.clicked = True
            self.count += 1
            self.checkIfWon()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Tic Tac Toe")
            msg.setText("Select Other On")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Close)
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()


