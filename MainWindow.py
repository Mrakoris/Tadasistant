import openai
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QPushButton, QScrollArea, QSizePolicy, QWidget, QMessageBox, QTextEdit)
import rc_icons
import registerWindow
import requestData
import chatAnswers

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMaximumSize(QSize(800, 600))
        Form.setStyleSheet(u"background-color: rgb(239, 239, 239);")
        self.chatRequestName = QLabel(Form)
        self.chatRequestName.setObjectName(u"chatRequestName")
        self.chatRequestName.setGeometry(QRect(200, 10, 560, 40))
        font = QFont()
        font.setFamilies([u"MS Reference Sans Serif"])
        font.setPointSize(10)
        font.setBold(True)
        self.chatRequestName.setFont(font)
        self.chatRequestName.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
"color: rgb(250, 255, 255);")
        self.chatRequestName.setText(u"\u041f\u043e\u043b\u0443\u0447\u0435\u043d\u0438\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u0438 \u043f\u043e \u0434\u0435\u0439\u0441\u0442\u0432\u0443\u044e\u0449\u0435\u043c\u0443 \u0437\u0430\u043a\u043e\u043d\u043e\u0434\u0430\u0442\u0435\u043b\u044c\u0441\u0442\u0432\u0443 \u0420\u0424")
        self.chatRequestName.setMargin(6)
        self.chatRequestName.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextEditable)
        self.stringInput = QLineEdit(Form)
        self.stringInput.setObjectName(u"stringInput")
        self.stringInput.setGeometry(QRect(200, 530, 560, 30))
        font1 = QFont()
        font1.setFamilies([u"MS Reference Sans Serif"])
        font1.setPointSize(11)
        self.stringInput.setFont(font1)
        self.stringInput.setMaxLength(80)
        self.btnStringInput = QPushButton(Form)
        self.btnStringInput.setObjectName(u"btnStringInput")
        self.btnStringInput.setGeometry(QRect(730, 530, 30, 30))
        self.btnStringInput.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
"color: rgb(250, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/materials/subdirectory_arrow_left_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnStringInput.setIcon(icon)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 170, 600))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
"")
        self.menuName = QLabel(Form)
        self.menuName.setObjectName(u"menuName")
        self.menuName.setGeometry(QRect(10, 20, 150, 20))
        sizePolicy.setHeightForWidth(self.menuName.sizePolicy().hasHeightForWidth())
        self.menuName.setSizePolicy(sizePolicy)
        font2 = QFont()
        font2.setFamilies([u"MS Reference Sans Serif"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.menuName.setFont(font2)
        self.menuName.setLayoutDirection(Qt.RightToLeft)
        self.menuName.setAutoFillBackground(False)
        self.menuName.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
"")
        self.menuName.setAlignment(Qt.AlignCenter)
        self.namePerson = QLabel(Form)
        self.namePerson.setObjectName(u"namePerson")
        self.namePerson.setGeometry(QRect(30, 60, 130, 20))
        font3 = QFont()
        font3.setFamilies([u"MS Reference Sans Serif"])
        font3.setPointSize(8)
        font3.setBold(False)
        self.namePerson.setFont(font3)
        self.namePerson.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
"")
        self.namePerson.setFrameShape(QFrame.NoFrame)
        self.namePerson.setAlignment(Qt.AlignCenter)
        self.namePerson.setWordWrap(False)
        self.namePerson.setOpenExternalLinks(True)
        self.namePerson.setTextInteractionFlags(Qt.TextEditable)
        self.btnChatOne = QPushButton(Form)
        self.btnChatOne.setObjectName(u"btnChatOne")
        self.btnChatOne.setGeometry(QRect(40, 110, 110, 20))
        font4 = QFont()
        font4.setFamilies([u"MS Reference Sans Serif"])
        font4.setPointSize(10)
        font4.setBold(False)
        self.btnChatOne.setFont(font4)
        self.btnChatOne.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(250, 255, 255);\n"
"")
        self.chatIconOne = QLabel(Form)
        self.chatIconOne.setObjectName(u"chatIconOne")
        self.chatIconOne.setGeometry(QRect(10, 110, 20, 20))
        self.chatIconOne.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
"")
        self.chatIconOne.setPixmap(QPixmap(u":/materials/counter_1_FILL0_wght400_GRAD0_opsz48.svg"))
        self.chatIconOne.setScaledContents(True)
        self.btnChatTwo = QPushButton(Form)
        self.btnChatTwo.setObjectName(u"btnChatTwo")
        self.btnChatTwo.setGeometry(QRect(40, 150, 110, 20))
        self.btnChatTwo.setFont(font4)
        self.btnChatTwo.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(250, 255, 255);\n"
"")
        self.chatIconTwo = QLabel(Form)
        self.chatIconTwo.setObjectName(u"chatIconTwo")
        self.chatIconTwo.setGeometry(QRect(10, 150, 20, 20))
        self.chatIconTwo.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
"")
        self.chatIconTwo.setPixmap(QPixmap(u":/materials/counter_2_FILL0_wght400_GRAD0_opsz48.svg"))
        self.chatIconTwo.setScaledContents(True)
        self.btnChatThree = QPushButton(Form)
        self.btnChatThree.setObjectName(u"btnChatThree")
        self.btnChatThree.setGeometry(QRect(40, 190, 110, 20))
        self.btnChatThree.setFont(font4)
        self.btnChatThree.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
                                        "color: rgb(250, 255, 255);\n"
                                        "")
        self.btnChatThree.setCheckable(False)
        self.chatIconThree = QLabel(Form)
        self.chatIconThree.setObjectName(u"chatIconThree")
        self.chatIconThree.setGeometry(QRect(10, 190, 20, 20))
        self.chatIconThree.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
"")
        self.chatIconThree.setPixmap(QPixmap(u":/materials/counter_3_FILL0_wght400_GRAD0_opsz48.svg"))
        self.chatIconThree.setScaledContents(True)
        self.btnChatFour = QPushButton(Form)
        self.btnChatFour.setObjectName(u"btnChatFour")
        self.btnChatFour.setGeometry(QRect(40, 230, 110, 20))
        self.btnChatFour.setFont(font4)
        self.btnChatFour.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(250, 255, 255);\n"
"")
        self.chatIconFour = QLabel(Form)
        self.chatIconFour.setObjectName(u"chatIconFour")
        self.chatIconFour.setGeometry(QRect(10, 230, 20, 20))
        self.chatIconFour.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
"")
        self.chatIconFour.setPixmap(QPixmap(u":/materials/counter_4_FILL0_wght400_GRAD0_opsz48.svg"))
        self.chatIconFour.setScaledContents(True)
        self.iconPerson = QLabel(Form)
        self.iconPerson.setObjectName(u"iconPerson")
        self.iconPerson.setGeometry(QRect(10, 60, 20, 20))
        self.iconPerson.setStyleSheet(u"background-color: rgb(245, 193, 119);\n"
"")
        self.iconPerson.setPixmap(QPixmap(u":/materials/person_FILL0_wght400_GRAD0_opsz48.svg"))
        self.iconPerson.setScaledContents(True)
        self.btnSettings = QPushButton(Form)
        self.btnSettings.setObjectName(u"btnSettings")
        self.btnSettings.setGeometry(QRect(20, 550, 130, 30))
        font5 = QFont()
        font5.setFamilies([u"MS Reference Sans Serif"])
        font5.setPointSize(11)
        font5.setBold(False)
        self.btnSettings.setFont(font5)
        self.btnSettings.setStyleSheet(u"background-color: rgb(200, 200, 200);\n"
"color: rgb(250, 255, 255);\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/materials/settings_FILL0_wght400_GRAD0_opsz48.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSettings.setIcon(icon1)
        self.btnSettings.setIconSize(QSize(20, 20))
        self.scrollChat = QScrollArea(Form)
        self.scrollChat.setObjectName(u"scrollChat")
        self.scrollChat.setGeometry(QRect(200, 70, 560, 450))
        self.scrollChat.setWidgetResizable(True)
        self.scrollChatWidgetContents_2 = QWidget()
        self.scrollChatWidgetContents_2.setObjectName(u"scrollChatWidgetContents_2")
        self.scrollChatWidgetContents_2.setGeometry(QRect(0, 0, 558, 448))
        self.scrollChatWidgetContents_2.setMinimumSize(QSize(558, 0))
        self.scrollChat.setWidget(self.scrollChatWidgetContents_2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

        self.chatRequestName.setText("Выберите чат")
        self.chatName()
        self.settingsBtn()
        self.sendRequest()
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Appsistant.team", None))
        self.stringInput.setPlaceholderText(QCoreApplication.translate("Form", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0437\u0430\u043f\u0440\u043e\u0441 (\u043d\u0435 \u0431\u043e\u043b\u0435\u0435 80-\u0442\u0438 \u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432)", None))
        self.btnStringInput.setText("")
        self.label.setText("")
        self.menuName.setText(QCoreApplication.translate("Form", u"\u041c\u0435\u043d\u044e", None))
        self.namePerson.setText(QCoreApplication.translate("Form", u"\u0421\u0442\u0430\u0442\u0443\u0441 \u043f\u043e\u0434\u0442\u0432\u0435\u0440\u0436\u0434\u0435\u043d", None))
        self.btnChatOne.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u043e\u043d\u044b \u0420\u0424", None))
        self.btnChatTwo.setText(QCoreApplication.translate("Form", u"\u0411\u0443\u0445. \u0423\u0447\u0435\u0442", None))
        self.btnChatThree.setText(QCoreApplication.translate("Form", u"\u041b\u044c\u0433\u043e\u0442\u044b", None))
        self.btnChatFour.setText(QCoreApplication.translate("Form", u"\u0410\u043d\u0430\u043b\u0438\u0442\u0438\u043a\u0430", None))
        self.btnSettings.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

    def chatName(self):
        self.btnChatOne.clicked.connect(lambda:self.chatRequestName.setText("Получение информации по действующему законодательству РФ"))
        self.btnChatTwo.clicked.connect(lambda:self.chatRequestName.setText("Информация по нормам и принципам бух.учета в РФ"))
        self.btnChatThree.clicked.connect(lambda:self.chatRequestName.setText("Информация для разного типа бизнеса в РФ"))
        self.btnChatFour.clicked.connect(lambda:self.chatRequestName.setText("Информация по рыночной аналитике определенной области"))

    def settingsBtn(self):
        self.btnSettings.clicked.connect(self.showSettingsMessageBox)
    def showSettingsMessageBox(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Настройки")
        msgBox.setText("Настройки будут позже")
        msgBox.setIcon(QMessageBox.Information)
        msgBox.addButton(QMessageBox.Ok)
        msgBox.addButton(QMessageBox.Cancel)

        returnValue = msgBox.exec()

        if returnValue == QMessageBox.Ok:
            print("Нажата кнопка Окей")
        elif returnValue == QMessageBox.Cancel:
            print("Нажата кнопка Отмена")

    def sendRequest(self):
        self.btnStringInput.clicked.connect(self.chatAnswer)

    def chatAnswer(self):
        # Я не понимаю, как сюда передать логин, перепробовал всё, что пришло в голову, доделать.
        requestData.initFileRequest()
        requestData.reQuest(login="root", request=self.stringInput.text())
        message = self.stringInput.text()
        chatAnswers.messages.append({"role": "user", "content": message})
        reply = chatAnswers.check_topic_filter(message)
        text_edit = QLabel()
        text_edit.setFixedWidth(500)
        text_edit.setWordWrap(True)
        font = QFont()
        font.setPointSize(10)
        text_edit.setFont(font)
        text_edit.setContentsMargins(20, 20, 20, 20)
        self.scrollChat.setWidget(text_edit)
        if reply is not None:
            text_edit.setText("Ответ : " + reply)
        else:
            return
