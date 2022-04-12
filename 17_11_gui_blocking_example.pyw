# simulate freezing
from PyQt5 import QtWidgets
import sys, time

def on_click():
    time.sleep(10)

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Start process')
button.resize(200, 40)
button.clicked.connect(on_click)
# если, нажав кнопку, заслонить окно другим, 
# а потом вернуться к первому, то оно не сразу отрисуется
# это иллюстрирует зависание программы 
# во время передачи управления от основного цикла обработчику
button.show()
sys.exit(app.exec_())
