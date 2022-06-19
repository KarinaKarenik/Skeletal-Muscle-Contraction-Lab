from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import pyqtgraph as pg
import windows


class Experiment3_four(QtWidgets.QMainWindow):
    def __init__(self):
        super(Experiment3_four, self).__init__()
        loadUi("./rsc/ui/experiment3_tetanus_four.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(400/5))
        self.pushButtonAnswerQuestion4.clicked.connect(self.question4)
        self.pushButtonAnswerQuestion5.clicked.connect(self.question5)
    
    def question4(self):
        inp = int(self.lineEditQuestion4.text())
        if (inp==308):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct! Well done!")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "No! Go back and stimulate with higher frequency.")

    def question5(self):
        if (self.radioButton_2.isChecked()):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct answer. The muscle membrane displays action potentials at the same frequency as the nerve, summation and tetanus occur only within the contractile machinery of the muscle. The image shows simultaneous recording of muscle action potentials and tetanus at a frequency of / sec.")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "Incorrect!")

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)