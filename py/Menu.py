from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows
from PyQt5.QtCore import QCoreApplication


class About(QtWidgets.QDialog):
    def __init__(self, parent = None):
        super(About, self).__init__(parent)
        loadUi("./rsc/ui/about.ui",self)

class Menu(QtWidgets.QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("./rsc/ui/menu.ui",self)
        self.setWindowTitle('Menu')
        self.pushButtonTheoryMenu.clicked.connect(self.goToTheory)
        self.pushButtonExperiment1Menu.clicked.connect(self.goToExperiment1)
        self.pushButtonExperiment2Menu.clicked.connect(self.goToExperiment2)
        self.pushButtonExperiment3Menu.clicked.connect(self.goToExperiment3)
        self.pushButtonExperiment4Menu.clicked.connect(self.goToExperiment4)
        self.pushButtonConclusion.clicked.connect(self.goToConclusion)   
        self.pushButtonAboutMenu.clicked.connect(self.showAbout)
        self.about = About(self)
        self.pushButtonExit.clicked.connect(QCoreApplication.instance().quit)
        

    def showAbout(self):
        self.about.setWindowTitle("About Skeletal Muscle Contraction.")
        self.about.exec()
        


    def goToTheory(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)
    def goToExperiment1(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+5)
    def goToExperiment2(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+10)
    def goToExperiment3(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+15)
    def goToExperiment4(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+20)
    def goToConclusion(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+27)



        