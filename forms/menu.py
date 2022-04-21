from windows.compiled.menu_window import Ui_menu_window
from PyQt6 import QtCore, QtGui, QtWidgets
from conecta import *


class Menu(QtWidgets.QMainWindow, Ui_menu_window):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        menu_window = QtWidgets.QMainWindow()
        self.ui = Ui_menu_window()
        self.ui.setupUi(menu_window)
        menu_window.show()

        self.connect_buttons()

    def connect_buttons(self):
        self.ui.addButton.clicked.connect(self.adicionar)
        self.ui.generateButton.clicked.connect(self.generate)

    def adicionar(self):
        self.website = self.lineEdit.text()
        self.email = self.lineEdit_2.text()
        self.password = self.lineEdit_3.text()
        self.username = self.lineEdit_4.text()

        with conecta() as conexao:
            with conexao.cursor() as cursor:
                create_table = "CREATE TABLE IF NOT EXISTS pessoas(" \
                               "id INT AUTO_INCREMENT NOT NULL," \
                               "website VARCHAR(255) NOT NULL," \
                               "email VARCHAR(255) NOT NULL," \
                               "password VARCHAR(255) NOT NULL," \
                               "username VARCHAR(255)," \
                               "PRIMARY KEY(id)" \
                               ");"
                cursor.execute(create_table)

                comando_SQL = "INSERT INTO pessoas (website, email, password, username) VALUES (%s,%s,%s,%s)"
                cursor.execute(comando_SQL, (str(self.website), str(self.email), str(self.password), str(self.username)))
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")

    def vizualisar(self):
        pass
        # with conecta() as conexao:
        #     with conexao.cursor() as cursor:
        #         comando_SQL = "SELECT * FROM login"
        #         cursor.execute(comando_SQL)
        #         dados_lidos = cursor.fetchall()
        #
        #         for k, v in dados_lidos[0].items():
        #             print(k, v)
        #
        # self.ui.tableWidget.setRowCount(len(dados_lidos))
        # self.ui.tableWidget.setColumnCount(3)
        #
        # try:
        #     for i in range(0, len(dados_lidos)):
        #         self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['id'])))
        #         self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['username'])))
        #         self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['master_password'])))
        # except:
        #     pass

    def generate(self):
        print('generate')
