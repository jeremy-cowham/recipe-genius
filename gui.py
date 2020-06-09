import sys
from recipe import Recipe

from PySide2.QtWidgets import (QMainWindow, QWidget, QLabel, QFormLayout, QLineEdit, QPushButton,
    QGroupBox, QTableWidget, QVBoxLayout, QHBoxLayout, QApplication, QGridLayout, QTableWidgetItem)
from PySide2.QtGui import QPixmap

class MainWindow(QMainWindow):

    def __init__(self, recipe):
        super().__init__()

        # setup
        self.setWindowTitle("Recipe Genius")
        self.mainWidget = QWidget()
        self.setCentralWidget(self.mainWidget)
        self.ingredientList = set()

        # images
        self.title = QLabel("No recipe loaded")
        self.pixmap = QPixmap()
        self.image = QLabel("No picture loaded")

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
        self.submitButton.clicked.connect(self.submitIngredients)

        # left layout (adding ingredients)
        self.leftLayout = QVBoxLayout()
        self.leftLayout.addWidget(self.formBox)
        self.leftLayout.addWidget(self.ingredientTable)
        self.leftLayout.addWidget(self.submitButton)

        # bottom right layout (recipe tables)
        self.usedTable = QTableWidget()
        self.usedTable.setColumnCount(3)
        self.usedTable.setHorizontalHeaderLabels(["Used ingredient", "Amount", "Unit"])
        
        self.missedTable = QTableWidget()
        self.missedTable.setColumnCount(3)
        self.missedTable.setHorizontalHeaderLabels(["Missed ingredient", "Amount", "Unit"])

        self.bottomRightLayout = QHBoxLayout()
        self.bottomRightLayout.addWidget(self.usedTable)
        self.bottomRightLayout.addWidget(self.missedTable)

        # right layout (recipe)
        self.rightLayout = QVBoxLayout()
        self.rightLayout.addWidget(self.title)
        self.rightLayout.addWidget(self.image)
        self.rightLayout.addLayout(self.bottomRightLayout)

        # main layout
        self.mainLayout = QGridLayout()
        self.mainLayout.addLayout(self.leftLayout, 0, 0, 1, 2)
        self.mainLayout.addLayout(self.rightLayout, 0, 2, 1, 1)
        self.centralWidget().setLayout(self.mainLayout)

        self.processRecipe(recipe)

    # functions
    def addIngredient(self):
        ingredient = self.ingredientInput.text().strip().lower()
        if ingredient not in self.ingredientList:
            rowIndex = self.ingredientTable.rowCount()
            self.ingredientTable.insertRow(rowIndex)
            self.ingredientTable.setItem(rowIndex, 0, QTableWidgetItem(ingredient))
            self.ingredientList.add(ingredient)
        self.ingredientInput.clear()

    def submitIngredients(self):
        self.ingredientTable.setRowCount(0)
        recipe = Recipe.get_top_recipe_by_ingredients(self.ingredientList)
        self.ingredientList.clear()
        self.processRecipe(recipe)

    def processRecipe(self, recipe):
        self.usedTable.setRowCount(0)
        self.missedTable.setRowCount(0)
        if recipe is None:
            self.title.setText("No recipe found. Please try again.")
            self.image.setText(" ")
        else:
            self.title.setText(recipe.title)
            self.pixmap.loadFromData(recipe.image)
            self.image.setPixmap(self.pixmap)
            self.insertIngredients(self.usedTable, recipe.used_ingredients)
            self.insertIngredients(self.missedTable, recipe.missed_ingredients)

    def insertIngredients(self, table, ingredients):
        rowIndex = table.rowCount()
        for ingredient in ingredients:
            table.insertRow(rowIndex)
            table.setItem(rowIndex, 0, QTableWidgetItem(ingredient.name))
            table.setItem(rowIndex, 1, QTableWidgetItem(str(ingredient.amount)))
            table.setItem(rowIndex, 2, QTableWidgetItem(ingredient.unit))
            rowIndex += 1

def runGui(recipe=None):
    app = QApplication(sys.argv)
    mainWindow = MainWindow(recipe)
    mainWindow.showNormal()
    sys.exit(app.exec_())

if __name__ == '__main__':
    runGui()
