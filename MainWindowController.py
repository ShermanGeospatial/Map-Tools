from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets, QtPositioning
from PyQt5.QtCore import QObject, pyqtSlot, Qt
from MainWindow import Ui_MainWindow
import sys, os
from surveymodel import SurveyModel, Job

class MainWindowUIClass( Ui_MainWindow ):
    def __init__( self ):

        super().__init__()
        self.surveymodel = SurveyModel()
        self.jobList = list()

    def setupUi( self, MW ):

        super().setupUi( MW )

        qml_path = os.path.join(os.path.dirname(__file__), "map.qml")
        self.quickWidget.setSource(QtCore.QUrl.fromLocalFile(qml_path))

    def newJobSlot(self):

        jobName = self.newJobLineEdit.text()

        if not (jobName == ''):

            self.jobList.append(Job(jobName))
            
            self.jobListWidget.addItem(jobName)


    def jobNameSlot(self):

        jobName = self.newJobLineEdit.text()

        if not (jobName == ''):

            self.jobList.append(Job(jobName))
            
            self.jobListWidget.addItem(jobName)

    def loadFileSlot(self):

        print("loadFileSlot")

    def dataFilenameSlot(self):

        print("dataFilenameSlot")

    def newSetSlot(self):

        print("newSetSlot")

    def loadSetSlot(self):

        print("loadSetSlot")

    def saveSetSlot(self):

        print("saveSetSlot")

