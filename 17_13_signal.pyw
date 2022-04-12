from PyQt5 import QtCore, QtWidgets

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)

    def run(self):
        # код, объявленный в методе run, будет выполняться в отдельном потоке
        for i in range(1, 21):
            self.sleep(3)
            self.mysignal.emit("i=%s" % i)

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('Push the button to start a thread')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button = QtWidgets.QPushButton('Start process')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.button)
        self.setLayout(self.vbox)
        self.mythread = MyThread()
        self.button.clicked.connect(self.on_click)
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_click(self):
        self.button.setDisabled(True)
        self.mythread.start()

    def on_started(self):
        self.label.setText('method on_started() is called')

    def on_finished(self):
        self.label.setText('on_finished() method is called')
        self.button.setDisabled(False)
    
    def on_change(self, s):
        self.label.setText(s)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('usnig QThread class')
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())
