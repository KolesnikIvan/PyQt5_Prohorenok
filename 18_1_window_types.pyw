from tkinter.tix import WINDOW
from PyQt5 import QtWidgets, QtCore, Qt
import sys

WINDOW_TYPES = [
    # QtCore.Qt.Widget, 
    # QtCore.Qt.Window, 
    # QtCore.Qt.Dialog, 
    # QtCore.Qt.Sheet, 
    # QtCore.Qt.Drawer, 
    # QtCore.Qt.Popup,
    QtCore.Qt.Tool,
    # QtCore.Qt.ToolTip,
    QtCore.Qt.SplashScreen,
    # QtCore.Qt.Desktop,
    QtCore.Qt.SubWindow,
    QtCore.Qt.ForeignWindow,
    QtCore.Qt.CoverWindow,
    ]

WINDOW_TYPES_NAMES = [
    # 'Widget', 
    # 'Window', 
    # 'Dialog', 
    # 'Sheet', 
    # 'Drawer', 
    # 'Popup',
    'Tool',
    # 'ToolTip',
    'SplashScreen',
    # 'Desktop',
    'SubWindow',
    'ForeignWindow',
    'CoverWindow',
    ]

app = QtWidgets.QApplication(sys.argv)
for w_type, w_name in zip(WINDOW_TYPES, WINDOW_TYPES_NAMES):
    print(w_name)
    window = QtWidgets.QWidget(flags = w_type)
    window.setWindowTitle("Window's header " + w_name)
    window.resize(400, 50)
    window.show()
    app.exec_()
    # QtCore.QThread.sleep(2)
    window.close()
sys.exit()
