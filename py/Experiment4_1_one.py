from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Experiment4_1_one(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment4_1_one, self).__init__()
        loadUi("./rsc/ui/experiment4.1_length_tension_one.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(100/7))

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)