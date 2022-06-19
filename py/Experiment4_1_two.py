from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import windows

class Experiment4_1_two(QtWidgets.QMainWindow):

    def __init__(self):
        super(Experiment4_1_two, self).__init__()
        loadUi("./rsc/ui/experiment4.1_length_tension_two.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.radioButton1.clicked.connect(self.buttonOne)
        self.radioButton2.clicked.connect(self.buttonTwo)
        self.radioButton3.clicked.connect(self.buttonThree)
        self.progressBar.setValue(int(200/7))
        self.img1 = QPixmap('./rsc/img/exp4/EXP4.1.1.png')
        self.img2 = QPixmap('./rsc/img/exp4/EXP4.1.2.png')
        self.img3 = QPixmap('./rsc/img/exp4/EXP4.1.3.png')
                    
    def buttonOne(self):
        self.labelImage.setPixmap(self.img1)
    
    def buttonTwo(self):
        self.labelImage.setPixmap(self.img2)
    
    def buttonThree(self):
        self.labelImage.setPixmap(self.img3)

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)