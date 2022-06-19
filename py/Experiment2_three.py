from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Experiment2_three(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment2_three, self).__init__()
        loadUi("./rsc/ui/experiment2_muscle_twitch_three.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.horizontalSlider.valueChanged.connect(self.valueChange)
        self.horizontalSlider_2.valueChanged.connect(self.valueChange)
        self.labelDifference.setText("")
        self.progressBar.setValue(int(300/5))
    
    def valueChange(self):
        a = self.horizontalSlider.value()
        b = self.horizontalSlider_2.value()
        diff = abs(a-b)
        self.labelDifference.setText(str(diff) + " msec.")
    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)