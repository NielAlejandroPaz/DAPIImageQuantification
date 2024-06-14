# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dapiquantificationoTcJOt.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_DAPIQuantification(object):
    def setupUi(self, DAPIQuantification):
        if not DAPIQuantification.objectName():
            DAPIQuantification.setObjectName(u"DAPIQuantification")
        DAPIQuantification.setEnabled(True)
        DAPIQuantification.resize(1000, 630)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DAPIQuantification.sizePolicy().hasHeightForWidth())
        DAPIQuantification.setSizePolicy(sizePolicy)
        DAPIQuantification.setMinimumSize(QSize(1000, 630))
        DAPIQuantification.setMaximumSize(QSize(1000, 630))
        self.centralwidget = QWidget(DAPIQuantification)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 70, 981, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.directoryLabel = QLabel(self.horizontalLayoutWidget)
        self.directoryLabel.setObjectName(u"directoryLabel")
        font = QFont()
        font.setFamily(u"Yu Gothic UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.directoryLabel.setFont(font)

        self.horizontalLayout_3.addWidget(self.directoryLabel)

        self.directoryLineEdit = QLineEdit(self.horizontalLayoutWidget)
        self.directoryLineEdit.setObjectName(u"directoryLineEdit")

        self.horizontalLayout_3.addWidget(self.directoryLineEdit)

        self.directoryPushbutton = QPushButton(self.horizontalLayoutWidget)
        self.directoryPushbutton.setObjectName(u"directoryPushbutton")
        self.directoryPushbutton.setFont(font)

        self.horizontalLayout_3.addWidget(self.directoryPushbutton)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Minimum, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 210, 711, 331))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.resultsTableWidget = QTableWidget(self.horizontalLayoutWidget_2)
        if (self.resultsTableWidget.columnCount() < 2):
            self.resultsTableWidget.setColumnCount(2)
        font1 = QFont()
        font1.setFamily(u"Yu Gothic UI Light")
        font1.setPointSize(14)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.resultsTableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.resultsTableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.resultsTableWidget.setObjectName(u"resultsTableWidget")
        font2 = QFont()
        font2.setFamily(u"Yu Gothic UI Light")
        font2.setPointSize(12)
        self.resultsTableWidget.setFont(font2)
        self.resultsTableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.resultsTableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.resultsTableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.resultsTableWidget.horizontalHeader().setMinimumSectionSize(39)
        self.resultsTableWidget.horizontalHeader().setDefaultSectionSize(330)
        self.resultsTableWidget.horizontalHeader().setStretchLastSection(True)
        self.resultsTableWidget.verticalHeader().setVisible(False)
        self.resultsTableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.resultsTableWidget.verticalHeader().setMinimumSectionSize(12)
        self.resultsTableWidget.verticalHeader().setDefaultSectionSize(35)

        self.horizontalLayout_4.addWidget(self.resultsTableWidget)

        self.horizontalLayoutWidget_3 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 10, 981, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.title = QLabel(self.horizontalLayoutWidget_3)
        self.title.setObjectName(u"title")
        font3 = QFont()
        font3.setFamily(u"Yu Gothic UI Semibold")
        font3.setPointSize(20)
        font3.setBold(True)
        font3.setWeight(75)
        self.title.setFont(font3)

        self.horizontalLayout.addWidget(self.title)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayoutWidget_4 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(10, 550, 981, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)

        self.exportPushButton = QPushButton(self.horizontalLayoutWidget_4)
        self.exportPushButton.setObjectName(u"exportPushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.exportPushButton.sizePolicy().hasHeightForWidth())
        self.exportPushButton.setSizePolicy(sizePolicy1)
        self.exportPushButton.setFont(font)

        self.horizontalLayout_2.addWidget(self.exportPushButton)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_6)

        self.horizontalLayoutWidget_5 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(10, 130, 981, 41))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.runPushButton = QPushButton(self.horizontalLayoutWidget_5)
        self.runPushButton.setObjectName(u"runPushButton")
        sizePolicy1.setHeightForWidth(self.runPushButton.sizePolicy().hasHeightForWidth())
        self.runPushButton.setSizePolicy(sizePolicy1)
        self.runPushButton.setFont(font)

        self.horizontalLayout_5.addWidget(self.runPushButton)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_9)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(17, 180, 971, 23))
        self.progressBar.setValue(24)
        self.imageLabel = QLabel(self.centralwidget)
        self.imageLabel.setObjectName(u"imageLabel")
        self.imageLabel.setGeometry(QRect(730, 210, 261, 321))
        self.imageLabel.setAlignment(Qt.AlignCenter)
        DAPIQuantification.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(DAPIQuantification)
        self.statusbar.setObjectName(u"statusbar")
        DAPIQuantification.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.directoryLineEdit, self.directoryPushbutton)
        QWidget.setTabOrder(self.directoryPushbutton, self.runPushButton)
        QWidget.setTabOrder(self.runPushButton, self.resultsTableWidget)
        QWidget.setTabOrder(self.resultsTableWidget, self.exportPushButton)

        self.retranslateUi(DAPIQuantification)
        self.directoryPushbutton.clicked.connect(DAPIQuantification.searchClicked)
        self.runPushButton.clicked.connect(DAPIQuantification.calculateClicked)
        self.exportPushButton.clicked.connect(DAPIQuantification.exportClicked)
        self.resultsTableWidget.cellDoubleClicked.connect(DAPIQuantification.selectionChanged)

        QMetaObject.connectSlotsByName(DAPIQuantification)
    # setupUi

    def retranslateUi(self, DAPIQuantification):
        DAPIQuantification.setWindowTitle(QCoreApplication.translate("DAPIQuantification", u"DAPIQuantification", None))
        self.directoryLabel.setText(QCoreApplication.translate("DAPIQuantification", u"Image Directory", None))
        self.directoryLineEdit.setPlaceholderText("")
        self.directoryPushbutton.setText(QCoreApplication.translate("DAPIQuantification", u"Search", None))
        ___qtablewidgetitem = self.resultsTableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("DAPIQuantification", u"Image Name", None));
        ___qtablewidgetitem1 = self.resultsTableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("DAPIQuantification", u"Percentage", None));
        self.title.setText(QCoreApplication.translate("DAPIQuantification", u"DAPI IMAGE QUANTIFICATION", None))
        self.exportPushButton.setText(QCoreApplication.translate("DAPIQuantification", u"Export", None))
        self.runPushButton.setText(QCoreApplication.translate("DAPIQuantification", u"Calculate", None))
        self.imageLabel.setText(QCoreApplication.translate("DAPIQuantification", u"No Image", None))
    # retranslateUi

