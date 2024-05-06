import sys

import keyboard
from pyqttoast import Toast, ToastPreset
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QAction, QApplication, QMainWindow, QMenu


class KeyBoardManager(QObject):
    Keyactive = pyqtSignal()

    def start(self):
        keyboard.add_hotkey("ctrl+m", self.Keyactive.emit, suppress=True)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__(flags=Qt.WindowStaysOnTopHint)

        #self.menu = QMenu("Menu")
        #self.menu.addAction(QAction("menu1", self.menu))
        #self.menu.addAction(QAction("menu2", self.menu))
        #self.menu.addAction(QAction("menu3", self.menu))

        manager = KeyBoardManager(self)
        manager.Keyactive.connect(self.show_menu)
        manager.start()

    def show_menu(self):
        #print("111")
        toast = Toast(self)
        toast.setDuration(5000)  # Hide after 5 seconds
        toast.setTitle('Success! Confirmation email sent.')
        toast.setText('Check your email to complete signup.')
        toast.applyPreset(ToastPreset.SUCCESS)  # Apply style preset
        toast.show()
        #self.menu.popup(QCursor.pos())
        #print("222")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    win = MainWindow()
    # win.show()
    sys.exit(app.exec_())