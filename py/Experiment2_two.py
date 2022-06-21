from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Experiment2_two(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment2_two, self).__init__()
        loadUi("./rsc/ui/experiment2_muscle_twitch_two.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.horizontalSlider.valueChanged.connect(self.valueChange)
        self.horizontalSlider_2.valueChanged.connect(self.valueChange)
        self.labelDifference.setText("")
        self.pushButtonAnswerQuestion1.clicked.connect(self.answerQuestionOne)
        self.progressBar.setValue(int(200/5))
        
    def answerQuestionOne(self):
        x = float(self.lineEditQuestion1.text())
        if (x >= 114 and x <= 118):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct!")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "Incorrect! The time is measured between the start of the contraction and the return to the baseline.")

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