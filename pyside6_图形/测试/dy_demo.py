# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dy_demo.ui'
##
## Created by: Qt User Interface Compiler version 6.3.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(411, 511)
        self.inputUrl = QLineEdit(Form)
        self.inputUrl.setObjectName(u"inputUrl")
        self.inputUrl.setGeometry(QRect(10, 200, 271, 21))
        self.startGet = QPushButton(Form)
        self.startGet.setObjectName(u"startGet")
        self.startGet.setGeometry(QRect(290, 200, 71, 21))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 180, 111, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(11, 1, 36, 16))
        self.loglabel = QLabel(Form)
        self.loglabel.setObjectName(u"loglabel")
        self.loglabel.setGeometry(QRect(10, 230, 41, 31))
        self.startBase = QPushButton(Form)
        self.startBase.setObjectName(u"startBase")
        self.startBase.setGeometry(QRect(240, 130, 81, 21))
        self.logPrint = QTextBrowser(Form)
        self.logPrint.setObjectName(u"logPrint")
        self.logPrint.setGeometry(QRect(10, 260, 371, 231))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(241, 41, 165, 23))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.inputPort = QLineEdit(self.widget)
        self.inputPort.setObjectName(u"inputPort")

        self.horizontalLayout_2.addWidget(self.inputPort)

        self.widget1 = QWidget(Form)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(242, 80, 165, 23))
        self.horizontalLayout_4 = QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.widget1)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.inputPassword = QLineEdit(self.widget1)
        self.inputPassword.setObjectName(u"inputPassword")

        self.horizontalLayout_4.addWidget(self.inputPassword)

        self.widget2 = QWidget(Form)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(11, 42, 152, 23))
        self.horizontalLayout = QHBoxLayout(self.widget2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.widget2)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.inputIp = QLineEdit(self.widget2)
        self.inputIp.setObjectName(u"inputIp")

        self.horizontalLayout.addWidget(self.inputIp)

        self.widget3 = QWidget(Form)
        self.widget3.setObjectName(u"widget3")
        self.widget3.setGeometry(QRect(11, 84, 165, 23))
        self.horizontalLayout_3 = QHBoxLayout(self.widget3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget3)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.inputUser = QLineEdit(self.widget3)
        self.inputUser.setObjectName(u"inputUser")

        self.horizontalLayout_3.addWidget(self.inputUser)

        self.widget4 = QWidget(Form)
        self.widget4.setObjectName(u"widget4")
        self.widget4.setGeometry(QRect(11, 125, 201, 23))
        self.horizontalLayout_5 = QHBoxLayout(self.widget4)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget4)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.inputDataBase = QLineEdit(self.widget4)
        self.inputDataBase.setObjectName(u"inputDataBase")

        self.horizontalLayout_5.addWidget(self.inputDataBase)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.startGet.setText(QCoreApplication.translate("Form", u"2.\u5f00\u59cb\u83b7\u53d6", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6296\u97f3\u76f4\u64ad\u95f4\u7f51\u5740\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u5e93", None))
        self.loglabel.setText(QCoreApplication.translate("Form", u"\u65e5\u5fd7\uff1a", None))
        self.startBase.setText(QCoreApplication.translate("Form", u"1.\u8fde\u63a5\u6570\u636e\u5e93", None))
        self.logPrint.setHtml(QCoreApplication.translate("Form", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">\u6b65\u9aa4\uff1a</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.\u8bf7\u8fde\u63a5\u6570\u636e\u5e93<br />2.\u83b7\u53d6dy\u7f51\u9875\u76f4\u64ad\u95f4\u5730\u5740\uff0c\u4f8b\u5982\uff1ahttps://live.douyin.com/xxxxx</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7aef\u53e3", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ip", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u7528\u6237", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u6570\u636e\u5e93\u540d\u79f0", None))
    # retranslateUi

