import sys

from PySide2.QtWidgets import (QMainWindow, QWidget, QLabel, QFormLayout, QLineEdit, QPushButton,
    QGroupBox, QTableWidget, QVBoxLayout, QHBoxLayout, QApplication, QGridLayout, QTableWidgetItem)
from PySide2.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        # setup
        self.setWindowTitle("Recipe Genius")
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)
        self.ingredientList = list()

        # images
        self.pixmap = QPixmap()
        self.image = QLabel("No recipe loaded")

        # ingredient form
        self.formBox = QGroupBox("Enter ingredients")
        self.formLayout = QFormLayout()
        self.ingredientInput = QLineEdit()
        self.formLayout.addRow(QLabel("Ingredient:"), self.ingredientInput)
        self.addButton = QPushButton("Add ingredient")
        self.addButton.clicked.connect(self.addIngredient)
        self.formLayout.addRow(self.addButton)
        self.formBox.setLayout(self.formLayout)

        # ingredient table
        self.ingredientTable = QTableWidget()
        self.ingredientTable.setColumnCount(1)
        self.ingredientTable.setHorizontalHeaderLabels(["Ingredients list"])
        self.submitButton = QPushButton("Submit ingredients")

        # left layout (adding ingredients)
        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.formBox)
        self.leftLayout.addWidget(self.ingredientTable)
        self.leftLayout.addWidget(self.submitButton)

        # bottom right layout (recipe tables)
        self.usedTable = QTableWidget()
        self.usedTable.setColumnCount(3)
        self.usedTable.setHorizontalHeaderLabels(["Used ingredients", "Amount", "Units"])
        
        self.missedTable = QTableWidget()
        self.missedTable.setColumnCount(3)
        self.missedTable.setHorizontalHeaderLabels(["Missed ingredients", "Amount", "Units"])

        self.bottomRightLayout = QHBoxLayout()
        self.bottomRightLayout.addWidget(self.usedTable)
        self.bottomRightLayout.addWidget(self.missedTable)

        # right layout (recipe)
        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(self.image)
        self.rightLayout.addLayout(self.bottomRightLayout)

        # main layout
        self.mainLayout = QGridLayout()
        self.mainLayout.addLayout(self.leftLayout, 0, 0, 1, 2)
        self.mainLayout.addLayout(self.rightLayout, 0, 2, 1, 1)
        self.centralWidget().setLayout(self.mainLayout)

    # functions
    def addIngredient(self):
        ingredient = self.ingredientInput.text().strip().lower()
        self.ingredientList.append(ingredient)
        rowIndex = self.ingredientTable.rowCount()
        self.ingredientTable.insertRow(rowIndex)
        self.ingredientTable.setItem(rowIndex, 0, QTableWidgetItem(ingredient))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.showNormal()
    sys.exit(app.exec_())
