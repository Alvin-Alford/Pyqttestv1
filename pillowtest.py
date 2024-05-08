from PIL import Image, ImageDraw 
import os
from datetime import datetime
import sys
from PyQt5.QtWidgets import QApplication
from window import Window
import pwd
from PyQt5.QtGui import QPixmap
import random
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import (QMainWindow, QPushButton, QComboBox, QVBoxLayout, QCheckBox, QWidget,
                             QGroupBox, QGridLayout, QSpinBox, QLineEdit, QHBoxLayout, QLabel, QFormLayout)
from pyqttoast import Toast, ToastPreset, ToastIcon, ToastPosition, ToastButtonAlignment

user = pwd.getpwuid(os.getuid())[0]
string = "mkdir /Users/" + str(user) + "/Documents/.hiddendata/"

os.system(string)

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.count = 0
        self.button = QPushButton(f"Click Count: {self.count}", self)
        self.button.setFixedSize(120, 60)
        self.button.clicked.connect(self.count_clicks)
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def count_clicks(self):
        img = Image.new("RGB", (50, 50))
        draw = ImageDraw.Draw(img) 
        draw.rectangle(xy = (0, 0, 50, 50), 
               fill = (0, 127, 0), 
               outline = (255, 255, 255), 
               width = 5) 
        

        today = datetime.now()

        # Get current ISO 8601 datetime in string format
        iso_date = today.isoformat()

        string = "/Users/" + str(user) + "/Documents/.hiddendata/" + str(iso_date) + ".png"
        print(string)
        img.save(string) 
        #toast.setIcon(QPixmap('path/to/your/icon.png'))

        toast = Toast(self)
        Toast.setOffset(30, 100)  # Default: 20, 45
        toast.setDuration(5000)
        #toast.setTitle(self.title_input.text())
        #toast.setText(self.text_input.text())
        toast.setBorderRadius(5)
        toast.setShowIcon(True)
        toast.setShowIcon(QPixmap(string))
        toast.setIconSize(QSize(50,50))
        toast.setMinimumWidth(500)
        toast.setMaximumWidth(501)
        toast.setMinimumHeight(500)
        toast.setMaximumHeight(501)
        toast.show()




# Run demo
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

# Opening the image to be used 

  
# Creating a Draw object 

  
# Drawing a green rectangle 
# in the middle of the image 

  
# Method to display the modified image 

