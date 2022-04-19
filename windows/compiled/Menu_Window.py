from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_menu_window(object):

    def setupUi(self, menu_window):
        menu_window.setObjectName("menu_window")
        menu_window.resize(240, 119)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        menu_window.setFont(font)
        menu_window.setStyleSheet("background-color: rgb(44, 44, 44);\n"
                                  "color: rgb(255, 105, 182);")
        self.centralwidget = QtWidgets.QWidget(menu_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 0, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 221, 31))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        menu_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(menu_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 240, 22))
        self.menubar.setObjectName("menubar")
        self.menuMENU = QtWidgets.QMenu(self.menubar)
        self.menuMENU.setObjectName("menuMENU")
        menu_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(menu_window)
        self.statusbar.setObjectName("statusbar")
        menu_window.setStatusBar(self.statusbar)
        self.actionVisualizar_Senhas = QtGui.QAction(menu_window)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionVisualizar_Senhas.setFont(font)
        self.actionVisualizar_Senhas.setObjectName("actionVisualizar_Senhas")
        self.actionGerar_senhas = QtGui.QAction(menu_window)
        self.actionGerar_senhas.setObjectName("actionGerar_senhas")
        self.actionAdicionar_senhas = QtGui.QAction(menu_window)
        self.actionAdicionar_senhas.setObjectName("actionAdicionar_senhas")
        self.menuMENU.addAction(self.actionVisualizar_Senhas)
        self.menuMENU.addAction(self.actionGerar_senhas)
        self.menuMENU.addAction(self.actionAdicionar_senhas)
        self.menubar.addAction(self.menuMENU.menuAction())

        self.retranslateUi(menu_window)
        QtCore.QMetaObject.connectSlotsByName(menu_window)

    def retranslateUi(self, menu_window):
        _translate = QtCore.QCoreApplication.translate
        menu_window.setWindowTitle(_translate("menu_window", "MainWindow"))
        self.label.setText(_translate("menu_window", "Password Manager"))
        self.label_2.setText(_translate("menu_window", "Please, choose an option from the menu!"))
        self.menuMENU.setTitle(_translate("menu_window", "MENU"))
        self.actionVisualizar_Senhas.setText(_translate("menu_window", "Visualizar senhas"))
        self.actionGerar_senhas.setText(_translate("menu_window", "Gerador de senhas"))
        self.actionAdicionar_senhas.setText(_translate("menu_window", "Adicionar senhas"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    menu_window = QtWidgets.QMainWindow()
    ui = Ui_menu_window()
    ui.setupUi(menu_window)
    menu_window.show()
    sys.exit(app.exec())
