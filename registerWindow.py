import self as self

import __main__
import userDataBase

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize, Qt)
from PySide6.QtGui import (QCursor, QFont, QPixmap,)
from PySide6.QtWidgets import (QFrame, QLabel, QLineEdit,
                               QPushButton, QSizePolicy, QWidget, QMessageBox, QMainWindow, QApplication)
import rc_icons


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(800, 600))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setStyleSheet(u"\n"
                                 "background-color: rgb(239, 239, 239);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.authLogo = QLabel(self.centralwidget)
        self.authLogo.setObjectName(u"authLogo")
        self.authLogo.setGeometry(QRect(275, 110, 250, 81))
        sizePolicy.setHeightForWidth(self.authLogo.sizePolicy().hasHeightForWidth())
        self.authLogo.setSizePolicy(sizePolicy)
        self.authLogo.setPixmap(QPixmap(u":/materials/Tada_logo.jpg"))
        self.authLogin = QLineEdit(self.centralwidget)
        self.authLogin.setObjectName(u"authLogin")
        self.authLogin.setEnabled(True)
        self.authLogin.setGeometry(QRect(290, 250, 231, 31))
        sizePolicy.setHeightForWidth(self.authLogin.sizePolicy().hasHeightForWidth())
        self.authLogin.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(11)
        self.authLogin.setFont(font)
        self.authLogin.setCursor(QCursor(Qt.ArrowCursor))
        self.authLogin.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
                                     "border:1px solid black;\n"
                                     "")
        self.authLogin.setMaxLength(24)
        self.authLogin.setFrame(False)
        self.authText = QLabel(self.centralwidget)
        self.authText.setObjectName(u"authText")
        self.authText.setGeometry(QRect(280, 220, 251, 21))
        sizePolicy.setHeightForWidth(self.authText.sizePolicy().hasHeightForWidth())
        self.authText.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"MS Reference Sans Serif"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        font1.setKerning(True)
        self.authText.setFont(font1)
        self.authText.setCursor(QCursor(Qt.ArrowCursor))
        self.authText.setLayoutDirection(Qt.LeftToRight)
        self.authText.setAutoFillBackground(False)
        self.authText.setFrameShape(QFrame.NoFrame)
        self.authText.setFrameShadow(QFrame.Plain)
        self.authText.setLineWidth(1)
        self.authText.setMidLineWidth(1)
        self.authText.setAlignment(Qt.AlignCenter)
        self.authText.setMargin(20)
        self.authPass = QLineEdit(self.centralwidget)
        self.authPass.setObjectName(u"authPass")
        self.authPass.setEnabled(True)
        self.authPass.setGeometry(QRect(290, 290, 231, 31))
        sizePolicy.setHeightForWidth(self.authPass.sizePolicy().hasHeightForWidth())
        self.authPass.setSizePolicy(sizePolicy)
        self.authPass.setFont(font)
        self.authPass.setCursor(QCursor(Qt.ArrowCursor))
        self.authPass.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
                                    "border:1px solid black;\n"
                                    "")
        self.authPass.setMaxLength(24)
        self.authPass.setFrame(False)
        self.btnRegister = QPushButton(self.centralwidget)
        self.btnRegister.setObjectName(u"btnRegister")
        self.btnRegister.setGeometry(QRect(300, 340, 101, 21))
        font2 = QFont()
        font2.setFamilies([u"MS Reference Sans Serif"])
        font2.setPointSize(9)
        self.btnRegister.setFont(font2)
        self.btnRegister.setStyleSheet(u"background-color: rgb(245, 193, 119);")
        self.btnLogin = QPushButton(self.centralwidget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(410, 340, 101, 21))
        font3 = QFont()
        font3.setFamilies([u"MS Reference Sans Serif"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setUnderline(False)
        self.btnLogin.setFont(font3)
        self.btnLogin.setStyleSheet(u"background-color: rgb(245, 193, 119);")
        self.btnLogin.setIconSize(QSize(13, 13))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        self.addUser()

        self.getUser()
    
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Appsistant.team", None))
        self.authLogo.setText("")
        self.authLogin.setInputMask("")
        self.authLogin.setText("")
        self.authLogin.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.authText.setText(QCoreApplication.translate("MainWindow",
                                                         u"\u0410\u0432\u0442\u043e\u0440\u0438\u0437\u0430\u0446\u0438\u044f",
                                                         None))
        self.authPass.setInputMask("")
        self.authPass.setText("")
        self.authPass.setPlaceholderText(
            QCoreApplication.translate("MainWindow", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.btnRegister.setText(QCoreApplication.translate("MainWindow",
                                                            u"\u0420\u0435\u0433\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f",
                                                            None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0445\u043e\u0434", None))
    # retranslateUi

    def addUser(self):
        self.btnRegister.clicked.connect(self.addLogin)

    def addLogin(self):
        username = self.authLogin.text()
        passWord = self.authPass.text()
        if (not username) or (not passWord):
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Пожалуйста, заполните все поля")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            return
        else:
            userDataBase.initFile()
            userDataBase.addUser(login=self.authLogin.text(), password=self.authPass.text())
            msg = QMessageBox()
            msg.setWindowTitle("Успешная регистрация!")
            msg.setText("Вы успешно зарегистрировались, можете входить")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
            

    def getUser(self):
        self.btnLogin.clicked.connect(self.checkLogin)

    def checkLogin(self):
        username = self.authLogin.text()
        passWord = self.authPass.text()
        if (not username) or (not passWord):
            error = QMessageBox()
            error.setWindowTitle("Ошибка")
            error.setText("Пожалуйста, заполните все поля")
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()
            return
        else:
            userDataBase.getUser(login=self.authLogin.text(), password=self.authPass.text())
            __main__.openMainWindow()