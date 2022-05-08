from windows.compiled.menu_window import Ui_menu_window
from PyQt6 import QtCore, QtGui, QtWidgets
from conecta import *


class Menu(QtWidgets.QMainWindow, Ui_menu_window):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.setupUi(self)
        self.connect_buttons()
        self.visualizar()

    def connect_buttons(self):
        self.addButton.clicked.connect(self.adicionar)
        self.generateButton.clicked.connect(self.generate)

    def adicionar(self):
        from forms.login import Login
        self.login = Login()
        self.website = self.lineEdit.text()
        self.email = self.lineEdit_2.text()
        self.password = self.lineEdit_3.text()
        self.username = self.lineEdit_4.text()

        with conecta() as conexao:
            with conexao.cursor() as cursor:
                create_table = "CREATE TABLE IF NOT EXISTS menu(" \
                               "id INT AUTO_INCREMENT NOT NULL," \
                               "website VARCHAR(255) NOT NULL," \
                               "email VARCHAR(255) NOT NULL," \
                               "password VARCHAR(255) NOT NULL," \
                               "username VARCHAR(255)," \
                               "login_id INT NOT NULL," \
                               "PRIMARY KEY(id)," \
                               "FOREIGN KEY(login_id) REFERENCES login(id)" \
                               ");"
                cursor.execute(create_table)

                comando_SQL = "INSERT INTO menu(website, email, password, username, login_id) VALUES (%s,%s,%s,%s,%s);"
                cursor.execute(comando_SQL, (str(self.website), str(self.email), str(self.password), str(self.username),
                                             int(self.login.login_id)))
                conexao.commit()

        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.visualizar()

    def visualizar(self):
        with conecta() as conexao:
            with conexao.cursor() as cursor:
                comando_SQL = "SELECT website, email, password, username FROM menu JOIN login ON login.id = menu.login_id;"
                cursor.execute(comando_SQL)
                dados_lidos = cursor.fetchall()

                for k, v in dados_lidos[0].items():
                    print(k, v)

        self.tableWidget.setRowCount(len(dados_lidos))
        self.tableWidget.setColumnCount(4)

        try:
            for i in range(0, len(dados_lidos)):
                self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['website'])))
                self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['email'])))
                self.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['password'])))
                self.tableWidget.setItem(i, 3, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['username'])))
        except:
            pass

    def generate(self):
        print('generate')
