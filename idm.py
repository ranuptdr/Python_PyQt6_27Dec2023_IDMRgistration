import sys
import uuid
import requests
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtGui import QIcon

def ranuLaptopHardwareId():
    hardwareid = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return hardwareid

def ranu(msg):
    co = QMessageBox()
    co.setText(msg)
    co.exec()

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QGridLayout')

iconCO = QIcon('./icon.png')
window.setWindowIcon(iconCO)

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


window.setLayout(layout)

def sendDataa():
    print("Inside sendData function")
    hardId = ranuLaptopHardwareId()
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
        co2.exec()


button1.clicked.connect(sendDataa)

window.show()
app.exec()
