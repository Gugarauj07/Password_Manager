from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Login_Window(object):

    def setupUi(self, Login_Window):
        Login_Window.setObjectName("Login_Window")
        Login_Window.resize(309, 197)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        Login_Window.setFont(font)
        Login_Window.setStyleSheet("background-color: rgb(44, 44, 44);\n"
                                   "color: rgb(255, 105, 182);")
        self.centralwidget = QtWidgets.QWidget(Login_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(30)
        font.setBold(True)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 50, 291, 91))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 140, 291, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setStyleSheet("background-color: rgb(255, 105, 182);\n"
                                      "color: rgb(44, 44, 44);")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 105, 182);\n"
                                        "color: rgb(44, 44, 44);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        Login_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Login_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 309, 22))
        self.menubar.setObjectName("menubar")
        Login_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Login_Window)
        self.statusbar.setObjectName("statusbar")
        Login_Window.setStatusBar(self.statusbar)

        self.retranslateUi(Login_Window)
        QtCore.QMetaObject.connectSlotsByName(Login_Window)

    def retranslateUi(self, Login_Window):
        _translate = QtCore.QCoreApplication.translate
        Login_Window.setWindowTitle(_translate("Login_Window", "MainWindow"))
        self.label.setText(_translate("Login_Window", "LOGIN"))
        self.label_2.setText(_translate("Login_Window", "Username:"))
        self.label_3.setText(_translate("Login_Window", "Password: "))
        self.pushButton.setText(_translate("Login_Window", "Login"))
        self.pushButton_2.setText(_translate("Login_Window", "Register"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Login_Window = QtWidgets.QMainWindow()
    ui = Ui_Login_Window()
    ui.setupUi(Login_Window)
    Login_Window.show()
    sys.exit(app.exec())
