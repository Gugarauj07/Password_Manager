from windows.compiled.Menu_Window import Ui_menu_window
from windows.compiled.vizualizar_window import Ui_vizualizar_window
from PyQt6 import QtCore, QtGui, QtWidgets
from conecta import *


class Menu(QtWidgets.QMainWindow, Ui_menu_window):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.setupUi(self)

        self.connect_buttons()

    def connect_buttons(self):
        # FUNCTIONS
        self.actionGerar_senhas.clicked.connect(self.gerar)
        self.actionVisualizar_Senhas.clicked.connect(self.vizualisar)
        self.actionAdicionar_senhas.clicked.connect(self.adicionar)

    def adicionar(self):
        pass

    def gerar(self):
        pass

    def vizualisar(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_vizualizar_window()
        self.ui.setupUi(self.window)
        self.window.show()
        self.hide()

        with conecta() as conexao:
            with conexao.cursor() as cursor:
                comando_SQL = "SELECT * FROM login"
                cursor.execute(comando_SQL)
                dados_lidos = cursor.fetchall()

                for k, v in dados_lidos[0].items():
                    print(k, v)

        self.ui.tableWidget.setRowCount(len(dados_lidos))
        self.ui.tableWidget.setColumnCount(3)

        try:
            for i in range(0, len(dados_lidos)):
                self.ui.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['id'])))
                self.ui.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['username'])))
                self.ui.tableWidget.setItem(i, 2, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['master_password'])))
        except:
            pass
