# Form implementation generated from reading ui file '.\windows\ui\Menu_Window.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Menu_window(object):
    def setupUi(self, Menu_window):
        Menu_window.setObjectName("Menu_window")
        Menu_window.resize(250, 150)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        Menu_window.setFont(font)
        Menu_window.setStyleSheet("background-color: rgb(44, 44, 44);\n"
"color: rgb(0, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(Menu_window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 231, 81))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(44, 44, 44);")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"color: rgb(44, 44, 44);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, -10, 229, 59))
        font = QtGui.QFont()
        font.setPointSize(19)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.StyleStrategy.PreferDefault)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        Menu_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Menu_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 250, 22))
        self.menubar.setObjectName("menubar")
        Menu_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Menu_window)
        self.statusbar.setObjectName("statusbar")
        Menu_window.setStatusBar(self.statusbar)

        self.retranslateUi(Menu_window)
        QtCore.QMetaObject.connectSlotsByName(Menu_window)

    def retranslateUi(self, Menu_window):
        _translate = QtCore.QCoreApplication.translate
        Menu_window.setWindowTitle(_translate("Menu_window", "MainWindow"))
        self.pushButton.setText(_translate("Menu_window", "LOGIN"))
        self.pushButton_2.setText(_translate("Menu_window", "REGISTER"))
        self.label.setText(_translate("Menu_window", "Password Manager"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Menu_window = QtWidgets.QMainWindow()
    ui = Ui_Menu_window()
    ui.setupUi(Menu_window)
    Menu_window.show()
    sys.exit(app.exec())
