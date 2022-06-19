from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Experiment4_1_three(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment4_1_three, self).__init__()
        loadUi("./rsc/ui/experiment4.1_length_tension_three.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.pushButtonBackToGraph.clicked.connect(self.goBack)
        self.pushButtonRevealAnswer.clicked.connect(self.showAnswer)
        self.pushButtonAnswerQuestion1.clicked.connect(self.answer1)
        self.progressBar.setValue(int(300/7))

    def answer1(self):
        n = int(self.lineEditQuestion1.text())
        if (n >= 3 and n <= 8):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct!")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "Incorrect!")

    def showAnswer(self):
        QtWidgets.QMessageBox.about(self, "Answer", "The muscle is now under tension in the resting state. This is due to the elastic properties of the muscle. It resists stretch, rather like a rubber band. This “resting tension” does not involve cross-bridge cycling.")

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)