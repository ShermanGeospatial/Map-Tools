# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 516)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.leftTabWidget = QtWidgets.QTabWidget(self.splitter)
        self.leftTabWidget.setObjectName("leftTabWidget")
        self.jobsTab = QtWidgets.QWidget()
        self.jobsTab.setMinimumSize(QtCore.QSize(123, 0))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.jobsTab.setFont(font)
        self.jobsTab.setMouseTracking(False)
        self.jobsTab.setTabletTracking(False)
        self.jobsTab.setAcceptDrops(False)
        self.jobsTab.setObjectName("jobsTab")
        self.splitter_3 = QtWidgets.QSplitter(self.jobsTab)
        self.splitter_3.setGeometry(QtCore.QRect(10, 10, 301, 431))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.jobListFrame = QtWidgets.QFrame(self.splitter_3)
        self.jobListFrame.setObjectName("jobListFrame")
        self.widget = QtWidgets.QWidget(self.jobListFrame)
        self.widget.setGeometry(QtCore.QRect(11, 11, 258, 171))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.newJobButton = QtWidgets.QPushButton(self.widget)
        self.newJobButton.setObjectName("newJobButton")
        self.horizontalLayout_2.addWidget(self.newJobButton)
        self.newJobLineEdit = QtWidgets.QLineEdit(self.widget)
        self.newJobLineEdit.setObjectName("newJobLineEdit")
        self.horizontalLayout_2.addWidget(self.newJobLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        self.jobListWidget = QtWidgets.QListWidget(self.widget)
        self.jobListWidget.setObjectName("jobListWidget")
        self.gridLayout.addWidget(self.jobListWidget, 1, 0, 1, 1)
        self.currentJobWidget = QtWidgets.QWidget(self.splitter_3)
        self.currentJobWidget.setObjectName("currentJobWidget")
        self.widget1 = QtWidgets.QWidget(self.currentJobWidget)
        self.widget1.setGeometry(QtCore.QRect(10, 10, 258, 181))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.loadFileButton = QtWidgets.QPushButton(self.widget1)
        self.loadFileButton.setObjectName("loadFileButton")
        self.horizontalLayout_3.addWidget(self.loadFileButton)
        self.loadFileLineEdit = QtWidgets.QLineEdit(self.widget1)
        self.loadFileLineEdit.setObjectName("loadFileLineEdit")
        self.horizontalLayout_3.addWidget(self.loadFileLineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.currentJobListWidget = QtWidgets.QListWidget(self.widget1)
        self.currentJobListWidget.setObjectName("currentJobListWidget")
        self.verticalLayout_2.addWidget(self.currentJobListWidget)
        self.leftTabWidget.addTab(self.jobsTab, "")
        self.setsTab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setPointSize(8)
        self.setsTab.setFont(font)
        self.setsTab.setObjectName("setsTab")
        self.splitter_2 = QtWidgets.QSplitter(self.setsTab)
        self.splitter_2.setGeometry(QtCore.QRect(0, 1, 258, 416))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.widget2 = QtWidgets.QWidget(self.splitter_2)
        self.widget2.setObjectName("widget2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.widget2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.setTableWidget = QtWidgets.QTableWidget(self.widget2)
        self.setTableWidget.setObjectName("setTableWidget")
        self.setTableWidget.setColumnCount(0)
        self.setTableWidget.setRowCount(0)
        self.verticalLayout.addWidget(self.setTableWidget)
        self.setTextEdit = QtWidgets.QTextEdit(self.splitter_2)
        self.setTextEdit.setObjectName("setTextEdit")
        self.leftTabWidget.addTab(self.setsTab, "")
        self.pointsTab = QtWidgets.QWidget()
        self.pointsTab.setObjectName("pointsTab")
        self.pointsTableView = QtWidgets.QTableView(self.pointsTab)
        self.pointsTableView.setGeometry(QtCore.QRect(10, 10, 271, 431))
        self.pointsTableView.setObjectName("pointsTableView")
        self.leftTabWidget.addTab(self.pointsTab, "")
        self.quickWidget = QtQuickWidgets.QQuickWidget(self.splitter)
        self.quickWidget.setResizeMode(QtQuickWidgets.QQuickWidget.SizeRootObjectToView)
        self.quickWidget.setObjectName("quickWidget")
        self.rightToolBox = QtWidgets.QToolBox(self.splitter)
        self.rightToolBox.setObjectName("rightToolBox")
        self.rightToolBoxPage1 = QtWidgets.QWidget()
        self.rightToolBoxPage1.setObjectName("rightToolBoxPage1")
        self.rightToolBox.addItem(self.rightToolBoxPage1, "")
        self.rightToolBoxPage2 = QtWidgets.QWidget()
        self.rightToolBoxPage2.setObjectName("rightToolBoxPage2")
        self.rightToolBox.addItem(self.rightToolBoxPage2, "")
        self.rightToolBoxPage3 = QtWidgets.QWidget()
        self.rightToolBoxPage3.setObjectName("rightToolBoxPage3")
        self.rightToolBox.addItem(self.rightToolBoxPage3, "")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 911, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.leftTabWidget.setCurrentIndex(2)
        self.newJobButton.clicked.connect(self.newJobSlot)
        self.newJobLineEdit.returnPressed.connect(self.jobNameSlot)
        self.loadFileButton.clicked.connect(self.loadFileSlot)
        self.loadFileLineEdit.returnPressed.connect(self.dataFilenameSlot)
        self.pushButton.clicked.connect(self.newSetSlot)
        self.pushButton_2.clicked.connect(self.loadSetSlot)
        self.pushButton_3.clicked.connect(self.saveSetSlot)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newJobButton.setText(_translate("MainWindow", "New"))
        self.loadFileButton.setText(_translate("MainWindow", "Load"))
        self.leftTabWidget.setTabText(self.leftTabWidget.indexOf(self.jobsTab), _translate("MainWindow", "Jobs"))
        self.pushButton.setText(_translate("MainWindow", "New"))
        self.pushButton_2.setText(_translate("MainWindow", "Load"))
        self.pushButton_3.setText(_translate("MainWindow", "Save"))
        self.leftTabWidget.setTabText(self.leftTabWidget.indexOf(self.setsTab), _translate("MainWindow", "Sets"))
        self.leftTabWidget.setTabText(self.leftTabWidget.indexOf(self.pointsTab), _translate("MainWindow", "Points"))
        self.rightToolBox.setItemText(self.rightToolBox.indexOf(self.rightToolBoxPage1), _translate("MainWindow", "COGO"))
        self.rightToolBox.setItemText(self.rightToolBox.indexOf(self.rightToolBoxPage2), _translate("MainWindow", "Point Manipulation"))
        self.rightToolBox.setItemText(self.rightToolBox.indexOf(self.rightToolBoxPage3), _translate("MainWindow", "Point/Observation Editor"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))

from PyQt5 import QtQuickWidgets

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

