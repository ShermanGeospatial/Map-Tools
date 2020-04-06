# surveytools.py
# D. Sherman
# PyQt5 Application
# A basic interface for displaying survey data over a map based upon an MVC design pattern

from PyQt5 import QtCore, QtGui, QtWidgets, QtQuickWidgets, QtPositioning
from PyQt5.QtCore import QObject, pyqtSlot, Qt
from surveymainwindow import Ui_MainWindow
import sys, os
from surveymodel import SurveyModel

class MainWindowUIClass( Ui_MainWindow ):
    def __init__( self ):

        super().__init__()
        self.surveymodel = SurveyModel()

    def setupUi( self, MW ):

        super().setupUi( MW )
        self.listWidget.clicked.connect(self.listClicked)

        qml_path = os.path.join(os.path.dirname(__file__), "map.qml")
        self.quickWidget.setSource(QtCore.QUrl.fromLocalFile(qml_path))

    def debugPrint( self, msg ):

        self.debugTextBrowser.append( msg )

    def refreshAll( self ):

        self.lineEdit.setText( self.surveymodel.getFileName() )
    
    # slot
    def returnPressedSlot( self ):

        fileName =  self.lineEdit.text()
        if self.surveymodel.isValid( fileName ):
            self.surveymodel.setFileName( self.lineEdit.text() )
            self.fillScrollArea()
            self.refreshAll()
        else:
            m = QtWidgets.QMessageBox()
            m.setText("Invalid file name!\n" + fileName )
            m.setIcon(QtWidgets.QMessageBox.Warning)
            m.setStandardButtons(QtWidgets.QMessageBox.Ok
                                 | QtWidgets.QMessageBox.Cancel)
            m.setDefaultButton(QtWidgets.QMessageBox.Cancel)
            ret = m.exec_()
            self.lineEdit.setText( "" )
            self.refreshAll()
            self.debugPrint( "Invalid file specified: " + fileName  )
        
    # slot
    def browseSlot( self ):

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(
                        None,
                        "QFileDialog.getOpenFileName()",
                        "",
                        "All Files (*);;Python Files (*.py)",
                        options=options)
        if fileName:
            self.surveymodel.setFileName( fileName )
            self.fillScrollArea()
            self.refreshAll()

    def fillScrollArea(self):


        for point in self.surveymodel.getSurveyData():

            labelObject = QtWidgets.QLabel(point.getPointString())
            self.listWidget.addItem(point.getPointString())

    def listClicked(self):

        print(self.listWidget.currentItem().text())

def main():

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

main()