from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Experiment4_conclussions(QtWidgets.QMainWindow):
    def __init__(self):
        super(Experiment4_conclussions, self).__init__()
        loadUi("./rsc/ui/experiment4_conclussions.ui",self)
        self.pushButtonMenu_2.clicked.connect(self.goToMenu)
        self.pushButtonBack_2.clicked.connect(self.goBack)
        self.pushButtonNext_2.clicked.connect(self.goNext)
        self.progressBar.setValue(int(700/7))

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)