from windows.compiled.login_window import Ui_Login_Window
from forms.menu import *
from PyQt6 import QtCore, QtGui, QtWidgets
from conecta import *


class Login(QtWidgets.QMainWindow, Ui_Login_Window):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setupUi(self)

        self.connect_buttons()

    def connect_buttons(self):
        # FUNCTIONS
        self.pushButton.clicked.connect(self.Login)
        self.pushButton_2.clicked.connect(self.Register)

    def Register(self):
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()

        with conecta() as conexao:
            with conexao.cursor() as cursor:
                create_table = "CREATE TABLE IF NOT EXISTS login(" \
                               "id INT AUTO_INCREMENT NOT NULL," \
                               "username VARCHAR(50) NOT NULL," \
                               "master_password VARCHAR(255) NOT NULL," \
                               "PRIMARY KEY(id)" \
                               ");"
                cursor.execute(create_table)

                comando_SQL = "INSERT INTO login (username, master_password) VALUES (%s,%s)"
                cursor.execute(comando_SQL, (str(self.username), str(self.password)))
                conexao.commit()
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")

    def Login(self):
        self.username = self.lineEdit.text()
        self.password = self.lineEdit_2.text()
        self.nomes = []
        self.senhas = []

        with conecta() as conexao:
            with conexao.cursor() as cursor:
                comando_SQL = "SELECT username, master_password FROM login"
                cursor.execute(comando_SQL)
                dados_lidos = cursor.fetchall()
                print(dados_lidos)

        for i in range(len(dados_lidos)):
            self.nomes.append(dados_lidos[i]['username'])
            self.senhas.append(dados_lidos[i]['master_password'])

        if self.password in self.senhas and self.username in self.nomes:
            self.window = QtWidgets.QMainWindow()
            self.ui = Menu()
            self.ui.setupUi(self.window)
            self.hide()
            self.window.show()
