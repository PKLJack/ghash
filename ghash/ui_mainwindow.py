# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.4.1
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTableView, QVBoxLayout, QWidget)

from .dnd_label import DNDLabel

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        MainWindow.setMinimumSize(QSize(600, 400))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.groupbox_sha = QGroupBox(self.centralwidget)
        self.groupbox_sha.setObjectName(u"groupbox_sha")
        self.verticalLayout = QVBoxLayout(self.groupbox_sha)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.checkbox_sha1 = QCheckBox(self.groupbox_sha)
        self.checkbox_sha1.setObjectName(u"checkbox_sha1")

        self.verticalLayout.addWidget(self.checkbox_sha1)

        self.checkbox_sha224 = QCheckBox(self.groupbox_sha)
        self.checkbox_sha224.setObjectName(u"checkbox_sha224")

        self.verticalLayout.addWidget(self.checkbox_sha224)

        self.checkbox_sha256 = QCheckBox(self.groupbox_sha)
        self.checkbox_sha256.setObjectName(u"checkbox_sha256")

        self.verticalLayout.addWidget(self.checkbox_sha256)

        self.checkbox_sha384 = QCheckBox(self.groupbox_sha)
        self.checkbox_sha384.setObjectName(u"checkbox_sha384")

        self.verticalLayout.addWidget(self.checkbox_sha384)

        self.checkbox_sha512 = QCheckBox(self.groupbox_sha)
        self.checkbox_sha512.setObjectName(u"checkbox_sha512")

        self.verticalLayout.addWidget(self.checkbox_sha512)


        self.horizontalLayout_3.addWidget(self.groupbox_sha)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.groupbox_others = QGroupBox(self.centralwidget)
        self.groupbox_others.setObjectName(u"groupbox_others")
        self.verticalLayout_2 = QVBoxLayout(self.groupbox_others)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkbox_md5 = QCheckBox(self.groupbox_others)
        self.checkbox_md5.setObjectName(u"checkbox_md5")

        self.verticalLayout_2.addWidget(self.checkbox_md5)

        self.checkbox_crc32 = QCheckBox(self.groupbox_others)
        self.checkbox_crc32.setObjectName(u"checkbox_crc32")

        self.verticalLayout_2.addWidget(self.checkbox_crc32)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addWidget(self.groupbox_others)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout_3.addWidget(self.line_2)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_drag_and_drop = DNDLabel(self.widget)
        self.label_drag_and_drop.setObjectName(u"label_drag_and_drop")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_drag_and_drop.sizePolicy().hasHeightForWidth())
        self.label_drag_and_drop.setSizePolicy(sizePolicy)
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_drag_and_drop.setFont(font)
        self.label_drag_and_drop.setAcceptDrops(True)
        self.label_drag_and_drop.setAlignment(Qt.AlignCenter)
        self.label_drag_and_drop.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.label_drag_and_drop)

        self.button_choose_files = QPushButton(self.widget)
        self.button_choose_files.setObjectName(u"button_choose_files")

        self.verticalLayout_3.addWidget(self.button_choose_files)


        self.horizontalLayout_3.addWidget(self.widget)

        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(6, 2)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line)

        self.tab_widget = QTabWidget(self.centralwidget)
        self.tab_widget.setObjectName(u"tab_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(1)
        sizePolicy1.setHeightForWidth(self.tab_widget.sizePolicy().hasHeightForWidth())
        self.tab_widget.setSizePolicy(sizePolicy1)
        self.tab_all = QWidget()
        self.tab_all.setObjectName(u"tab_all")
        self.horizontalLayout = QHBoxLayout(self.tab_all)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.table_view_all = QTableView(self.tab_all)
        self.table_view_all.setObjectName(u"table_view_all")

        self.horizontalLayout.addWidget(self.table_view_all)

        self.tab_widget.addTab(self.tab_all, "")
        self.tab_others = QWidget()
        self.tab_others.setObjectName(u"tab_others")
        self.horizontalLayout_4 = QHBoxLayout(self.tab_others)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.table_view_others = QTableView(self.tab_others)
        self.table_view_others.setObjectName(u"table_view_others")

        self.horizontalLayout_4.addWidget(self.table_view_others)

        self.tab_widget.addTab(self.tab_others, "")

        self.verticalLayout_4.addWidget(self.tab_widget)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.button_calculate = QPushButton(self.centralwidget)
        self.button_calculate.setObjectName(u"button_calculate")

        self.horizontalLayout_2.addWidget(self.button_calculate)

        self.button_clear = QPushButton(self.centralwidget)
        self.button_clear.setObjectName(u"button_clear")

        self.horizontalLayout_2.addWidget(self.button_clear)

        self.button_copy_json = QPushButton(self.centralwidget)
        self.button_copy_json.setObjectName(u"button_copy_json")

        self.horizontalLayout_2.addWidget(self.button_copy_json)

        self.button_copy_tsv = QPushButton(self.centralwidget)
        self.button_copy_tsv.setObjectName(u"button_copy_tsv")

        self.horizontalLayout_2.addWidget(self.button_copy_tsv)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tab_widget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GHash", None))
        self.groupbox_sha.setTitle(QCoreApplication.translate("MainWindow", u"SHA", None))
        self.checkbox_sha1.setText(QCoreApplication.translate("MainWindow", u"sha1sum", None))
        self.checkbox_sha224.setText(QCoreApplication.translate("MainWindow", u"sha224sum", None))
        self.checkbox_sha256.setText(QCoreApplication.translate("MainWindow", u"sha256sum", None))
        self.checkbox_sha384.setText(QCoreApplication.translate("MainWindow", u"sha384sum", None))
        self.checkbox_sha512.setText(QCoreApplication.translate("MainWindow", u"sha512sum", None))
        self.groupbox_others.setTitle(QCoreApplication.translate("MainWindow", u"Others", None))
        self.checkbox_md5.setText(QCoreApplication.translate("MainWindow", u"md5", None))
        self.checkbox_crc32.setText(QCoreApplication.translate("MainWindow", u"crc32", None))
        self.label_drag_and_drop.setText(QCoreApplication.translate("MainWindow", u"Drag & Drop Files", None))
        self.button_choose_files.setText(QCoreApplication.translate("MainWindow", u"Choose Files", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_all), QCoreApplication.translate("MainWindow", u"All", None))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.tab_others), QCoreApplication.translate("MainWindow", u"Others", None))
        self.button_calculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.button_clear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.button_copy_json.setText(QCoreApplication.translate("MainWindow", u"Copy (JSON)", None))
        self.button_copy_tsv.setText(QCoreApplication.translate("MainWindow", u"Copy (TSV)", None))
    # retranslateUi

