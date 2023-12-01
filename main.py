import sys
import time

from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, qDrawWinButton, QPushButton
from PyQt5.QtGui import QIcon
from load import Ui_MainWindow
from gameTicTacToe  import clsGame
TIME_LIMIT = 100
class External(QThread):
    countChanged = pyqtSignal(int)
    def run(self):
        count = 0
        while count < TIME_LIMIT:
            count += 1
            time.sleep(0.05)
            self.countChanged.emit(count)
class clsload(QMainWindow):
    def __init__(self):
        super(clsload, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)
        self.setStyleSheet("background-image: url(img1.png); background-repeat: no-repeat; background-position: center")
        self.updateProgressBar()
        self.setWindowIcon(QIcon("icon/python.png"))
        self.g = clsGame()

    def updateProgressBar(self):
        self.calc = External()
        self.calc.countChanged.connect(self.onCountChanged)
        self.calc.start()

    def onCountChanged(self, value):
        self.ui.progressBar.setValue(value)
        if self.ui.progressBar.value() == 100:
            self.hide()
            self.g.show()


if __name__ == '__main__':
    app = QApplication([])
    f = clsload()
    f.show()
    sys.exit(app.exec_())
