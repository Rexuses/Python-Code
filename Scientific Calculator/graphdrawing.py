from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtQuickWidgets
from PyQt5.QtWidgets import QLabel
ans=0
result_list=[]
class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.Buttons()
        self.x=np.arange(0,0)
    def Buttons(self):
        self.resize(602, 385)
        self.label_equation = QLabel(self)
        self.label_equation.setVisible(False)
        self.pushButton_leftparant = QtWidgets.QPushButton(self)
        self.pushButton_leftparant.setGeometry(QtCore.QRect(90, 80, 111, 31))
        self.pushButton_leftparant.setObjectName("pushButton_leftparant")
        self.pushButton_rightparant = QtWidgets.QPushButton(self)
        self.pushButton_rightparant.setGeometry(QtCore.QRect(210, 80, 111, 31))
        self.pushButton_rightparant.setObjectName("pushButton_rightparant")
        self.pushButton_del = QtWidgets.QPushButton(self)
        self.pushButton_del.setGeometry(QtCore.QRect(330, 80, 111, 31))
        self.pushButton_del.setObjectName("pushButton_del")
        self.pushButton_ac = QtWidgets.QPushButton(self)
        self.pushButton_ac.setGeometry(QtCore.QRect(450, 80, 111, 31))
        self.pushButton_ac.setObjectName("pushButton_ac")
        self.pushButton_7 = QtWidgets.QPushButton(self)
        self.pushButton_7.setGeometry(QtCore.QRect(90, 120, 111, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_div = QtWidgets.QPushButton(self)
        self.pushButton_div.setGeometry(QtCore.QRect(450, 120, 111, 31))
        self.pushButton_div.setObjectName("pushButton_div")
        self.pushButton_9 = QtWidgets.QPushButton(self)
        self.pushButton_9.setGeometry(QtCore.QRect(330, 120, 111, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self)
        self.pushButton_8.setGeometry(QtCore.QRect(210, 120, 111, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_4 = QtWidgets.QPushButton(self)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 160, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_prod = QtWidgets.QPushButton(self)
        self.pushButton_prod.setGeometry(QtCore.QRect(450, 160, 111, 31))
        self.pushButton_prod.setObjectName("pushButton_prod")
        self.pushButton_6 = QtWidgets.QPushButton(self)
        self.pushButton_6.setGeometry(QtCore.QRect(330, 160, 111, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_5 = QtWidgets.QPushButton(self)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 160, 111, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_1 = QtWidgets.QPushButton(self)
        self.pushButton_1.setGeometry(QtCore.QRect(90, 200, 111, 31))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_plus = QtWidgets.QPushButton(self)
        self.pushButton_plus.setGeometry(QtCore.QRect(450, 200, 111, 31))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_3 = QtWidgets.QPushButton(self)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 200, 111, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_0 = QtWidgets.QPushButton(self)
        self.pushButton_0.setGeometry(QtCore.QRect(90, 240, 111, 31))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_draw = QtWidgets.QPushButton(self)
        self.pushButton_draw.setGeometry(QtCore.QRect(450, 240, 111, 31))
        self.pushButton_draw.setObjectName("pushButton_draw")
        self.pushButton_minus = QtWidgets.QPushButton(self)
        self.pushButton_minus.setGeometry(QtCore.QRect(330, 240, 111, 31))
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_dot = QtWidgets.QPushButton(self)
        self.pushButton_dot.setGeometry(QtCore.QRect(210, 240, 111, 31))
        self.pushButton_dot.setObjectName("pushButton_dot")
        self.spinBoxmin = QtWidgets.QSpinBox(self)
        self.spinBoxmin.setGeometry(QtCore.QRect(255, 300, 42, 22))
        self.spinBoxmin.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.spinBoxmin.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.spinBoxmin.setMinimum(-5000)
        self.spinBoxmin.setMaximum(5000)
        self.spinBoxmin.setObjectName("spinBoxmin")
        self.spinBoxmax = QtWidgets.QSpinBox(self)
        self.spinBoxmax.setGeometry(QtCore.QRect(320, 300, 42, 22))
        self.spinBoxmax.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.spinBoxmax.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.spinBoxmax.setMinimum(-5000)
        self.spinBoxmax.setMaximum(5000)
        self.spinBoxmax.setObjectName("spinBoxmax")
        self.pushButton_range = QtWidgets.QPushButton(self)
        self.pushButton_range.setGeometry(QtCore.QRect(380, 300, 75, 23))
        self.pushButton_range.setObjectName("pushButton_range")
        self.pushButton_x = QtWidgets.QPushButton(self)
        self.pushButton_x.setGeometry(QtCore.QRect(0, 150, 81, 31))
        self.pushButton_x.setObjectName("pushButton_x")
        self.pushButton_us = QtWidgets.QPushButton(self)
        self.pushButton_us.setGeometry(QtCore.QRect(0, 200, 81, 31))
        self.pushButton_us.setObjectName("pushButton_us")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(90, 20, 468, 41))
        self.label.setText("")
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid orange;"
                                 "background : white;"
                                 "}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(250, 330, 47, 13))
        self.label_2.setContextMenuPolicy(QtCore.Qt.PreventContextMenu)
        self.label_2.setToolTipDuration(-4)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(313, 330, 47, 14))
        self.label_3.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.label_3.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_3.setObjectName("label_3")

        self.pushButton_x.clicked.connect(self.action_x)
        self.pushButton_us.clicked.connect(self.action_us)
        self.pushButton_range.clicked.connect(self.action_range)



        self.pushButton_leftparant.clicked.connect(self.action_leftparant)
        self.pushButton_rightparant.clicked.connect(self.action_rightparant)
        self.pushButton_del.clicked.connect(self.action_clear)
        self.pushButton_ac.clicked.connect(self.action_allclear)

        self.pushButton_7.clicked.connect(self.action_7)
        self.pushButton_8.clicked.connect(self.action_8)
        self.pushButton_9.clicked.connect(self.action_9)
        self.pushButton_div.clicked.connect(self.action_divd)

        self.pushButton_4.clicked.connect(self.action_4)
        self.pushButton_5.clicked.connect(self.action_5)
        self.pushButton_6.clicked.connect(self.action_6)
        self.pushButton_prod.clicked.connect(self.action_mult)

        self.pushButton_1.clicked.connect(self.action_1)
        self.pushButton_2.clicked.connect(self.action_2)
        self.pushButton_3.clicked.connect(self.action_3)
        self.pushButton_plus.clicked.connect(self.action_plus)

        self.pushButton_0.clicked.connect(self.action_0)
        self.pushButton_dot.clicked.connect(self.action_dot)
        self.pushButton_minus.clicked.connect(self.action_minus)
        self.pushButton_draw.clicked.connect(self.action_draw)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Graph"))
        self.pushButton_leftparant.setText(_translate("Form", "("))
        self.pushButton_rightparant.setText(_translate("Form", ")"))
        self.pushButton_del.setText(_translate("Form", "DEL"))
        self.pushButton_ac.setText(_translate("Form", "AC"))
        self.pushButton_7.setText(_translate("Form", "7"))
        self.pushButton_div.setText(_translate("Form", "÷"))
        self.pushButton_9.setText(_translate("Form", "9"))
        self.pushButton_8.setText(_translate("Form", "8"))
        self.pushButton_4.setText(_translate("Form", "4"))
        self.pushButton_prod.setText(_translate("Form", "X"))
        self.pushButton_6.setText(_translate("Form", "6"))
        self.pushButton_5.setText(_translate("Form", "5"))
        self.pushButton_1.setText(_translate("Form", "1"))
        self.pushButton_plus.setText(_translate("Form", "+"))
        self.pushButton_3.setText(_translate("Form", "3"))
        self.pushButton_2.setText(_translate("Form", "2"))
        self.pushButton_0.setText(_translate("Form", "0"))
        self.pushButton_draw.setText(_translate("Form", "Draw"))
        self.pushButton_minus.setText(_translate("Form", "-"))
        self.pushButton_dot.setText(_translate("Form", "."))
        self.pushButton_range.setText(_translate("Form", "Set Range"))
        self.pushButton_x.setText(_translate("Form", "x"))
        self.pushButton_us.setText(_translate("Form", "^"))
        self.label_2.setText(_translate("Form", "Min "))
        self.label_3.setText(_translate("Form", "Max"))

    def action_range(self):
        self.x=np.arange(int(self.spinBoxmin.text()),int(self.spinBoxmax.text()))
    def action_draw(self):
        graph=eval(self.label_equation.text())
        plt.plot(self.x,graph,"black")
        plt.show()

    def action_x(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "self.x")
        self.label.setText(text + "x")
    def action_us(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "**")
        self.label.setText(text + "^")
    def action_plus(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "+")
        self.label.setText(text + " + ")
    def action_minus(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "-")
        self.label.setText(text + " - ")

    def action_divd(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "/")
        self.label.setText(text + " / ")

    def action_mult(self):
        # appending label text

        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "*")
        self.label.setText(text + " * ")

    def action_dot(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + ".")
        self.label.setText(text + ".")

    def action_0(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "0")
        self.label.setText(text + "0")

    def action_1(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "1")
        self.label.setText(text + "1")

    def action_2(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "2")
        self.label.setText(text + "2")

    def action_3(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "3")
        self.label.setText(text + "3")

    def action_4(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "4")
        self.label.setText(text + "4")

    def action_5(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "5")
        self.label.setText(text + "5")

    def action_6(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "6")
        self.label.setText(text + "6")

    def action_7(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "7")
        self.label.setText(text + "7")

    def action_8(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "8")
        self.label.setText(text + "8")

    def action_9(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "9")
        self.label.setText(text+"9")
    def action_leftparant(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "(")
        self.label.setText(text + "(")
    def action_rightparant(self):
        # appending label text
        text          = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + ")")
        self.label.setText(text + ")")

    def action_allclear(self):
        # clearing the label text
        self.label_equation.setText("")
        self.label.setText("")

    def action_clear(self):
        # clearing a single digit
        text          = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])
        self.label_equation.setText(text[:len(text) - 1])

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())
