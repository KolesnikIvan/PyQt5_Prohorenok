# from PyQt5 import QtCore, QtWidgets

# class MyThread(QtCore.QThread):
#     mysignal = QtCore.pyqtSignal(str)
#     def __init__(self, parent=None):
#         QtCore.QThread.__init__(self, parent)
#         self.running = False  # flag
#         self.count = 0

#     def run(self):
#         self.running = True
#         while self.running:
#             self.count += 1
#             self.mysignal.emit("count=%s" % self.count)
#             self.sleep(1)


# class MyWindow(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.label = QtWidgets.QLabel("Press th button to start the process")
#         self.label.setAlignment(QtCore.Qt.AlignHCenter)
#         self.btnStart = QtWidgets.QPushButton("Start the thread")
#         self.btnStop = QtWidgets.QPushButton('Stop the thread')
#         self.vbox = QtWidgets.QVBoxLayout()
#         self.vbox.addWidget(self.label)
#         self.vbox.addWidget(self.btnStart)
#         self.vbox.addWidget(self.btnStop)
#         self.setLayout(self.vbox)
#         self.mythread = MyThread()
#         self.btnStart.clicked.connect(self.on_start)
#         self.btnStop.clicked.connect(self.on_stop)
#         self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

#     def on_start(self):
#         if not self.mythread.isRunning():
#             self.mythread.start()

#     def on_stop(self):
#         self.mythread.running = False

#     def on_change(self, s):
#         self.label.setText(s)

#     def closeEvent(self, event):        # will be called when close the window
#         self.hide()                     # hide the window
#         self.mythread.running = False   # change the flag
#         self.mythread.wait(5000)        # give time to finish
#         event.accept()


# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWindow()
#     window.setWindowTitle('Start and stop a thread')
#     window.show()
#     sys.exit(app.exec_())

from PyQt5 import QtCore, QtWidgets

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.running = False  # flag
        self.count = 0

    def run(self):
        self.running = True
        while self.running:
            self.count += 1
            self.mysignal.emit("count=%s" % self.count)
            self.sleep(1)


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('Push the button to start the thread')
        self.btnStart = QtWidgets.QPushButton('Press to start')
        self.btnStop = QtWidgets.QPushButton('Press to stop')
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnStart)
        self.vbox.addWidget(self.btnStop)
        self.setLayout(self.vbox)
        self.mythread = MyThread()
        self.btnStart.clicked.connect(self.on_start)
        self.btnStop.clicked.connect(self.on_stop)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_start(self):
        if not self.mythread.isRunning():
            self.mythread.start()

    def on_stop(self):
        self.mythread.running = False
    
    def on_change(self, s):
        self.label.setText(s)

    def closeEvent(self, event):
        self.hide()
        self.mythread.running = False
        self.mythread.wait(5000)
        event.accept()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle('17_14 cycle in thread')
    window.resize(300, 70)
    window.show()
    sys.exit(app.exec_())
