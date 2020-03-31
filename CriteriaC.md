
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
salt = os.urandom(32)   #This is the combination with the password, which makes the passwords harder to crack

key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'),salt,1000) #encode the password with the hashlib library
```
### 5. Main Home Windows
```.py
#The Main Windows is the Home so it contains the buttons to the other dialog functions
class Home(QMainWindow, mainW):  # this is the main parent, and as such, it takes the library QMainWindow
    def __init__(self, parent=None):
        super(Home, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.log_out)    #This syntax will execute the function "log_out" when clicking the                                                              button
        self.pushButton_3.clicked.connect(self.list_food)
        self.pushButton_5.clicked.connect(self.add)
        self.pushButton_4.clicked.connect(self.summary)
        self.pushButton_6.clicked.connect(self.delete)
        self.pushButton_7.clicked.connect(self.edit)
        logVar = log_in(self)
        logVar.show()

    def log_out(self):  
        sys.exit(0)  #exit the program

    def list_food(self):
        listF = list_food(self)
        listF.show()   #Open the windows

    def add(self):
        addF = Add(self)
        addF.show()

    def summary(self):
        summaryF = summary(self)
        summaryF.show()

    def delete(self):
        deleteF = delete(self)
        deleteF.show()

    def edit(self):
        editF = edit(self)
        editF.show()
```
### 6. Log in Window
```.py
def __init__(self, parent=None):
    super(log_in, self).__init__(parent)
    self.setupUi(self)

    self.pushButton_2.clicked.connect(self.exit_app)
    self.pushButton.clicked.connect(self.enterApp)

    self.lineEdit.setPlaceholderText("Enter username: ")
    self.lineEdit_2.setPlaceholderText("Enter password: ")
    self.lineEdit_2.setEchoMode(QLineEdit.Password)

def exit_app(self):
    sys.exit(0)  # 0 means without errors

def enterApp(self):
    if self.lineEdit.text() == username and self.lineEdit_2.text() == my_secret_password:  #Check if the username and password                                                                                            are correct
        self.close()
    else: 
        self.lineEdit.setText("")
        self.lineEdit_2.setText("")
```
### 7. Add Window
```.py
def __init__(self, parent=None):
    super(Add, self).__init__(parent)
    self.setupUi(self)
    self.lineEdit.setPlaceholderText("Name of food: ")
    self.lineEdit_2.setPlaceholderText("Location: ")
    self.lineEdit_3.setPlaceholderText("Quantity: ")
    self.lineEdit_4.setPlaceholderText("Expiration: ")
    self.lineEdit_5.setPlaceholderText("Price: ")

    self.buttonBox.accepted.connect(self.addf)

def addf(self):
    with open("Database/NewFoodData.txt", "a") as out_file_add:   #open the Database text file
        StringName = self.lineEdit.text() + " "                   #Assign the input value 
        StringLocation = self.lineEdit_2.text() + " "
        StringQuantity = self.lineEdit_3.text() + " "
        StringExpiration = self.lineEdit_4.text() + " "
        StringPrice = self.lineEdit_5.text() + "\n"

        out_file_add.write(StringName)                          #Write the Input value to the Database text file
        out_file_add.write(StringLocation)
        out_file_add.write(StringQuantity)
        out_file_add.write(StringExpiration)
        out_file_add.write(StringPrice)
```
### 8. Delete window
```.py
def __init__(self, parent=None):
    super(delete, self).__init__(parent)
    self.setupUi(self)
    self.lineEdit.setPlaceholderText("Food Delete Name: ")

    self.buttonBox.clicked.connect(self.deletef)

def deletef(self):
    fn = "DataBase/NewFoodData.txt"
    f = open(fn, "r")                   #open the Database text file
    output = []                               
    string = self.lineEdit.text()
    for line in f:
        if not line.startswith(string):  #if the line not startwith the String Input, append it to the output list => The name             output.append(line)                 deleted will no longer in the list
    f.close()                  
    f = open(fn, "w")         
    f.writelines(output)    #Write the output list to the Database file
    f.close()
```
