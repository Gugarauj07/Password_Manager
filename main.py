from forms.login import Login
from PyQt6.QtWidgets import QApplication
import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    main_window = Login()
    main_window.show()

    app.exec()
