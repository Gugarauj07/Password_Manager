from contextlib import contextmanager
import pymysql.cursors
from forms.login import Login
from PyQt6.QtWidgets import QApplication
import sys


@contextmanager
def conecta():
    conexao = pymysql.connect(
        host='127.0.0.1',
        user='root',
        password='',
        db='password_manager',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        yield conexao
    finally:
        conexao.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = Login()
    main_window.show()

    app.exec()
