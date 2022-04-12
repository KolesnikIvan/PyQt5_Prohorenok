# using loadUi function
# loads a QtDesigner .ui and returns an instance of user interface
from PyQt5 import QtWidgets, uic

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi("MyForm.ui", self)
        # self.btnQuit.clicked.connect(QtWidgets.qApp.quit)
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
