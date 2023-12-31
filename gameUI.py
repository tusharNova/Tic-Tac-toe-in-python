from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 300)
        MainWindow.setMinimumSize(QtCore.QSize(300, 300))
        MainWindow.setMaximumSize(QtCore.QSize(300, 300))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.b1 = QtWidgets.QPushButton(self.centralwidget)
        self.b1.setMinimumSize(QtCore.QSize(50, 50))
        self.b1.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.b1.setFont(font)
        self.b1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b1.setText("")
        self.b1.setObjectName("b1")
        self.horizontalLayout.addWidget(self.b1)
        self.b2 = QtWidgets.QPushButton(self.centralwidget)
        self.b2.setMinimumSize(QtCore.QSize(50, 50))
        self.b2.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b2.setText("")
        self.b2.setObjectName("b2")
        self.horizontalLayout.addWidget(self.b2)
        self.b3 = QtWidgets.QPushButton(self.centralwidget)
        self.b3.setMinimumSize(QtCore.QSize(50, 50))
        self.b3.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.b3.setFont(font)
        self.b3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b3.setText("")
        self.b3.setObjectName("b3")
        self.horizontalLayout.addWidget(self.b3)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.b4 = QtWidgets.QPushButton(self.centralwidget)
        self.b4.setMinimumSize(QtCore.QSize(50, 50))
        self.b4.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.b4.setFont(font)
        self.b4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b4.setText("")
        self.b4.setObjectName("b4")
        self.horizontalLayout_2.addWidget(self.b4)
        self.b5 = QtWidgets.QPushButton(self.centralwidget)
        self.b5.setMinimumSize(QtCore.QSize(50, 50))
        self.b5.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.b5.setFont(font)
        self.b5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b5.setText("")
        self.b5.setObjectName("b5")
        self.horizontalLayout_2.addWidget(self.b5)
        self.b6 = QtWidgets.QPushButton(self.centralwidget)
        self.b6.setMinimumSize(QtCore.QSize(50, 50))
        self.b6.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.b6.setFont(font)
        self.b6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b6.setText("")
        self.b6.setObjectName("b6")
        self.horizontalLayout_2.addWidget(self.b6)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.b7 = QtWidgets.QPushButton(self.centralwidget)
        self.b7.setMinimumSize(QtCore.QSize(50, 50))
        self.b7.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.b7.setFont(font)
        self.b7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b7.setText("")
        self.b7.setObjectName("b7")
        self.horizontalLayout_3.addWidget(self.b7)
        self.b8 = QtWidgets.QPushButton(self.centralwidget)
        self.b8.setMinimumSize(QtCore.QSize(50, 50))
        self.b8.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.b8.setFont(font)
        self.b8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b8.setText("")
        self.b8.setObjectName("b8")
        self.horizontalLayout_3.addWidget(self.b8)
        self.b9 = QtWidgets.QPushButton(self.centralwidget)
        self.b9.setMinimumSize(QtCore.QSize(50, 50))
        self.b9.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.b9.setFont(font)
        self.b9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b9.setText("")
        self.b9.setObjectName("b9")
        self.horizontalLayout_3.addWidget(self.b9)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionRestart = QtWidgets.QAction(MainWindow)
        self.actionRestart.setObjectName("actionRestart")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionRestart)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tic Tac Toe "))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionRestart.setText(_translate("MainWindow", "Restart"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
