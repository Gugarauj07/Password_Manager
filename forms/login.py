from windows.compiled.login_window import Ui_Login_Window
from windows.compiled.Menu_Window import Ui_menu_window
from PyQt6 import QtCore, QtGui, QtWidgets
from main import conecta


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
        self.window = QtWidgets.QMainWindow()

        self.ui = Ui_menu_window()
        self.ui.setupUi(self.window, self)
        self.hide()
        self.window.show()

        # with conecta() as conexao:
        #     with conexao.cursor() as cursor:
        #         comando_SQL = "SELECT * FROM register"
        #         cursor.execute(comando_SQL)
        #         dados_lidos = cursor.fetchall()
        #
        #         for k, v in dados_lidos[0].items():
        #             print(k, v)
        #
        # self.ui.SecondWindow.setRowCount(len(dados_lidos))
        # self.ui.SecondWindow.setColumnCount(4)
        #
        # try:
        #     for i in range(0, len(dados_lidos)):
        #
        #          self.ui.SecondWindow.setItem(i, 0, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['id'])))
        #          self.ui.SecondWindow.setItem(i, 1, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['nome'])))
        #          self.ui.SecondWindow.setItem(i, 2, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['email'])))
        #          self.ui.SecondWindow.setItem(i, 3, QtWidgets.QTableWidgetItem(str(dados_lidos[i]['telefone'])))
        # except:
        #     pass
