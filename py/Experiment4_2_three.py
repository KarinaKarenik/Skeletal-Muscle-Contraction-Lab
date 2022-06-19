from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows


class ExplanationDialog(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(ExplanationDialog, self).__init__(parent)
        loadUi("./rsc/ui/experiment4.2_explanation.ui",self)

class Experiment4_2_three(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment4_2_three, self).__init__()
        loadUi("./rsc/ui/experiment4.2_length_tension_three.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.pushButtonOk.clicked.connect(self.answer)

        self.progressBar.setValue(int(600/7))

    def answer(self):
        one = self.checkBox1.isChecked()
        two = self.checkBox2.isChecked()
        three = self.checkBox3.isChecked()

        if (one and two and three):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct!")
        else:
            dialog = ExplanationDialog(self)
            dialog.setWindowTitle("Explanation")
            dialog.exec()

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)