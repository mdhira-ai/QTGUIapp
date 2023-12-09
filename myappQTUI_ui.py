# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'myappQTUI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(400, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Segoe Fluent Icons"])
        font.setPointSize(13)
        Dialog.setFont(font)
        Dialog.setContextMenuPolicy(Qt.DefaultContextMenu)
        Dialog.setAcceptDrops(False)
        Dialog.setAutoFillBackground(True)
        Dialog.setStyleSheet(u"background-color: rgb(18, 18, 18);")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 20, 161, 41))
        self.pushButton.setContextMenuPolicy(Qt.NoContextMenu)
        self.pushButton.setStyleSheet(u"background-color:'#1E1E1E';\n"
"color: rgb(255, 255, 255);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 70, 271, 41))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setScaledContents(False)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"myapp", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Start", None))
        self.label.setText("")
    # retranslateUi

