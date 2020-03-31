
# Development

### 1. Install and import necessary libraries to the mainApp.
#### a. Install PyQt5
 ```.sh
 pip install pyqt5
 ```
 #### b. Import libraries
 ```.py
 import sys, os, hashlib
 from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QDialog, QLineEdit
 ```
### 2. Convert ui file to py file
```.sh
python3 pyuic.py name.ui -o name.py
```
### 3. Add all the Main Windows and Dialog Windows to the mainApp
```.py
#import the class of all the Dialog Windows
from Add_food import Add_Food
from Delete import Delete
from Edit_food import Edit
from ListOfFood import List_food
from log_in import login
from Summary import Summary
from ListFunct import Ui_MainWindow as mainW  #This is the Home (Main windows for the App)

class Home(QMainWindow, mainW):  # this is the main parent, and as such, it takes the library QMainWindow
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)
        
class log_in(login):  # this one does not say QMainWindow since it will be defined as a child of Home, and as such,
    # it is unnecessary
    def __init__(self, parent=None):
        super(log_in, self).__init__(parent)
        self.setupUi(self)

class Add(Add_Food):
    def __init__(self, parent=None):
        super(Add, self).__init__(parent)
        self.setupUi(self)

class delete(Delete):
    def __init__(self, parent=None):
        super(delete, self).__init__(parent)
        self.setupUi(self)

class edit(Edit):
    def __init__(self, parent=None):
        super(edit, self).__init__(parent)
        self.setupUi(self)

class list_food(List_food):
    def __init__(self, parent=None):
        super(list_food, self).__init__(parent)
        self.setupUi(self)

class summary(Summary):
    def __init__(self, parent=None):
        super(summary, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)  # creating the application with arguments from user
mainW = Home()  # setting the main window to the Home UI
mainW.show()
app.exec_()
        
```


### 4. Hash a password
```.py
import hashlib
import os

password = "123456"
salt = os.urandom(32)

key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt,1000) #encode the password with the hashlib library
```
### 5.
