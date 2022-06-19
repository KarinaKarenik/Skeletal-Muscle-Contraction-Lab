from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows

class Experiment1_four(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment1_four, self).__init__()
        loadUi("./rsc/ui/experiment1_nerve_treshold_four.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(400/5))
        self.pushButtonAnswerQuestion1.clicked.connect(self.answerQuestion1)
        self.pushButtonAnswerQuestion2.clicked.connect(self.answerQuestion2)
        self.pushButtonQ3Yes.clicked.connect(self.question3Yes)
        self.pushButtonQ3No.clicked.connect(self.question3No)
        self.pushButtonAnswerQuestion4.clicked.connect(self.answerQuestion4)
        self.pushButtonQ5Yes.clicked.connect(self.question5Yes)
        self.pushButtonQ5No.clicked.connect(self.question5No)

    def answerQuestion1(self):
        x = float(self.lineEditQuestion1.text())
        if (x > 1.4):
            QtWidgets.QMessageBox.about(self, "Incorrect!", "No! The voltage is TOO BIG")
        elif (x > 0.5):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct! That is the threshold voltage.")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "No! At that voltage you have NO response.")
    
    def answerQuestion2(self):
        if (self.comboBox.currentText() == "one" and self.comboBox_2.currentText() == "motor"):
            QtWidgets.QMessageBox.about(self, "Correct!", "Correct! A voltage just above the threshold will stimulate one motor nerve(or a few) and this results in a twitch of a few muscle fibers. Sensory nerves may also be stimulated, but this will not result in muscle contraction, as the nerve impulses cannot cross to the muscle.")
        else:
            QtWidgets.QMessageBox.about(self, "Incorrect!", "Incorrect! A voltage just above the threshold will stimulate one motor nerve(or a few) and this results in a twitch of a few muscle fibers. Sensory nerves may also be stimulated, but this will not result in muscle contraction, as the nerve impulses cannot cross to the muscle.")
    
    def question3Yes(self):
        QtWidgets.QMessageBox.about(self, "Incorrect!", "No, you are Incorrect!")
    
    def question3No(self):
        QtWidgets.QMessageBox.about(self, "Correct!", "Correct! The frog nerve-muscle preparation shows biological variability. This allows us to repeat the observations three or more times and record the average values.")

    def answerQuestion4(self):
        x = float(self.lineEditQuestion4.text())
        if (x > 136):
             QtWidgets.QMessageBox.about(self, "Incorrect!", "Your answer is too big. Go back, make more observations, and use the cursor on the graph to determine the average maximum response.")
        elif (x > 119):
             QtWidgets.QMessageBox.about(self, "Correct!", "Well done.")
        else:
             QtWidgets.QMessageBox.about(self, "Incorrect!", "Your answer is too small. Go back, make more observations, and use the cursor on the graph to determine the average maximum response.")
    
    def question5Yes(self):
        QtWidgets.QMessageBox.about(self, "Correct!", "Correct! This law applies to each individual motor nerve fiber in the sciatic nerve. The gastrocnemius muscle gives a graded response to stimuli to the sciatic nerve because this nerve trunk is made up of hundreds of separate motor nerves, each of which has a different threshold. Each motor nerve causes a specific group of muscle fibers to contract the motor unit")
    
    def question5No(self):
        QtWidgets.QMessageBox.about(self, "Incorrect!", "Incorrect")

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)