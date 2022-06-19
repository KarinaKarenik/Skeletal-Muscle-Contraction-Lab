from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Experiment2_four(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment2_four, self).__init__()
        loadUi("./rsc/ui/experiment2_muscle_twitch_four.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(400/5))
        self.pushButtonAnswerQuestion1.clicked.connect(self.answerQuestionOne)
        self.pushButtonAnswerQuestion2.clicked.connect(self.answerQuestionTwo)

    def answerQuestionOne(self):
        x = float(self.lineEditQuestion1.text())
        if (x >= 1 and x <= 2):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct! The time is measured between the start of the stimulus and the beginning of the deflection of the action potential from the baseline. This time is taken up by the action potential traveling down the nerve, the synaptic delay, and the action potential traveling down the muscle to the electrode at the end. The total distance traveled is about 5 cm.")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "Incorrect! The time is measured between the start of the stimulus and the beginning of the deflection of the action potential from the baseline. This time is taken up by the action potential traveling down the nerve, the synaptic delay, and the action potential traveling down the muscle to the electrode at the end. The total distance traveled is about 5 cm.")

    def answerQuestionTwo(self):
        x = float(self.lineEditQuestion2.text())
        if (x >= 5 and x <= 6):
             QtWidgets.QMessageBox.about(self, "Correct!", "Correct! The time is measured between the start of the action potential and the start of the muscle contraction.")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "Incorrect! The time is measured between the start of the action potential and the start of the muscle contraction..")

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)