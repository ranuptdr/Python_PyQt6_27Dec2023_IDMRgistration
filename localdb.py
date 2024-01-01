#import module
import sys  # sys is a built-in module in python
import uuid  # uuid is a built-in module in python
import sqlite3 #sqlite2 is a built-in module in python 
#import sqlite4 
import requests # requests is a 3rd party module in python

# from top-level module.submodul import  element1,element2,........
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon # PyQt6 is a 3rd party module in python

#return= module.method(actual argument)
conn  =  sqlite3.connect('ranu.db') # every function return something
cursor = conn.cursor() 

# Create a Table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,  -- Add TEXT here
        email TEXT NOT NULL,
        sno TEXT NOT NULL
    )
""")
conn.commit()

'''connId  =  sqlite4.connect("a.db")
print(connId)'''

#1. function defination is a one time process
def ranuLaptopHardwareId():
    hardwareid = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return hardwareid

def ranu(msg):
    co = QMessageBox()
    co.setText(msg)
    co.exec()

def sendDataa():
    print("Inside sendData function")
    data = {         #Key   :  Value
                "firstname": fname_input.text(),
                "lastname": lname_input.text(),
                "email": email_input.text(),
                "serial_number": snumber_input.text(),
            }
    cursor.execute("INSERT INTO user (first_name, last_name, email, sno) VALUES (?, ?, ?, ?)", (data["firstname"], data["lastname"], data["email"], data["serial_number"]))
    conn.commit()
    QMessageBox.information(None, "Success", "Data Saved Successfully")

    '''hardId = ranuLaptopHardwareId()
    api_url = 'http://localhost:1337/api/registrations'
    response2 = requests.get(api_url+f'?filters[hardwareid][$eq]={hardId}')

    
    json_data = response2.json()
    print("JSON Data:", json_data["meta"]["pagination"]["total"])
    if json_data["meta"]["pagination"]["total"]==0:
        payload = {
            "data": {
                "firstname": fname_input.text(),
                "lastname": lname_input.text(),
                "email": email_input.text(),
                "serial_number": snumber_input.text(),
                "hardwareId": ranuLaptopHardwareId(),
            }
        }

        response = requests.post(api_url, json=payload)

        if response.status_code == 200:
            ranu("Registration successful")
        else:
            ranu("Registration not successful")

    else:
        co2 = QMessageBox()
        co2.setText(f"User is already registered with hardwareid {hardId}")
        co2.exec()'''
    pass

#2. create a class object
#ceo = ClassName(actual argument) 
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QGridLayout') # ceo.method()

iconCO = QIcon('./icon.png')
window.setWindowIcon(iconCO)  # ceo.method()

button1 = QPushButton('Save')
button2 = QPushButton("How To License")
button3 = QPushButton("Cancle")

fname = QLabel("First Name")
lname = QLabel("Last Name")
email = QLabel("Email")
snumber = QLabel("Serial number")

fname_input = QLineEdit()
lname_input = QLineEdit()
email_input = QLineEdit()
snumber_input = QLineEdit()

layout = QGridLayout()

layout.addWidget(fname, 0, 0)
layout.addWidget(fname_input, 0, 1)
layout.addWidget(lname, 1, 0)
layout.addWidget(lname_input, 1, 1)
layout.addWidget(email, 2, 0)
layout.addWidget(email_input, 2, 1)
layout.addWidget(snumber, 3, 0) 
layout.addWidget(snumber_input, 3, 1) 
layout.addWidget(button1, 4, 0)
layout.addWidget(button2, 4, 1)
layout.addWidget(button3, 4, 2)


window.setLayout(layout)  # ceo.method()

#widget.signal.connect(slot_function)
button1.clicked.connect(sendDataa)

window.show()  # ceo.method()
app.exec()  # ceo.method()
