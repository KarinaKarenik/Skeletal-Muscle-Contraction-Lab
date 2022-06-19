from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Experiment2_five(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment2_five, self).__init__()
        loadUi("./rsc/ui/experiment2_muscle_twitch_five.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(500/5))

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)