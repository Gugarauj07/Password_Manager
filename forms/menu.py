from windows.compiled.menu_window import Ui_menu_window
from PyQt6 import QtCore, QtGui, QtWidgets
from conecta import *


class Menu(QtWidgets.QMainWindow, Ui_menu_window):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        menu_window = QtWidgets.QMainWindow()
        ui = Ui_menu_window()
        ui.setupUi(menu_window)
        menu_window.show()

        self.connect_buttons()

    def connect_buttons(self):
        pass

    def adicionar(self):
        print('oi')

    def vizualisar(self):
        pass
        # self.window = QtWidgets.QMainWindow()
        # self.ui.setupUi(self.window)
        # self.window.show()
        # self.hide()
        #
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
