from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Theory4(QtWidgets.QMainWindow):

    def __init__(self):
        super(Theory4, self).__init__()
        loadUi("./rsc/ui/theory4_setup_two.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(400/4))
    
    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)