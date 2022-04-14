from PyQt5 import QtCore, QtWidgets
import sys

def show_modal_window():
    global modalWindow
    modalWindow = QtWidgets.QWidget(window1, QtCore.Qt.Window)
    modalWindow.setWindowTitle('modal window')
    modalWindow.resize(200, 50)
    # modalWindow.setWindowModality(QtCore.Qt.WindowModal)
    modalWindow.setWindowModality(QtCore.Qt.ApplicationModal)
    # attribute WA_DeleteOnClose automatically deletes the window when close
    modalWindow.setAttribute(QtCore.Qt.WA_DeleteOnClose, True)
    modalWindow.move(window1.geometry().center()\
                    - modalWindow.rect().center()\
                    - QtCore.QPoint(4, 30))
    modalWindow.show()

app = QtWidgets.QApplication(sys.argv)
window1 = QtWidgets.QWidget()
window1.setWindowTitle('usual window')
window1.resize(300, 100)
button = QtWidgets.QPushButton('open modal window')
button.clicked.connect(show_modal_window)
vbox = QtWidgets.QVBoxLayout()
vbox.addWidget(button)
window1.setLayout(vbox)
window1.show()

window2 = QtWidgets.QWidget()
window2.setWindowTitle('this window will not be blocked by WindowModal')
window2.resize(500, 100)
window2.show()

sys.exit(app.exec_())

