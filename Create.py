import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
from PyQt5.QtWidgets import QMessageBox

from datetime import datetime
from pymongo import MongoClient
from Modules import AnimalShelter
# MongoDB database
client = MongoClient('mongodb://localhost:27017')
database = client["AAC"]
collection = database["animals"]


class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("Create a Document")

        form_layout = qtw.QFormLayout(self)
        self.setLayout(form_layout)

        # Add Stuff/Widgets
        label_1 = qtw.QLabel("Enter data for new document")
        label_1.setFont(qtg.QFont("Helvetica", 24))
        ID = qtw.QLineEdit(self)
        Name = qtw.QLineEdit(self)
        DOB = qtw.QLineEdit(self)
        Outcome = qtw.QLineEdit(self)
        AnimalType = qtw.QLineEdit(self)
        Gender = qtw.QLineEdit(self)
        Fixed = qtw.QLineEdit(self)
        Age = qtw.QLineEdit(self)
        Breed = qtw.QLineEdit(self)
        Color = qtw.QLineEdit(self)
        label_2 = qtw.QLabel("")
        label_2.setFont(qtg.QFont("Helvetica", 14))

        # Add Rows To App
        form_layout.addRow(label_1)
        form_layout.addRow("Animal ID", ID)
        form_layout.addRow("Animal Name", Name)
        form_layout.addRow("Date of Birth", DOB)
        form_layout.addRow("Outcome Type", Outcome)
        form_layout.addRow("Animal Type", AnimalType)
        form_layout.addRow("Gender", Gender)
        form_layout.addRow("Age", Age)
        form_layout.addRow("Animal Breed", Breed)
        form_layout.addRow("Animal Color", Color)
        form_layout.addRow(qtw.QPushButton("Submit",
                                           clicked=lambda: view()))
        form_layout.addRow(label_2)
        form_layout.addRow(qtw.QPushButton("Create",
                                           clicked=lambda: submit()))

        # Show the app
        self.show()

        def view():
            label_2.setText(f'You entered: \nAnimal ID: {ID.text()} \nAnimal Name: {Name.text()} \nDate of Birth: '
                            f'{DOB.text()} \nOutcome Type: {Outcome.text()} \nAnimal Type: {AnimalType.text()} \n'
                            f'Sex: {Gender.text()} \nAge: {Age.text()} \nAnimal Breed: {Breed.text()} '
                            f'\nAnimal Color: {Color.text()}')

        def submit():
            my_dict = {
                "Animal ID": str(ID),
                "Name": str(Name),
                "DateTime": str(datetime.utcnow()),
                "MonthYear": str(datetime.utcnow()),
                "Date of Birth": str(DOB),
                "Outcome Type": str(Outcome),
                "Animal Type": str(AnimalType),
                "Sex upon Outcome": str(Gender),
                "Age upon Outcome": str(Age),
                "Breed": str(Breed),
                "Color": str(Color)
            }
            AnimalShelter.create(my_dict)

            # Pop up box
            msg = QMessageBox()
            msg.setWindowTitle("Saved")
            msg.setText("Entered Data Saved To AAC Database")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

            # Clear old values
            ID.setText("")
            Name.setText("")
            DOB.setText("")
            Outcome.setText("")
            AnimalType.setText("")
            Gender.setText("")
            Fixed.setText("")
            Age.setText("")
            Breed.setText("")
            Color.setText("")
            label_2.setText("")


app = qtw.QApplication([])
mw = MainWindow()

# Run The App
app.exec_()