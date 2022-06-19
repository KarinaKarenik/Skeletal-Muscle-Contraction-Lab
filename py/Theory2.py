from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia, QtMultimediaWidgets
from PyQt5.uic import loadUi
import windows, sys, os

class Theory2(QtWidgets.QMainWindow):

    def __init__(self):
        super(Theory2, self).__init__()
        ui_path = "rsc/ui/theory2_preparation.ui"
        filepath = "rsc/vid/video1.gif"
        if getattr(sys, 'frozen', False):
            ui_path = os.path.join(sys._MEIPASS, ui_path)
            filepath = os.path.join(sys._MEIPASS, filepath)
        loadUi(ui_path,self)
        #self.setup()
        self.movie = QtGui.QMovie(filepath)
        self.label_2.setMovie(self.movie)
        self.movie.start()
        #self.mediaPlayer.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(filepath)))
        #self.mediaPlayer.play()
        self.pushButtonMenu.clicked.connect(self.goToMenu)
        self.pushButtonBack.clicked.connect(self.goBack)
        self.pushButtonNext.clicked.connect(self.goNext)
        self.progressBar.setValue(int(200/4))
        
    #def setup(self):$
        #self.videoOutput = self.makeVideoWidget()
        #self.mediaPlayer = self.makeMediaPlayer()
    
    #def makeVideoWidget(self):
        #videoOutput = QtMultimediaWidgets.QVideoWidget(self)
        #vbox =  QtWidgets.QVBoxLayout()
        #vbox.addWidget(videoOutput)
        #self.videoWidget.setLayout(vbox)
        #return videoOutput
    
    #def makeMediaPlayer(self):
        #mediaPlayer = QtMultimedia.QMediaPlayer(self)
        #mediaPlayer.setVideoOutput(self.videoOutput)
        #return mediaPlayer
    

    def goBack(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()-1)

    def goNext(self):
        windows.DataWindows.widgets.setCurrentIndex(windows.DataWindows.widgets.currentIndex()+1)

    def goToMenu(self):
        windows.DataWindows.widgets.setCurrentIndex(0)
        
        
        