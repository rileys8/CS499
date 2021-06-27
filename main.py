import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import main

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        # Add a title
        self.setWindowTitle("Austin Animal Center Database")

        # Set layout
        self.setLayout(qtw.QVBoxLayout())

        # Create Label
        my_label = qtw.QLabel("Pick from list")
        self.layout().addWidget(my_label)
        # Change font
        my_label.setFont(qtg.QFont('Helvetica', 24))
        self.layout().addWidget(my_label)

        # Create combo box
        my_combo = qtw.QComboBox(self)
        # Add items to combo box
        my_combo.addItem("Add new animal")
        my_combo.addItem("Search for an animal")
        my_combo.addItem("Update an animal file")
        my_combo.addItem("Delete an animal file")
        # Put combobox on screen
        self.layout().addWidget(my_combo)

        # Create a button
        my_button = qtw.QPushButton("Press Me!", clicked = lambda: press_it())
        self.layout().addWidget(my_button )

        # Show the app
        self.show()

        def press_it():
            # Add name to label
            my_label.setText(f'{str(my_combo.currentText())}')


app = qtw.QApplication([])
mw = MainWindow()

# Run App
app.exec_()