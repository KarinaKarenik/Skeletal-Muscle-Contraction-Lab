from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Experiment3_one(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment3_one, self).__init__()
        loadUi("./rsc/ui/experiment3_tetanus_one.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        #self.pushButtonAnswerQuestion1.clicked.connect(self.answerQuestionOne)
        self.progressBar.setValue(int(100/5))

    #def answerQuestionOne(self):
        #x = float(self.lineEditQuestion1.text())

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)