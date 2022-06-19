from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import pyqtgraph as pg
import windows


class Experiment3_three(QtWidgets.QMainWindow):
    def __init__(self):
        super(Experiment3_three, self).__init__()
        loadUi("./rsc/ui/experiment3_tetanus_three.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(300/5))
        self.pushButtonAnswerQuestion1.clicked.connect(self.question1)
        self.pushButtonAnswerQuestion2.clicked.connect(self.question2)
        self.pushButtonAnswerQuestion3.clicked.connect(self.question3)
    
    def question1(self):
        inp = int(self.lineEditQuestion1.text())
        if (inp==7):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct! Well done!")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "No! Go back and make some more observations. What is the lowest frequency at which tension fails to return to the baseline between contractions?")

    def question2(self):
        inp = int(self.lineEditQuestion2.text())
        if (inp>= 11 and inp<= 13):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct! The duration of a twitch is too short to allow full activation of the contractile machinery of the muscle. Repetitive stimulation allows a longer period of activation. This gives a larger contraction.")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "No! Go back and make some more observations. What is the lowest frequency at which the peak tension increases above the value seen when stimulating at 1 per second? ")

    def question3(self):
        inp = int(self.lineEditQuestion3.text())
        if (inp>= 30 and inp<= 32):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct!")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "No! The correct answer is about 30/sec. During tetanus the contractile machinery is fully activated and the muscle is giving the largest possible contraction under these conditions")


    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)