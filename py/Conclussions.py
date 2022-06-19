from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import windows


class Conclussions(QtWidgets.QMainWindow):

    def __init__(self):
        super(Conclussions, self).__init__()
        loadUi("./rsc/ui/conclussions.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonMenu2.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)