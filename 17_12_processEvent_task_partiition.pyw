# using processEvents() method
from PyQt5 import QtWidgets
import sys, time

def on_click():
    button.setDisabled(True)
    for i in range(1, 21):
        QtWidgets.qApp.processEvents()
        # метод processEvent возвращает управление в главный цикл (в "перерывах")
        # в результате всегда можно перещелкнуться на окно программы
        # она не выглядит зависшей, окно переотрисовывается
        time.sleep(1)
        print('step ', i)
    button.setDisabled(False)


app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Start process 17_12')
button.resize(200, 40)
button.clicked.connect(on_click)
button.show()
sys.exit(app.exec_())
