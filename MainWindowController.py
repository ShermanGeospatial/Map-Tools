from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets, QtPositioning
from PyQt5.QtCore import QObject, pyqtSlot, Qt
from MainWindow import Ui_MainWindow
import sys, os
from surveymodel import SurveyModel, Job

class MainWindowUIClass( Ui_MainWindow ):
    def __init__(self):

        super().__init__()
        self.jobDict = dict()
        self.currentJob = Job()

    def setupUi(self, MW):

        super().setupUi( MW )
        self.jobListWidget.clicked.connect(self.jobListClicked)

        qml_path = os.path.join(os.path.dirname(__file__), "map.qml")
        self.quickWidget.setSource(QtCore.QUrl.fromLocalFile(qml_path))

    def debugPrint( self, msg ):

        self.debugTextBrowser.append( msg )

    def newJobSlot(self):

        jobName = self.newJobLineEdit.text()

        if not (jobName == ''):

            self.currentJob = Job(jobName)
            self.jobDict[jobName] = self.currentJob
            self.jobListWidget.addItem(jobName)
            self.refreshNewJob()

    def jobNameSlot(self):

        jobName = self.newJobLineEdit.text()

        if not (jobName == ''):

            self.currentJob = Job(jobName)
            self.jobDict[jobName] = self.currentJob
            self.jobListWidget.addItem(jobName)
            self.refreshNewJob()

    def refreshNewJob(self):

        self.newJobLineEdit.setText('')

    def jobListClicked(self):

        self.currentJob = self.jobDict[self.jobListWidget.currentItem().text()]
        self.currentJobListWidget.clear()
        self.currentJobListWidget.addItems(self.currentJob.fileNameList)

        self.currentJob.getPointTable()

    def loadFileSlot(self):
  
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "All Files (*);;Python Files (*.py)",
                        options=options)
        if fileName:
            self.currentJob.addFileName( fileName )
            self.currentJobListWidget.addItem(fileName)
            self.pointsTableView.setModel(self.currentJob.getPointTable())            
            self.refreshCurrentJob()

    def dataFilenameSlot(self):

        fileName =  self.loadFileLineEdit.text()

        if self.currentJob.isValid( fileName ):
            self.currentJob.addFileName( self.loadFileLineEdit.text() )
            self.currentJobListWidget.addItem(fileName)
            self.pointsTableView.setModel(self.currentJob.getPointTable())
            self.refreshCurrentJob()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name!\n" + fileName )
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.loadFileLineEdit.setText( "" )
            self.refreshCurrentJob()
            self.debugPrint( "Invalid file specified: " + fileName  )

    def refreshCurrentJob(self):

        self.loadFileLineEdit.setText(self.currentJob.getFileName())

    def newSetSlot(self):

        print("newSetSlot")

    def loadSetSlot(self):

        print("loadSetSlot")

    def saveSetSlot(self):

        print("saveSetSlot")

