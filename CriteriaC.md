
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
### 6. Log in
Due to the user would like to be the exclusive user for this app so that the username and the password do not need to change. Hence, I will just check if the username and password input is mathched with the set username and password.

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
### 7. Add new food
The user wants to add the new food's properties: Name, Location, Quantity, Expiration and Price. Hence, writing the data input into database text file to help the user keep track of it. I also leave two "None" ones for the Day last used and amount last used due to when people add new food, the food has not been used yet so that these two information is not necessary to fill out in the add section and can be edited in the edit section.

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
    with open("Database/NewFoodData.csv", "a") as out_file_add:  # open the Database text file
        StringName = self.lineEdit.text() + ","  # Assign the input value
        StringLocation = self.lineEdit_2.text() + " "
        StringQuantity = self.lineEdit_3.text() + " "
        StringExpiration = self.lineEdit_4.text() + " "
        StringPrice = self.lineEdit_5.text() + " None" + " None" + "\n"

        out_file_add.write(StringName)  # Write the Input value to the Database text file
        out_file_add.write(StringLocation)
        out_file_add.write(StringQuantity)
        out_file_add.write(StringExpiration)
        out_file_add.write(StringPrice)
```
### 8. Delete the food
These codes will help user delete the information of the input food name. It will delete every information that are related to the food. The code will delete the information in the database file and also in the data table.

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
        if not line.startswith(string):  #if the line not startwith the String Input, append it to the output list => The name                                          # deleted will no longer in the list
        output.append(line)                                  
    f.close()                  
    f = open(fn, "w")         
    f.writelines(output)    #Write the output list to the Database file
    f.close()
```
### 9. Edit the food's information
The user wants to edit the information of the food in case of wrongly typing, or some information changed. So, the user will input the name of the food and choose the properties they want to change. The data in the database will be updated right after the button is clicked and also the data table.

```.py
def __init__(self, parent=None):
    super(edit, self).__init__(parent)
    self.setupUi(self)
    self.lineEdit.setPlaceholderText("The name of food: ")
    self.lineEdit_3.setPlaceholderText("New information: ")

    self.pushButton_2.clicked.connect(self.exit_editf)
    self.pushButton.clicked.connect(self.editf)

def exit_editf(self):
    self.close()

def editf(self):
    words = []
    output = []
    output_2 = []
    with open("DataBase/NewFoodData.csv", "r") as database:  # Open the database text file
        for line in database:  # loop through all the lines in the text file
            if self.lineEdit.text() in line:  # If found the Name Of the Food in the line, choose that line
                for word in line.split():  # Split that line into elements of a list
                    words.append(word)
                for i in range(
                        4):  # To have space for Date last used, Amount last used (Add food does not add these two)
                    words.append(" ")
                if self.comboBox.currentText() == "Name":  # Check which item did the user choose, and assign appropriate value
                    words[0] = self.lineEdit_3.text()  # to the item.
                elif self.comboBox.currentText() == "Location":
                    words[1] = self.lineEdit_3.text()
                elif self.comboBox.currentText() == "Quantity":
                    if self.lineEdit_3.text().isdecimal():  # Check if the input value is number or not
                        words[2] = self.lineEdit_3.text()
                    else:
                        self.lineEdit_3.setText("Invalid value!")
                elif self.comboBox.currentText() == "Expiration":
                    words[3] = self.lineEdit_3.text()
                elif self.comboBox.currentText() == "Price":
                    if self.lineEdit_3.text().isdecimal():
                        words[4] = self.lineEdit_3.text()
                    else:
                        self.lineEdit_3.setText("Invalid value!")
                elif self.comboBox.currentText() == "Date last used":
                    words[5] = self.lineEdit_3.text()
                elif self.comboBox.currentText() == "Amount last used":
                    if self.lineEdit_3.text().isdecimal():
                        words[6] = self.lineEdit_3.text()
                    else:
                        self.lineEdit_3.setText("Invalid value!")

            if not line.startswith(self.lineEdit.text()):
                output.append(line)
    database.close()

    with open("DataBase/NewFoodData.csv", "w") as outfile:
        outfile.writelines(output)  # Delete the line contain the Name of the food
        print("\n")
        for str in words:  # Print the new line with new information
            outfile.write(str + " ")
```
### 10. Load the food information to the QWidgetTable
The food data table will help the user to keep track of all the food he has. He will know all the name of the food he has and the properties related to them.

```.
class list_food(List_food):
    def __init__(self, parent=None):
        super(list_food, self).__init__(parent)
        self.setupUi(self)
        self.data = self.load_data()
        self.pushButton.clicked.connect(self.exit_listf)   # Connect the button to function

    def load_data(self):
        with open("DataBase/NewFoodData.csv") as mydatabase:   # Open the file 
            file = csv.reader(mydatabase, delimiter=",")    # Split the data by the ","
            for i, row in enumerate(file):           
                for j, col in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(col)) # Set the data to the table

        return []

    def exit_listf(self):   # close the dialog
        self.close()
```
### 11.Summary 
The summary dialog will summarize the total money,quantity or amount used of all the food he has. By taking the data from the database file, I will take out the information of the properties he chooses to summarize and calculate the sum of them.

```.py
def __init__(self, parent=None):
    super(summary, self).__init__(parent)
    self.setupUi(self)
    self.lineEdit.setPlaceholderText("Properties Summary: ")

    self.pushButton.clicked.connect(self.summarize)

def summarize(self):
    quantity = 0
    money = 0
    amount_used = 0
    with open("DataBase/NewFoodData.csv", "r") as data:  # Open the data file
        words = []
        file = csv.reader(data, delimiter=",")
        for row in file:
            for col in row:
                words.append(col)
        if self.comboBox.currentText() == "Quantity":
            for i in range(2, len(words), 7):  # Get the values of quantity in the list
                quantity = quantity + int(words[i])  # Calculate the quantity
                self.label_2.setText("Result: {}".format(quantity))  # Print out the result
        elif self.comboBox.currentText() == "Amount used":
            for i in range(6, len(words), 7):
                if words[i] == "None":
                    words[i] = 0
                amount_used = amount_used + int(words[i])
                print(amount_used)
                self.label_2.setText("Result: {}".format(amount_used))
        else:
            for i in range(4, len(words), 7):
                money = money + int(words[i])
                self.label_2.setText("Result: {}".format(money))
```
### 12.Search Food
Search Food Dialog will help the user find all the information of the input food. I will take the data of the food in the databse file and print out the food information into a table 

```.py
class search_food(Search):
    def __init__(self, parent=None):
        super(search_food, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Search)

    def Search(self):

        with open("DataBase/NewFoodData.csv", "r") as data:  # Open the data file
            output = []
            for line in data:
                if line.startswith(self.lineEdit.text()):    #Check if the food is on the list
                    output.append(line)                 #Append the information of food to the list
                    self.lineEdit_3.setText("The information for the food is below:")
                else:                     
                    self.lineEdit_3.setText("The food is not on the list")

        data.close()
        with open("DataBase/SearchFoodData.csv", "w") as NF_data:    
            for str in output:             #Write the information of the food into a Search Food Data file
                NF_data.write(str)
        NF_data.close()
        with open("DataBase/SearchFoodData.csv") as mydatabase:          
            file = csv.reader(mydatabase, delimiter=" ")
            for i, row in enumerate(file):    #Showing the data from the csv file to the table
                for j, col in enumerate(row):
                    self.tableWidget.setItem(i, j, QTableWidgetItem(col))
```
