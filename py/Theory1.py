from PyQt5 import QtWidgets, QtGui
from PyQt5.uic import loadUi
import windows

class Theory1(QtWidgets.QMainWindow):

    def __init__(self):
        super(Theory1, self).__init__()
        loadUi("./rsc/ui/theory1_introduction.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(100/4))
        self.textBrowser.setTextColor(QtGui.QColor(0, 0, 0, 255))

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)