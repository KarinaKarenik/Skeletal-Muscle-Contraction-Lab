from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Explanation1Dialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(Explanation1Dialog, self).__init__(parent)
        loadUi("./rsc/ui/experiment1_q1_explanation.ui",self)

class Experiment1_one(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment1_one, self).__init__()
        loadUi("./rsc/ui/experiment1_nerve_treshold_one.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(100/5))
        self.pushButtonShowExplanation.clicked.connect(self.showExplanationPopup)
        self.pushButtonAnswer.clicked.connect(self.answerQuestion)
    

    def answerQuestion(self):
        one = self.checkBox.isChecked()
        two = self.checkBox2.isChecked()
        three = self.checkBox3.isChecked()
        if (one and two and three):
            QtWidgets.QMessageBox.about(self, "Correct!", "All are correct!")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "Incorrect!")

    def showExplanationPopup(self):
        dialog = Explanation1Dialog(self)
        dialog.setWindowTitle("Explanation")
        dialog.exec()

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)