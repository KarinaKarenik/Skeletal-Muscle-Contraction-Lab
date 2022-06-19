from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import random, windows

class Experiment1_two(QtWidgets.QMainWindow):
    experiment1_three = 0
    def __init__(self):
        super(Experiment1_two, self).__init__()
        loadUi("./rsc/ui/experiment1_nerve_treshold_two.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(200/5))
        self.pushButtonApplyVoltage.clicked.connect(self.applyVoltage)
        self.dial.valueChanged.connect(self.valueChanged)
        #self.labelPage.setStyleSheet("color: black")

    def loadChart(self, exp1three):
        self.experiment1_three = exp1three

    def valueChanged(self):
        value = self.dial.value()
        value = value / 1000
        self.lcdNumber.display(str(value))

    def applyVoltage(self):
        force = 0
        value = self.dial.value()
        value = value / 1000
        if (value >= 2.4):
            force = random.randint(117,142)
        elif (value >= 2.3):
            force = random.randint(117,140)
        elif (value >= 2.0):
            force = random.randint(114,135)
        elif (value >= 1.9):
            force = random.randint(107,129)
        elif (value >= 1.8):
            force = random.randint(111,123)
        elif (value >= 1.7):
            force = random.randint(101,116)
        elif (value >= 1.6):
            force = random.randint(85,99)
        elif (value >= 1.5):
            force = random.randint(67,81)
        elif (value >= 1.4):
            force = random.randint(49,56)
        elif (value >= 1.3):
            force = random.randint(26,29)
        elif (value >= 1.2):
            force = random.randint(10,12)
        elif (value >= 1.1):
            force = 2
        else:
            force = 0
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(""+str(value)))
        self.tableWidget.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(""+str(force)))
        
        #copia y añade los datos tambien a la tabla de la siguiente ventana
        self.experiment1_three.x_data.append(value)
        self.experiment1_three.y_data.append(force)
        self.experiment1_three.tableWidget.insertRow(rowPosition)
        self.experiment1_three.tableWidget.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(""+str(value)))
        self.experiment1_three.tableWidget.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(""+str(force)))
        self.experiment1_three.UiComponents()


    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)
