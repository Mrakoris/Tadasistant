import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow

import MainWindow
from registerWindow import Ui_MainWindow
from MainWindow import Ui_Form


class Appsistant(QMainWindow):
    def __init__(self):
        super(Appsistant, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = Appsistant()
    window.show()

    def openMainWindow():
        global nextWindow
        nextWindow = QtWidgets.QDialog()
        ui = Ui_Form()
        ui.setupUi(nextWindow)
        window.close()
        nextWindow.show()

    sys.exit(app.exec())
