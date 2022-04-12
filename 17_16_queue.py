# from PyQt5 import QtCore, QtWidgets
# import queue

# class MyThread(QtCore.QThread):
#     task_done = QtCore.pyqtSignal(int, int, name='taskdone')
#     def __init__(self, id, queue, parent=None):
#         QtCore.QThread.__init__(self, parent)
#         self.id = id
#         self.queue = queue

#     def run(self):
#         while True:
#             task = self.queue.get()
#             self.sleep(5)
#             self.task_done.emit(task, self,id)
#             self.queue.task_done()

# class MyWindow(QtWidgets.QPushButton):
#     def __init__(self, parent=None):
#         QtWidgets.QPushButton.__init__(self, parent)
#         self.setText('distribute tasks')
#         self.queue = queue.Queue()
#         self.threads = []
#         for i in range(1, 3):
#             thread = MyThread(i, self.queue)
#             self.threads.append(thread)
#             thread.task_done.connect(self.on_task_done, QtCore.Qt.QueuedConnection)
#             thread.start()
#         self.clicked.connect(self.on_add_task)

#     def on_add_task(self):
#         for i in range(0, 11):
#             self.queue.put(i)
            
#     def on_task_done(self, data, id):
#         print(data, "- id=", id)

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = MyWindow()
#     window.setWindowTitle('Use queue module')
#     window.resize(300, 30)
#     window.show()
#     sys.exit(app.exec_())

from PyQt5 import QtCore, QtWidgets
import queue
from random import randint
from string import ascii_lowercase

class MyThread(QtCore.QThread):
    task_done = QtCore.pyqtSignal(str, int, name='taskDone')
    def __init__(self, id, queue, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.id = id
        self.queue = queue

    def run(self):
        while True:
            task = self.queue.get()
            self.sleep(randint(1, 3))
            # выполнив задание, посылает сигнал и вызывает task_done()
            self.task_done.emit(task, self.id)
            self.queue.task_done()
            print(self.queue.qsize(), ' tasks remain')

class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText('distribute tasks')
        self.queue = queue.Queue()
        self.threads = []
        for i  in range(1, 3):
            thread = MyThread(i, self.queue) #всем потокам один экз.очереди
            self.threads.append(thread)
            thread.task_done.connect(self.on_task_done, QtCore.Qt.QueuedConnection)
            thread.start()
        print('thrads are initialised')
        print('qsize is ', self.queue.qsize())
        self.clicked.connect(self.on_add_task)

    def on_add_task(self):
        # for i in range(0, 11):
        for i in ascii_lowercase:
            self.queue.put(i)

    def on_task_done(self, data, id):
        print(data, "- id=", id)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Использование модуля queue")
    window.resize(300, 30)
    window.show()
    sys.exit(app.exec_())
