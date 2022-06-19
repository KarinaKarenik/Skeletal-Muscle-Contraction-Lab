from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import pyqtgraph as pg
import windows


class Experiment4_2_two(QtWidgets.QMainWindow):
    x_data = []
    y_data_rt = []
    y_data_tt = []
    y_data_diff = []
    def __init__(self):
        super(Experiment4_2_two, self).__init__()
        loadUi("./rsc/ui/experiment4.2_length_tension_two.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(500/7))
        self.UiComponents()
        # showing all the widgets
        
    def clearLayout(self):
        for i in reversed(range(self.gridLayout.count())): 
            widgetToRemove = self.gridLayout.itemAt(i).widget()
            # remove it from the layout list
            self.gridLayout.removeWidget(widgetToRemove)
            # remove it from the gui
            widgetToRemove.setParent(None)

    def UiComponents(self):
        self.clearLayout()
        self.gridLayout
        # create plot window object
        plt = pg.plot()
        # showing x and y grids
        plt.showGrid(x = True, y = True)
        # adding legend
        plt.addLegend()
        # set properties of the label for y axis
        plt.setLabel('left', 'Weight', units ='g')
        # set properties of the label for x axis
        plt.setLabel('bottom', 'Length', units ='mm')
        # setting horizontal range
        plt.setXRange(25, 35)
        # setting vertical range
        plt.setYRange(0, 400)
        # setting window title to the plot window
        # ploting line in green color
        # with dot symbol as x, not a mandatory field
        line1 = plt.plot(self.x_data, self.y_data_rt, pen ='b', symbol ='o', symbolPen ='g',symbolBrush = 0.1, name ='resting tension')
        # ploting line2 with blue color
        # with dot symbol as o
        line2 = plt.plot(self.x_data, self.y_data_tt, pen ='r', symbol ='o', symbolPen ='b',symbolBrush = 0.1, name ='tetanic tension')
        line3 = plt.plot(self.x_data, self.y_data_diff, pen ='g', symbol ='x', symbolPen ='b',symbolBrush = 0.1, name ='difference TT-RT')

        self.gridLayout.addWidget(plt)


    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)