# changing window size 
from PyQt5 import QtCore, QtWidgets
import time

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.btnMin = QtWidgets.QPushButton('minimize')
        self.btnMax = QtWidgets.QPushButton('maximize')
        self.btnFull = QtWidgets.QPushButton('full screen')
        self.btnNormal = QtWidgets.QPushButton('normal')
        self.btnOpacify = QtWidgets.QPushButton('opasify')
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.btnMin)
        vbox.addWidget(self.btnMax)
        vbox.addWidget(self.btnFull)
        vbox.addWidget(self.btnNormal)
        vbox.addWidget(self.btnOpacify)
        self.setLayout(vbox)
        self.btnMin.clicked.connect(self.on_min)
        self.btnMax.clicked.connect(self.on_max)
        self.btnFull.clicked.connect(self.on_full)
        self.btnNormal.clicked.connect(self.on_normal)
        self.btnOpacify.clicked.connect(self.on_opacify)

    def on_min(self):
        self.showMinimized()

    def on_max(self):
        self.showMaximized()

    def on_full(self):
        self.showFullScreen()
    
    def on_normal(self):
        self.showNormal()

    def on_opacify(self):
        for i in range(1, 10):
            self.setWindowOpacity(i / 10)
            time.sleep(1)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('window open/close')
    window.resize(300, 100)
    window.show()
    sys.exit(app.exec_())
