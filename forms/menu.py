from windows.compiled.login_window import Ui_Login_Window
from windows.compiled.Menu_Window import Ui_menu_window
from PyQt6 import QtCore, QtGui, QtWidgets
from main import conecta


class Menu(QtWidgets.QMainWindow, Ui_menu_window):
    def __init__(self, parent=None):
        super(Menu, self).__init__(parent)
        self.setupUi(self, Ui_Login_Window)

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
        pass
