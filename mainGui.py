import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import *
from PySide6.QtCore import QFile, QIODevice, QObject, Slot
import time
import threading


class MyWindow(QObject):
    def __init__(self, ui_file_name):
        super().__init__()

        ui_file = QFile(ui_file_name)
        if not ui_file.open(QIODevice.ReadOnly):
            print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
            sys.exit(-1)

        loader = QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()

        if not self.window:
            print(loader.errorString())
            sys.exit(-1)

        self.stop_flag = threading.Event()
        
        # Find the button by its object name
        self.button = self.window.findChild(QPushButton, "pushButton")

        # Connect the button's clicked signal to a function
        self.button.clicked.connect(self.startloopThread)

        self.label = self.window.findChild(QLabel, "label")

        self.window.show()


    def startloopThread(self):
        self.thread = threading.Thread(target=self.onClick)
        self.thread.start()

    def onClick(self):
        self.button.setDisabled(True) 
        currentThread = threading.current_thread().name       

        c = 0
        while True and not self.stop_flag.is_set() :

            
            c += 1
            if c == 5:
                self.button.setDisabled(False)
                break
            else:
                test = f"Hello World, {c}, {currentThread}"
                self.label.setText(test)
                time.sleep(1)

        print(f'{currentThread} stopped')
            

    
    def stop_thread(self):
        self.stop_flag.set()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui_file_name = "./myappQTUI.ui"
    my_window = MyWindow(ui_file_name)
    sys.exit(app.exec())
