from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap
import random, windows

class Experiment4_2_one(QtWidgets.QMainWindow):
    chart_window = 0
    def __init__(self):
        super(Experiment4_2_one, self).__init__()
        loadUi("./rsc/ui/experiment4.2_length_tension.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(400/7))
        self.pushButtonStimulate.clicked.connect(self.stimulate)
        self.dial.valueChanged.connect(self.valueChanged)
        #self.labelPage.setStyleSheet("color: black")

    def loadChart(self, window):
        self.chart_window = window

    def valueChanged(self):
        muscle_length = self.dial.value()
        muscle_length = muscle_length / 10.0
        self.lcdNumber.display(str(muscle_length))

    def changeImage(self, muscle_length):
        if (muscle_length >= 34):
            pixmap = QPixmap('./rsc/img/exp4.2/exp 4.2.5.png')
            self.labelImage.setPixmap(pixmap)
        elif (muscle_length >= 32):
            pixmap = QPixmap('./rsc/img/exp4.2/exp 4.2.4.png')
            self.labelImage.setPixmap(pixmap)
        elif (muscle_length >= 29):
            pixmap = QPixmap('./rsc/img/exp4.2/exp 4.2.3.png')
            self.labelImage.setPixmap(pixmap)
        elif (muscle_length >= 27):
            pixmap = QPixmap('./rsc/img/exp4.2/exp 4.2.2.png')
            self.labelImage.setPixmap(pixmap)
        else:
            pixmap = QPixmap('./rsc/img/exp4.2/exp4.2.1.png')
            self.labelImage.setPixmap(pixmap)
            
    def stimulate(self):
        muscle_length = self.dial.value()
        muscle_length = muscle_length / 10.0
        resting_tension = 0.0
        tetanic_tension = 0.0
        if (muscle_length >= 35):
            resting_tension = round(random.uniform(310.0,330.0),1)
            tetanic_tension = round(random.uniform(290.5,340.5),1)
        elif (muscle_length >= 34.5):
            resting_tension = round(random.uniform(250.0,260.0),1)
            tetanic_tension = round(random.uniform(280.5,318.5),1)
        elif (muscle_length >= 34):
            resting_tension = round(random.uniform(210.0,225.0),1)
            tetanic_tension = round(random.uniform(275.6,300.5),1)
        elif (muscle_length >= 33.5):
            resting_tension = round(random.uniform(180.0,190.0),1)
            tetanic_tension = round(random.uniform(265.6,300.5),1)
        elif (muscle_length >= 33):
            resting_tension = round(random.uniform(140.0,150.0),1)
            tetanic_tension = round(random.uniform(265.6,300.5),1)
        elif (muscle_length >= 32.5):
            resting_tension = round(random.uniform(115.0,130.0),1)
            tetanic_tension = round(random.uniform(280.5,318.5),1)
        elif (muscle_length >= 32):
            resting_tension = round(random.uniform(85.0,100.0),1)
            tetanic_tension = round(random.uniform(280.5,318.5),1)
        elif (muscle_length >= 31.5):
            resting_tension = round(random.uniform(65.0,70.0),1)
            tetanic_tension = round(random.uniform(280.5,318.5),1)
        elif (muscle_length >= 31):
            resting_tension = round(random.uniform(50.0,55.0),1)
            tetanic_tension = round(random.uniform(290.5,340.5),1)
        elif (muscle_length >= 30.5):
            resting_tension = round(random.uniform(40.0,45.0),1)
            tetanic_tension = round(random.uniform(330.5,375.5),1)
        elif (muscle_length >= 30):
            resting_tension = round(random.uniform(30.0,35.0),1)
            tetanic_tension = round(random.uniform(330.5,375.5),1)
        elif (muscle_length >= 29.5):
            resting_tension = round(random.uniform(22.0,22.5),1)
            tetanic_tension = round(random.uniform(330.5,375.5),1)
        elif (muscle_length >= 29):
            resting_tension = round(random.uniform(17.0,18.0),1)
            tetanic_tension = round(random.uniform(330.5,375.5),1)
        elif (muscle_length >= 28.5):
            resting_tension = round(random.uniform(13.5,14.5),1)
            tetanic_tension = round(random.uniform(330.5,375.5),1)
        elif (muscle_length >= 28):
            resting_tension = round(random.uniform(11.0,11.5),1)
            tetanic_tension = round(random.uniform(325.5,350.5),1)
        elif (muscle_length >= 27.5):
            resting_tension = round(random.uniform(9.5,10.5),1)
            tetanic_tension = round(random.uniform(290.5,318.5),1)
        elif (muscle_length >= 27):
            resting_tension = round(random.uniform(8.0,8.5),1)
            tetanic_tension = round(random.uniform(180.5,222.5),1)
        elif (muscle_length >= 26.5):
            resting_tension = round(random.uniform(6.5,6.5),1)
            tetanic_tension = round(random.uniform(180.5,222.5),1)
        elif (muscle_length >= 26):
            resting_tension = round(random.uniform(3.0,3.5),1)
            tetanic_tension = round(random.uniform(120.5,144.5),1)
        else:
            resting_tension = 0
            tetanic_tension = round(random.uniform(36.5,39.5),1)
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(""+str(muscle_length)))
        self.tableWidget.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(""+str(resting_tension)))
        self.tableWidget.setItem(rowPosition,2,QtWidgets.QTableWidgetItem(""+str(tetanic_tension)))
        
        #añade los datos tambien a la tabla de la siguiente ventana
        self.chart_window.x_data.append(muscle_length)
        self.chart_window.y_data_rt.append(resting_tension)
        self.chart_window.y_data_tt.append(tetanic_tension)
        self.chart_window.y_data_diff.append(tetanic_tension-resting_tension)
        self.chart_window.tableWidget.insertRow(rowPosition)
        self.chart_window.tableWidget.setItem(rowPosition,0,QtWidgets.QTableWidgetItem(""+str(muscle_length)))
        self.chart_window.tableWidget.setItem(rowPosition,1,QtWidgets.QTableWidgetItem(""+str(resting_tension)))
        self.chart_window.tableWidget.setItem(rowPosition,2,QtWidgets.QTableWidgetItem(""+str(tetanic_tension)))
        self.chart_window.tableWidget.setItem(rowPosition,3,QtWidgets.QTableWidgetItem(""+str(resting_tension-tetanic_tension)))
        self.chart_window.UiComponents()

        self.changeImage(muscle_length)

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)
