from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv) #QApplication object required before creating QWidgets
from windows import DataWindows    

with open('./rsc/qss/Irrorater.qss', 'r') as f:
        styleSheet = f.read()
        app.setStyleSheet(styleSheet)

DataWindows.widgets.show()
DataWindows.widgets.showFullScreen()
sys.exit(app.exec_())


