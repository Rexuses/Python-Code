from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from math import *
import sys
import numpy as np
import graphdrawing
import Scientific
import Standard


ans=0
result_list=[]
class Window(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Calculator")
        self.setGeometry(100,100,280,430)
        self.setMinimumSize(280,430)
        self.setMaximumSize(280, 430)

        self.setStyleSheet("QMainWindow"
                                 "{"
                                 "background : gray;"
                                 "}")

        menubar               = self.menuBar()
        settings              = menubar.addMenu("Settings")
        standard_calculator   = QAction("Standard Calculator",self)
        scientific_calculator = QAction("Scientific Calculator",self)
        graph_drawing = QAction("Graph Drawing", self)
        exit=QAction("Exit",self)

        settings.addAction(standard_calculator)
        standard_calculator.setShortcut("Ctrl+Q")
        settings.addAction(scientific_calculator)
        scientific_calculator.setShortcut("Ctrl+S")
        settings.addAction(graph_drawing)
        graph_drawing.setShortcut("Ctrl+G")
        settings.addAction(exit)
        exit.setShortcut("Ctrl+E")

        standard_calculator.triggered.connect(self.standard)
        scientific_calculator.triggered.connect(self.scientific)
        graph_drawing.triggered.connect(self.graph)
        exit.triggered.connect(self.quit)

        self.standard()

        self.show()

    def standard(self):
        self.standard_calculator=Standard.Standard_Calc()
        self.setCentralWidget(self.standard_calculator)
        self.setMaximumSize(280,430)
        self.setMinimumSize(280,430)
        self.resize(280,430)
        self.setWindowTitle("Calculator")

    def scientific(self):
        self.scientific_calculator = Scientific.Scientific_Calc()
        self.setCentralWidget(self.scientific_calculator)
        self.setMaximumSize(561,430)
        self.setMinimumSize(561,430)
        self.resize(561,430)
        self.setWindowTitle("Scientific Calculator")
    def graph(self):
        self.graph = graphdrawing.Ui_Form()
        self.setMaximumSize(602, 385)
        self.setMinimumSize(602, 385)
        self.resize(602, 385)
        self.setWindowTitle("Graph")
        self.setCentralWidget(self.graph)
    def quit(self):
        qApp.exit()




app = QApplication(sys.argv)
window=Window()
sys.exit(app.exec_())
