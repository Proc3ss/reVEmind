# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'revemind.ui'
#
# Created: Sun Apr 06 18:32:32 2014
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_EveAnalyze(object):
    def setupUi(self, EveAnalyze):
        EveAnalyze.setObjectName(_fromUtf8("reVEmind"))
        EveAnalyze.resize(1102, 757)
        EveAnalyze.setMinimumSize(QtCore.QSize(1054, 757))
        self.centralwidget = QtGui.QWidget(EveAnalyze)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.frame = QtGui.QFrame(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(4)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.logCalendar = QtGui.QCalendarWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logCalendar.sizePolicy().hasHeightForWidth())
        self.logCalendar.setSizePolicy(sizePolicy)
        self.logCalendar.setMinimumSize(QtCore.QSize(290, 201))
        self.logCalendar.setMaximumSize(QtCore.QSize(350, 229))
        self.logCalendar.setAutoFillBackground(False)
        self.logCalendar.setGridVisible(True)
        self.logCalendar.setHorizontalHeaderFormat(QtGui.QCalendarWidget.SingleLetterDayNames)
        self.logCalendar.setVerticalHeaderFormat(QtGui.QCalendarWidget.NoVerticalHeader)
        self.logCalendar.setNavigationBarVisible(True)
        self.logCalendar.setDateEditEnabled(True)
        self.logCalendar.setObjectName(_fromUtf8("logCalendar"))
        self.verticalLayout.addWidget(self.logCalendar)
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.verticalLayout.addWidget(self.pushButton)
        self.logfileList = QtGui.QListWidget(self.frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logfileList.sizePolicy().hasHeightForWidth())
        self.logfileList.setSizePolicy(sizePolicy)
        self.logfileList.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.logfileList.setObjectName(_fromUtf8("logfileList"))
        self.verticalLayout.addWidget(self.logfileList)
        self.horizontalLayout_2.addWidget(self.frame)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.splitter_3 = QtGui.QSplitter(self.centralwidget)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName(_fromUtf8("splitter_3"))
        self.splitter_2 = QtGui.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.layoutWidget = QtGui.QWidget(self.splitter_2)
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.loglineViewer = QtGui.QTableView(self.layoutWidget)
        self.loglineViewer.setEnabled(True)
        self.loglineViewer.setMinimumSize(QtCore.QSize(400, 0))
        self.loglineViewer.setObjectName(_fromUtf8("loglineViewer"))
        self.verticalLayout_5.addWidget(self.loglineViewer)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.dateTimeEdit = QtGui.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit.setObjectName(_fromUtf8("dateTimeEdit"))
        self.horizontalLayout.addWidget(self.dateTimeEdit)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.dateTimeEdit_2 = QtGui.QDateTimeEdit(self.layoutWidget)
        self.dateTimeEdit_2.setObjectName(_fromUtf8("dateTimeEdit_2"))
        self.horizontalLayout.addWidget(self.dateTimeEdit_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.splitter = QtGui.QSplitter(self.splitter_2)
        self.splitter.setMinimumSize(QtCore.QSize(340, 0))
        self.splitter.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.splitter.setAutoFillBackground(True)
        self.splitter.setFrameShape(QtGui.QFrame.StyledPanel)
        self.splitter.setFrameShadow(QtGui.QFrame.Raised)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.scrollArea = QtGui.QScrollArea(self.splitter)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 336, 374))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(self.scrollAreaWidgetContents_2)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 350))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.pilot_tab = QtGui.QWidget()
        self.pilot_tab.setObjectName(_fromUtf8("pilot_tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.pilot_tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.pilotStack = QtGui.QToolBox(self.pilot_tab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pilotStack.sizePolicy().hasHeightForWidth())
        self.pilotStack.setSizePolicy(sizePolicy)
        self.pilotStack.setObjectName(_fromUtf8("pilotStack"))
        self.pilotStack_page = QtGui.QWidget()
        self.pilotStack_page.setGeometry(QtCore.QRect(0, 0, 294, 291))
        self.pilotStack_page.setObjectName(_fromUtf8("pilotStack_page"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.pilotStack_page)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.pilotTable = QtGui.QTableWidget(self.pilotStack_page)
        self.pilotTable.setMaximumSize(QtCore.QSize(16777215, 220))
        self.pilotTable.setAutoFillBackground(True)
        self.pilotTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pilotTable.setAutoScroll(True)
        self.pilotTable.setAutoScrollMargin(12)
        self.pilotTable.setObjectName(_fromUtf8("pilotTable"))
        self.pilotTable.setColumnCount(3)
        self.pilotTable.setRowCount(5)
        item = QtGui.QTableWidgetItem()
        self.pilotTable.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.pilotTable.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.pilotTable.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.pilotTable.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.pilotTable.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(0, 85, 255, 100))
        self.pilotTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setBackground(QtGui.QColor(255, 0, 0, 100))
        self.pilotTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.pilotTable.setHorizontalHeaderItem(2, item)
        self.verticalLayout_3.addWidget(self.pilotTable)
        self.pilotStack.addItem(self.pilotStack_page, _fromUtf8(""))
        self.verticalLayout_4.addWidget(self.pilotStack)
        self.tabWidget.addTab(self.pilot_tab, _fromUtf8(""))
        self.weapon_tab = QtGui.QWidget()
        self.weapon_tab.setObjectName(_fromUtf8("weapon_tab"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.weapon_tab)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.WeaponStack = QtGui.QToolBox(self.weapon_tab)
        self.WeaponStack.setObjectName(_fromUtf8("WeaponStack"))
        self.page_7 = QtGui.QWidget()
        self.page_7.setGeometry(QtCore.QRect(0, 0, 93, 79))
        self.page_7.setObjectName(_fromUtf8("page_7"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.page_7)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.pushButton_3 = QtGui.QPushButton(self.page_7)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.verticalLayout_7.addWidget(self.pushButton_3)
        self.label_2 = QtGui.QLabel(self.page_7)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_7.addWidget(self.label_2)
        self.label = QtGui.QLabel(self.page_7)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_7.addWidget(self.label)
        self.WeaponStack.addItem(self.page_7, _fromUtf8(""))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 294, 258))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_12 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_12.setObjectName(_fromUtf8("verticalLayout_12"))
        self.WeaponStack.addItem(self.page, _fromUtf8(""))
        self.verticalLayout_10.addWidget(self.WeaponStack)
        self.tabWidget.addTab(self.weapon_tab, _fromUtf8(""))
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.listStats = QtGui.QListWidget(self.splitter)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listStats.sizePolicy().hasHeightForWidth())
        self.listStats.setSizePolicy(sizePolicy)
        self.listStats.setMaximumSize(QtCore.QSize(16777215, 100))
        self.listStats.setObjectName(_fromUtf8("listStats"))
        self.plot_widget = PlotWidget(self.splitter_3)
        self.plot_widget.setMinimumSize(QtCore.QSize(250, 208))
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        self.plot_widget.setForegroundBrush(brush)
        self.plot_widget.setObjectName(_fromUtf8("plot_widget"))
        self.verticalLayout_6.addWidget(self.splitter_3)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        EveAnalyze.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(EveAnalyze)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1102, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuActions = QtGui.QMenu(self.menubar)
        self.menuActions.setObjectName(_fromUtf8("menuActions"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        EveAnalyze.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(EveAnalyze)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        EveAnalyze.setStatusBar(self.statusbar)
        self.actionSelect_Folder = QtGui.QAction(EveAnalyze)
        self.actionSelect_Folder.setObjectName(_fromUtf8("actionSelect_Folder"))
        self.actionImport_All_Files = QtGui.QAction(EveAnalyze)
        self.actionImport_All_Files.setObjectName(_fromUtf8("actionImport_All_Files"))
        self.menuActions.addAction(self.actionImport_All_Files)
        self.menuFile.addAction(self.actionSelect_Folder)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())

        self.retranslateUi(EveAnalyze)
        self.tabWidget.setCurrentIndex(0)
        self.pilotStack.setCurrentIndex(0)
        self.pilotStack.layout().setSpacing(0)
        self.WeaponStack.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(EveAnalyze)

    def retranslateUi(self, EveAnalyze):
        EveAnalyze.setWindowTitle(QtGui.QApplication.translate("reVEmind", "reVEmind 0.1a", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("reVEmind", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        item = self.pilotTable.verticalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("reVEmind", "Total Dmg", None, QtGui.QApplication.UnicodeUTF8))
        item = self.pilotTable.verticalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("reVEmind", "Avg DPS", None, QtGui.QApplication.UnicodeUTF8))
        item = self.pilotTable.verticalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("reVEmind", "Total Hits", None, QtGui.QApplication.UnicodeUTF8))
        item = self.pilotTable.verticalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("reVEmind", "Best Hit", None, QtGui.QApplication.UnicodeUTF8))
        item = self.pilotTable.verticalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("reVEmind", "Hit Accy", None, QtGui.QApplication.UnicodeUTF8))
        item = self.pilotTable.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("reVEmind", "Dealt", None, QtGui.QApplication.UnicodeUTF8))
        item = self.pilotTable.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("reVEmind", "Received", None, QtGui.QApplication.UnicodeUTF8))
        self.pilotStack.setItemText(self.pilotStack.indexOf(self.pilotStack_page), QtGui.QApplication.translate("reVEmind", "Page", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pilot_tab), QtGui.QApplication.translate("reVEmind", "Pilot", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("reVEmind", "PushButton", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("reVEmind", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("reVEmind", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.WeaponStack.setItemText(self.WeaponStack.indexOf(self.page_7), QtGui.QApplication.translate("reVEmind", "Page 1", None, QtGui.QApplication.UnicodeUTF8))
        self.WeaponStack.setItemText(self.WeaponStack.indexOf(self.page), QtGui.QApplication.translate("reVEmind", "Page", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.weapon_tab), QtGui.QApplication.translate("reVEmind", "Weapon", None, QtGui.QApplication.UnicodeUTF8))
        self.menuActions.setTitle(QtGui.QApplication.translate("reVEmind", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("reVEmind", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSelect_Folder.setText(QtGui.QApplication.translate("reVEmind", "Select Folder", None, QtGui.QApplication.UnicodeUTF8))
        self.actionImport_All_Files.setText(QtGui.QApplication.translate("reVEmind", "Import All Files", None, QtGui.QApplication.UnicodeUTF8))

from pyqtgraph import PlotWidget
