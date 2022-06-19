from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
import pyqtgraph as pg
import windows


class Experiment1_three(QtWidgets.QMainWindow):
    x_data = []
    y_data = []
    def __init__(self):
        super(Experiment1_three, self).__init__()
        loadUi("./rsc/ui/experiment1_nerve_treshold_three.ui",self)
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(300/5))
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
        plot = pg.plot()
        # creating a scatter plot item
        # of size = 10
        # using brush to enlarge the of green color
        scatter = pg.ScatterPlotItem(size=10, brush=pg.mkBrush(30, 255, 35, 255))
        # adding spots to the scatter plot
        scatter.addPoints(self.x_data, self.y_data)
        plot.addItem(scatter)
        # set properties of the label for y axis
        plot.setLabel('left', 'Peak force', units ='g')
        # set properties of the label for x axis
        plot.setLabel('bottom', 'Voltage', units ='V')
        self.gridLayout.addWidget(plot)


    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)