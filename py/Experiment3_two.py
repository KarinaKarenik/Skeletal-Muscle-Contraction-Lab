from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import pyqtgraph as pg
from PyQt5.QtGui import QPixmap
import random,windows


class Experiment3_two(QtWidgets.QMainWindow):
    def __init__(self):
        super(Experiment3_two, self).__init__()
        loadUi("./rsc/ui/experiment3_tetanus_two.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(200/5))
        self.pushButtonApplyFreq.clicked.connect(self.applyFreq)
        #self.UiComponents()
        self.dial.valueChanged.connect(self.valueChanged)

        # showing all the widgets

    def valueChanged(self):
        value = self.dial.value()
        self.lcdNumber.display(str(value))
        
                
    def applyFreq(self):
        value = self.dial.value()
        self.lcdNumber.display(str(value))
        self.changeImage(value)
        
        
        
    def changeImage(self, value):
        if (value == 50):
            pixmap = QPixmap('./rsc/img/EXP3g/50.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 49):
            pixmap = QPixmap('./rsc/img/EXP3g/49.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 48):
            pixmap = QPixmap('./rsc/img/EXP3g/48.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 47):
            pixmap = QPixmap('./rsc/img/EXP3g/47.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 46):
            pixmap = QPixmap('./rsc/img/EXP3g/46.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 45):
            pixmap = QPixmap('./rsc/img/EXP3g/45.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 44):
            pixmap = QPixmap('./rsc/img/EXP3g/44.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 43):
            pixmap = QPixmap('./rsc/img/EXP3g/43.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 42):
            pixmap = QPixmap('./rsc/img/EXP3g/42.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 41):
            pixmap = QPixmap('./rsc/img/EXP3g/41.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 40):
            pixmap = QPixmap('./rsc/img/EXP3g/40.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 39):
            pixmap = QPixmap('./rsc/img/EXP3g/39.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 38):
            pixmap = QPixmap('./rsc/img/EXP3g/38.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 37):
            pixmap = QPixmap('./rsc/img/EXP3g/37.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 36):
            pixmap = QPixmap('./rsc/img/EXP3g/36.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 35):
            pixmap = QPixmap('./rsc/img/EXP3g/35.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 34):
            pixmap = QPixmap('./rsc/img/EXP3g/34.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 33):
            pixmap = QPixmap('./rsc/img/EXP3g/33.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 32):
            pixmap = QPixmap('./rsc/img/EXP3g/32.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 31):
            pixmap = QPixmap('./rsc/img/EXP3g/31.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 30):
            pixmap = QPixmap('./rsc/img/EXP3g/30.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 29):
            pixmap = QPixmap('./rsc/img/EXP3g/29.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 28):
            pixmap = QPixmap('./rsc/img/EXP3g/28.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 27):
            pixmap = QPixmap('./rsc/img/EXP3g/27.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 26):
            pixmap = QPixmap('./rsc/img/EXP3g/26.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 25):
            pixmap = QPixmap('./rsc/img/EXP3g/25.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 24):
            pixmap = QPixmap('./rsc/img/EXP3g/24.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 23):
            pixmap = QPixmap('./rsc/img/EXP3g/23.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 22):
            pixmap = QPixmap('./rsc/img/EXP3g/22.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 21):
            pixmap = QPixmap('./rsc/img/EXP3g/21.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 20):
            pixmap = QPixmap('./rsc/img/EXP3g/20.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 19):
            pixmap = QPixmap('./rsc/img/EXP3g/19.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 18):
            pixmap = QPixmap('./rsc/img/EXP3g/18.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 17):
            pixmap = QPixmap('./rsc/img/EXP3g/17.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 16):
            pixmap = QPixmap('./rsc/img/EXP3g/16.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 15):
            pixmap = QPixmap('./rsc/img/EXP3g/15.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 14):
            pixmap = QPixmap('./rsc/img/EXP3g/14.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 13):
            pixmap = QPixmap('./rsc/img/EXP3g/13.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 12):
            pixmap = QPixmap('./rsc/img/EXP3g/12.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 11):
            pixmap = QPixmap('./rsc/img/EXP3g/11.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 10):
            pixmap = QPixmap('./rsc/img/EXP3g/10.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 9):
            pixmap = QPixmap('./rsc/img/EXP3g/9.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 8):
            pixmap = QPixmap('./rsc/img/EXP3g/8.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 7):
            pixmap = QPixmap('./rsc/img/EXP3g/7.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 6):
            pixmap = QPixmap('./rsc/img/EXP3g/6.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 5):
            pixmap = QPixmap('./rsc/img/EXP3g/5.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 4):
            pixmap = QPixmap('./rsc/img/EXP3g/4.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 3):
            pixmap = QPixmap('./rsc/img/EXP3g/3.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 2):
            pixmap = QPixmap('./rsc/img/EXP3g/2.png')
            self.labelImage.setPixmap(pixmap)
        elif (value == 1):
            pixmap = QPixmap('./rsc/img/EXP3g/1.png')
            self.labelImage.setPixmap(pixmap)
        else: 
            pixmap = QPixmap('./rsc/img/EXP3g/0.png')
            self.labelImage.setPixmap(pixmap)
            
            
        
        

        
    # def UiComponents(self):
    #     # create plot window object
    #     plt = pg.plot()
    #     # showing x and y grids
    #     plt.showGrid(x = True, y = True)
    #     # adding legend
    #     plt.addLegend()
    #     # set properties of the label for y axis
    #     plt.setLabel('left', 'Weight', units ='g')
    #     # set properties of the label for x axis
    #     plt.setLabel('bottom', 'Length', units ='mm')
    #     # setting horizontal range
    #     plt.setXRange(25, 35)
    #     # setting vertical range
    #     plt.setYRange(0, 400)
    #     # setting window title to the plot window
    #     # ploting line in green color
    #     # with dot symbol as x, not a mandatory field
    #     #line1 = plt.plot(self.x_data, self.y_data_rt, pen ='b', symbol ='o', symbolPen ='g',symbolBrush = 0.1, name ='resting tension')
    #     # ploting line2 with blue color
    #     # with dot symbol as o
    #     #line2 = plt.plot(self.x_data, self.y_data_tt, pen ='r', symbol ='o', symbolPen ='b',symbolBrush = 0.1, name ='tetanic tension')
    #     #line3 = plt.plot(self.x_data, self.y_data_diff, pen ='g', symbol ='x', symbolPen ='b',symbolBrush = 0.1, name ='difference TT-RT')

    #     self.gridLayout.addWidget(plt)


    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)
        
        
        