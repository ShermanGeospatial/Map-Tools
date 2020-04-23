from PyQt5 import QtQuickWidgets, QtCore, QtGui, QtWidgets
from MainWindow import Ui_MainWindow
from MainWindowController import MainWindowUIClass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MainWindowUIClass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())