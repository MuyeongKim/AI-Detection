# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ex-guihUtrmv.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(422, 618)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 411, 81))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(320, 60, 91, 31))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 100, 121, 41))
        font1 = QFont()
        font1.setPointSize(12)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 121, 41))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 180, 121, 41))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_source = QComboBox(self.centralwidget)
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.addItem("")
        self.comboBox_source.setObjectName(u"comboBox_source")
        self.comboBox_source.setGeometry(QRect(160, 110, 131, 22))
        self.comboBox_data = QComboBox(self.centralwidget)
        self.comboBox_data.addItem("")
        self.comboBox_data.addItem("")
        self.comboBox_data.addItem("")
        self.comboBox_data.addItem("")
        self.comboBox_data.addItem("")
        self.comboBox_data.addItem("")
        self.comboBox_data.setObjectName(u"comboBox_data")
        self.comboBox_data.setGeometry(QRect(160, 150, 131, 22))
        self.lineEdit_juso = QLineEdit(self.centralwidget)
        self.lineEdit_juso.setObjectName(u"lineEdit_juso")
        self.lineEdit_juso.setGeometry(QRect(160, 190, 131, 21))
        self.pushButton_search = QPushButton(self.centralwidget)
        self.pushButton_search.setObjectName(u"pushButton_search")
        self.pushButton_search.setGeometry(QRect(320, 190, 51, 24))
        self.pushButton_enter = QPushButton(self.centralwidget)
        self.pushButton_enter.setObjectName(u"pushButton_enter")
        self.pushButton_enter.setGeometry(QRect(110, 290, 75, 24))
        self.pushButton_close = QPushButton(self.centralwidget)
        self.pushButton_close.setObjectName(u"pushButton_close")
        self.pushButton_close.setGeometry(QRect(230, 290, 75, 24))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(140, 320, 121, 41))
        self.label_6.setFont(font1)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 360, 401, 191))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 220, 121, 41))
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 230, 391, 61))
        font2 = QFont()
        font2.setPointSize(8)
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.comboBox_percentage = QComboBox(self.centralwidget)
        self.comboBox_percentage.addItem("")
        self.comboBox_percentage.addItem("")
        self.comboBox_percentage.addItem("")
        self.comboBox_percentage.addItem("")
        self.comboBox_percentage.addItem("")
        self.comboBox_percentage.setObjectName(u"comboBox_percentage")
        self.comboBox_percentage.setGeometry(QRect(120, 230, 71, 22))
        self.comboBox_device = QComboBox(self.centralwidget)
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.addItem("")
        self.comboBox_device.setObjectName(u"comboBox_device")
        self.comboBox_device.setGeometry(QRect(190, 230, 71, 22))
        self.comboBox_imgsz = QComboBox(self.centralwidget)
        self.comboBox_imgsz.addItem("")
        self.comboBox_imgsz.addItem("")
        self.comboBox_imgsz.addItem("")
        self.comboBox_imgsz.addItem("")
        self.comboBox_imgsz.addItem("")
        self.comboBox_imgsz.addItem("")
        self.comboBox_imgsz.addItem("")
        self.comboBox_imgsz.addItem("")
        self.comboBox_imgsz.setObjectName(u"comboBox_imgsz")
        self.comboBox_imgsz.setGeometry(QRect(260, 230, 71, 22))
        self.comboBox_buffer = QComboBox(self.centralwidget)
        self.comboBox_buffer.addItem("")
        self.comboBox_buffer.addItem("")
        self.comboBox_buffer.addItem("")
        self.comboBox_buffer.setObjectName(u"comboBox_buffer")
        self.comboBox_buffer.setGeometry(QRect(330, 230, 71, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AI\uac1d\uccb4\ud0d0\uc9c0 \ud504\ub85c\uadf8\ub7a8 V.0319", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AI\uac1d\uccb4\ud0d0\uc9c0 \uc2e4\ud589\ud504\ub85c\uadf8\ub7a8", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\uc81c\uc791 : \uae40\ubb34\uc601", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\uc601\uc0c1\uc18c\uc2a4\uc720\ud615", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\ub370\uc774\ud130\ud06c\uae30", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\uc8fc\uc18c\uc785\ub825\ucc3d", None))
        self.comboBox_source.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.comboBox_source.setItemText(1, QCoreApplication.translate("MainWindow", u"\uc678\ubd80\uc601\uc0c1(\ucea1\uccd0\ubcf4\ub4dc)", None))
        self.comboBox_source.setItemText(2, QCoreApplication.translate("MainWindow", u"\uc720\ud29c\ube0c(URL)", None))
        self.comboBox_source.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc0ac\uc9c4", None))
        self.comboBox_source.setItemText(4, QCoreApplication.translate("MainWindow", u"\uc601\uc0c1", None))

        self.comboBox_data.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc120\ud0dd\ud558\uc138\uc694", None))
        self.comboBox_data.setItemText(1, QCoreApplication.translate("MainWindow", u"\ucd5c\ub300", None))
        self.comboBox_data.setItemText(2, QCoreApplication.translate("MainWindow", u"\ub300", None))
        self.comboBox_data.setItemText(3, QCoreApplication.translate("MainWindow", u"\uc911", None))
        self.comboBox_data.setItemText(4, QCoreApplication.translate("MainWindow", u"\uc18c", None))
        self.comboBox_data.setItemText(5, QCoreApplication.translate("MainWindow", u"\ucd5c\uc18c", None))

        self.pushButton_search.setText(QCoreApplication.translate("MainWindow", u"\uac80\uc0c9", None))
        self.pushButton_enter.setText(QCoreApplication.translate("MainWindow", u"\uc2e4\ud589\ud558\uae30", None))
        self.pushButton_close.setText(QCoreApplication.translate("MainWindow", u"\uc885\ub8cc\ud558\uae30", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"[\uc124\uba85\ucc3d]", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"\u203b \uc2e4\ud589\uc815\uc9c0\ub294 \ucf58\uc194\ucc3d\uc5d0\uc11c Ctrl + C \uc785\ub825\n"
"\u203b Cuda\ub294 \uadf8\ub798\ud53d\uce74\ub4dc \uc720\ubb34\uc5d0 \ub530\ub77c \uc0ac\uc6a9\n"
"\u203b \uc678\ubd80\uc601\uc0c1(\ucea1\uccd0\ubcf4\ub4dc) \uc120\ud0dd\uc2dc\uc5d0\ub294 \n"
"\uc8fc\uc18c\uc785\ub825\ucc3d\uc5d0 0 \ub610\ub294 1\uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694\n"
"\n"
"[\ucc28\ud6c4 \uc5c5\ub370\uc774\ud2b8 \ub0b4\uc6a9]\n"
"1. \ucf58\uc194 \uc2e4\ud589\ucc3d \ucd94\uac00", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\uc635\uc158\uc124\uc815", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\uc635\uc158\ubbf8\uc124\uc815\uc2dc \uae30\ubcf8\uac12 : \uc2e0\ub8b0\ub3c4\uac12 30%, \uc0ac\uc6a9\uc7a5\uce58 CPU, \ud574\uc0c1\ub3c4 1920, \ubc84\ud37c ON", None))
        self.comboBox_percentage.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc784\uacc4\uac12", None))
        self.comboBox_percentage.setItemText(1, QCoreApplication.translate("MainWindow", u"15%", None))
        self.comboBox_percentage.setItemText(2, QCoreApplication.translate("MainWindow", u"30%(\uae30\ubcf8\uac12)", None))
        self.comboBox_percentage.setItemText(3, QCoreApplication.translate("MainWindow", u"50%", None))
        self.comboBox_percentage.setItemText(4, QCoreApplication.translate("MainWindow", u"80%", None))

        self.comboBox_device.setItemText(0, QCoreApplication.translate("MainWindow", u"\uc0ac\uc6a9\uc7a5\uce58", None))
        self.comboBox_device.setItemText(1, QCoreApplication.translate("MainWindow", u"CPU(\uae30\ubcf8\uac12)", None))
        self.comboBox_device.setItemText(2, QCoreApplication.translate("MainWindow", u"CUDA(GPU)", None))

        self.comboBox_imgsz.setItemText(0, QCoreApplication.translate("MainWindow", u"\ud574\uc0c1\ub3c4", None))
        self.comboBox_imgsz.setItemText(1, QCoreApplication.translate("MainWindow", u"640", None))
        self.comboBox_imgsz.setItemText(2, QCoreApplication.translate("MainWindow", u"1080", None))
        self.comboBox_imgsz.setItemText(3, QCoreApplication.translate("MainWindow", u"1280", None))
        self.comboBox_imgsz.setItemText(4, QCoreApplication.translate("MainWindow", u"1680", None))
        self.comboBox_imgsz.setItemText(5, QCoreApplication.translate("MainWindow", u"1920(\uae30\ubcf8\uac12)", None))
        self.comboBox_imgsz.setItemText(6, QCoreApplication.translate("MainWindow", u"3000", None))
        self.comboBox_imgsz.setItemText(7, QCoreApplication.translate("MainWindow", u"5000", None))

        self.comboBox_buffer.setItemText(0, QCoreApplication.translate("MainWindow", u"\ubc84\ud37c", None))
        self.comboBox_buffer.setItemText(1, QCoreApplication.translate("MainWindow", u"ON(\uae30\ubcf8\uac12)", None))
        self.comboBox_buffer.setItemText(2, QCoreApplication.translate("MainWindow", u"OFF", None))

    # retranslateUi

