# Form implementation generated from reading ui file '.\windows\ui\menu_window.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_menu_window(object):
    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.resize(432, 291)
        menu_window.setStyleSheet("background-color: rgb(42, 42, 42);\n"
"color: rgb(255, 105, 182);")
        self.centralwidget = QtWidgets.QWidget(menu_window)
        self.centralwidget.setObjectName("centralwidget")
        self.Menu = QtWidgets.QTabWidget(self.centralwidget)
        self.Menu.setGeometry(QtCore.QRect(0, 0, 431, 331))
        self.Menu.setDocumentMode(True)
        self.Menu.setTabsClosable(False)
        self.Menu.setMovable(True)
        self.Menu.setTabBarAutoHide(False)
        self.Menu.setObjectName("Menu")
        self.Visualize = QtWidgets.QWidget()
        self.Visualize.setObjectName("Visualize")
        self.tableView = QtWidgets.QTableView(self.Visualize)
        self.tableView.setGeometry(QtCore.QRect(0, 0, 431, 241))
        self.tableView.setObjectName("tableView")
        self.Menu.addTab(self.Visualize, "")
        self.Add = QtWidgets.QWidget()
        self.Add.setObjectName("Add")
        self.gridLayoutWidget = QtWidgets.QWidget(self.Add)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 0, 411, 221))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setStyleSheet("background-color: rgb(66, 66, 66);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.Add)
        self.pushButton.setGeometry(QtCore.QRect(40, 220, 345, 21))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")
        self.Menu.addTab(self.Add, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(10, 0, 411, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 50, 345, 21))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 80, 411, 141))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.Menu.addTab(self.tab, "")
        menu_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menu_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 432, 22))
        self.menubar.setObjectName("menubar")
        menu_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menu_window)
        self.statusbar.setObjectName("statusbar")
        menu_window.setStatusBar(self.statusbar)

        self.retranslateUi(menu_window)
        self.Menu.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(menu_window)

    def retranslateUi(self, menu_window):
        _translate = QtCore.QCoreApplication.translate
        menu_window.setWindowTitle(_translate("menu_window", "MainWindow"))
        self.Menu.setTabText(self.Menu.indexOf(self.Visualize), _translate("menu_window", "Visualize"))
        self.label.setText(_translate("menu_window", "Website:"))
        self.label_2.setText(_translate("menu_window", "E-mail:"))
        self.label_3.setText(_translate("menu_window", "Password:"))
        self.label_4.setText(_translate("menu_window", "Username:"))
        self.pushButton.setText(_translate("menu_window", "Submit"))
        self.Menu.setTabText(self.Menu.indexOf(self.Add), _translate("menu_window", "Add"))
        self.label_5.setText(_translate("menu_window", "Press the button to generate a random password!"))
        self.pushButton_2.setText(_translate("menu_window", "Generate!"))
        self.label_7.setText(_translate("menu_window", "Your password is: "))
        self.Menu.setTabText(self.Menu.indexOf(self.tab), _translate("menu_window", "Generate"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    menu_window = QtWidgets.QMainWindow()
    ui = Ui_menu_window()
    ui.setupUi(menu_window)
    menu_window.show()
    sys.exit(app.exec())