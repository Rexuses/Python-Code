from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from math import *
import graphdrawing
import sys
import numpy as np
from PyQt5 import QtWidgets


ans=0
result_list=[]
class Scientific_Calc(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(561, 430)
        self.setMinimumSize(561, 430)
        self.resize(561, 430)
        self.buttons_and_label()
    def buttons_and_label(self):
        self.label = QLabel(self)
        self.label_equation = QLabel(self)
        self.label_equation.setVisible(False)
        self.label.setGeometry(1, 30, 280, 70)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid orange;"
                                 "background : white;"
                                 "}")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont("Arial", 15))

        # Buttons

        buttonleftparant = QPushButton("(", self)
        buttonleftparant.setGeometry(1, 100, 70, 65)
        buttonrightparant = QPushButton(")", self)
        buttonrightparant.setGeometry(71, 100, 70, 65)
        buttonclear = QPushButton("DEL", self)
        buttonclear.setGeometry(141, 100, 70, 65)
        buttonclear.setStyleSheet("QPushButton"
                                  "{"
                                  "background : orange;"
                                  "}")
        buttonallclear = QPushButton("AC", self)
        buttonallclear.setGeometry(211, 100, 70, 65)
        buttonallclear.setStyleSheet("QPushButton"
                                     "{"
                                     "background : orange;"
                                     "}")

        button7 = QPushButton("7", self)
        button7.setGeometry(1, 160, 70, 65)
        button8 = QPushButton("8", self)
        button8.setGeometry(71, 160, 70, 65)
        button9 = QPushButton("9", self)
        button9.setGeometry(141, 160, 70, 65)
        buttondivd = QPushButton("÷", self)
        buttondivd.setGeometry(211, 160, 70, 65)
        buttondivd.setStyleSheet("QPushButton"
                                 "{"
                                 "background : #C0C0C0;"
                                 "}")

        button4 = QPushButton("4", self)
        button4.setGeometry(1, 220, 70, 65)
        button5 = QPushButton("5", self)
        button5.setGeometry(71, 220, 70, 65)
        button6 = QPushButton("6", self)
        button6.setGeometry(141, 220, 70, 65)
        buttonmult = QPushButton("X", self)
        buttonmult.setGeometry(211, 220, 70, 65)
        buttonmult.setStyleSheet("QPushButton"
                                 "{"
                                 "background : #C0C0C0;"
                                 "}")

        button1 = QPushButton("1", self)
        button1.setGeometry(1, 280, 70, 65)
        button2 = QPushButton("2", self)
        button2.setGeometry(71, 280, 70, 65)
        button3 = QPushButton("3", self)
        button3.setGeometry(141, 280, 70, 65)
        buttonplus = QPushButton("+", self)
        buttonplus.setGeometry(211, 280, 70, 65)
        buttonplus.setStyleSheet("QPushButton"
                                 "{"
                                 "background :#C0C0C0;"
                                 "}")

        button0 = QPushButton("0", self)
        button0.setGeometry(1, 340, 70, 65)
        buttondot = QPushButton(".", self)
        buttondot.setGeometry(71, 340, 70, 65)
        buttonminus = QPushButton("-", self)
        buttonminus.setGeometry(141, 340, 70, 65)
        buttonminus.setStyleSheet("QPushButton"
                                  "{"
                                  "background :#C0C0C0;"
                                  "}")
        buttonequal = QPushButton("=", self)
        buttonequal.setGeometry(211, 340, 70, 65)
        buttonequal.setStyleSheet("QPushButton"
                                  "{"
                                  "background : #C0C0C0;"
                                  "}")
        # Scientific Buttons
        buttonsin = QPushButton("sin", self)
        buttonsin.setGeometry(281, 100, 70, 65)
        buttonsin.setStyleSheet("QPushButton"
                                "{"
                                "background : #C0C0C0;"
                                "}")
        buttoncos = QPushButton("cos", self)
        buttoncos.setGeometry(351, 100, 70, 65)
        buttoncos.setStyleSheet("QPushButton"
                                "{"
                                "background : #C0C0C0;"
                                "}")
        buttontan = QPushButton("tan", self)
        buttontan.setGeometry(421, 100, 70, 65)
        buttontan.setStyleSheet("QPushButton"
                                "{"
                                "background : #C0C0C0;"
                                "}")
        buttonpi = QPushButton("π", self)
        buttonpi.setGeometry(491, 100, 70, 65)
        buttonpi.setStyleSheet("QPushButton"
                               "{"
                               "background : #C0C0C0;"
                               "}")

        buttonasin = QPushButton("Arc sin", self)
        buttonasin.setGeometry(281, 160, 70, 65)
        buttonasin.setStyleSheet("QPushButton"
                                 "{"
                                 "background : #C0C0C0;"
                                 "}")
        buttonacos = QPushButton("Arc cos", self)
        buttonacos.setGeometry(351, 160, 70, 65)
        buttonacos.setStyleSheet("QPushButton"
                                 "{"
                                 "background : #C0C0C0;"
                                 "}")
        buttonatan = QPushButton("Arc tan", self)
        buttonatan.setGeometry(421, 160, 70, 65)
        buttonatan.setStyleSheet("QPushButton"
                                 "{"
                                 "background : #C0C0C0;"
                                 "}")
        buttone = QPushButton("e", self)
        buttone.setGeometry(491, 160, 70, 65)
        buttone.setStyleSheet("QPushButton"
                              "{"
                              "background : #C0C0C0;"
                              "}")

        buttonsqrt = QPushButton("√", self)
        buttonsqrt.setGeometry(281, 220, 70, 65)
        buttonsqrt.setStyleSheet("QPushButton"
                                 "{"
                                 "background : #C0C0C0;"
                                 "}")
        buttonpow = QPushButton("xʸ", self)
        buttonpow.setGeometry(351, 220, 70, 65)
        buttonpow.setStyleSheet("QPushButton"
                                "{"
                                "background : #C0C0C0;"
                                "}")
        buttondeg = QPushButton("deg", self)
        buttondeg.setGeometry(421, 220, 70, 65)
        buttondeg.setStyleSheet("QPushButton"
                                "{"
                                "background : #C0C0C0;"
                                "}")
        buttonfact = QPushButton("!", self)
        buttonfact.setGeometry(491, 220, 70, 65)
        buttonfact.setStyleSheet("QPushButton"
                                 "{"
                                 "background : #C0C0C0;"
                                 "}")

        buttonlog2 = QPushButton("log2", self)
        buttonlog2.setGeometry(281, 280, 70, 65)
        buttonlog2.setStyleSheet("QPushButton"
                                 "{"
                                 "background : #C0C0C0;"
                                 "}")
        buttonlog10 = QPushButton("log10", self)
        buttonlog10.setGeometry(351, 280, 70, 65)
        buttonlog10.setStyleSheet("QPushButton"
                                  "{"
                                  "background : #C0C0C0;"
                                  "}")
        buttonlog = QPushButton("log", self)
        buttonlog.setGeometry(421, 280, 70, 65)
        buttonlog.setStyleSheet("QPushButton"
                                "{"
                                "background : #C0C0C0;"
                                "}")
        buttoncomma = QPushButton(",", self)
        buttoncomma.setGeometry(491, 280, 70, 65)
        buttoncomma.setStyleSheet("QPushButton"
                                  "{"
                                  "background : #C0C0C0;"
                                  "}")

        button2pi = QPushButton("2π", self)
        button2pi.setGeometry(281, 340, 70, 65)
        button2pi.setStyleSheet("QPushButton"
                                "{"
                                "background : #C0C0C0;"
                                "}")
        buttonrad = QPushButton("Rad", self)
        buttonrad.setGeometry(351, 340, 70, 65)
        buttonrad.setStyleSheet("QPushButton"
                                "{"
                                "background : #C0C0C0;"
                                "}")
        buttonexp = QPushButton("Exp", self)
        buttonexp.setGeometry(421, 340, 70, 65)
        buttonexp.setStyleSheet("QPushButton"
                                "{"
                                "background : #C0C0C0;"
                                "}")
        buttongamma = QPushButton("Gamma", self)
        buttongamma.setGeometry(491, 340, 70, 65)
        buttongamma.setStyleSheet("QPushButton"
                                  "{"
                                  "background : #C0C0C0;"
                                  "}")

        self.radioradian = QRadioButton("Radian", self)
        self.radioradian.setGeometry(300, 50, 60, 60)
        self.radioradian.setChecked(True)
        self.radiodegree = QRadioButton("Degree", self)
        self.radiodegree.setGeometry(400, 50, 60, 60)

        # adding action to each of the button

        buttonleftparant.clicked.connect(self.action_leftparant)
        buttonrightparant.clicked.connect(self.action_rightparant)
        buttonclear.clicked.connect(self.action_clear)
        buttonallclear.clicked.connect(self.action_allclear)

        button7.clicked.connect(self.action_7)
        button8.clicked.connect(self.action_8)
        button9.clicked.connect(self.action_9)
        buttondivd.clicked.connect(self.action_divd)

        button4.clicked.connect(self.action_4)
        button5.clicked.connect(self.action_5)
        button6.clicked.connect(self.action_6)
        buttonmult.clicked.connect(self.action_mult)

        button1.clicked.connect(self.action_1)
        button2.clicked.connect(self.action_2)
        button3.clicked.connect(self.action_3)
        buttonplus.clicked.connect(self.action_plus)

        button0.clicked.connect(self.action_0)
        buttondot.clicked.connect(self.action_dot)
        buttonminus.clicked.connect(self.action_minus)
        buttonequal.clicked.connect(self.action_equal)

        buttonsin.clicked.connect(self.action_sin)
        buttoncos.clicked.connect(self.action_cos)
        buttontan.clicked.connect(self.action_tan)
        buttonpi.clicked.connect(self.action_pi)

        buttonasin.clicked.connect(self.action_asin)
        buttonacos.clicked.connect(self.action_acos)
        buttonatan.clicked.connect(self.action_atan)
        buttone.clicked.connect(self.action_e)

        buttonsqrt.clicked.connect(self.action_sqrt)
        buttonpow.clicked.connect(self.action_pow)
        buttondeg.clicked.connect(self.action_deg)
        buttonfact.clicked.connect(self.action_fact)

        buttonlog2.clicked.connect(self.action_log2)
        buttonlog10.clicked.connect(self.action_log10)
        buttonlog.clicked.connect(self.action_log)
        buttoncomma.clicked.connect(self.action_comma)

        button2pi.clicked.connect(self.action_2pi)
        buttonrad.clicked.connect(self.action_rad)
        buttonexp.clicked.connect(self.action_exp)
        buttongamma.clicked.connect(self.action_gamma)

    def action_equal(self):
        # get the label text
        equation = self.label_equation.text()
        leftparantheses = self.label_equation.text().count("(")
        rightparantheses = self.label.text().count(")")
        addparantheses = leftparantheses - rightparantheses
        for i in range(addparantheses):
            self.label_equation.setText(equation + ")")
            equation = self.label_equation.text()
        try:
            # getting the ans
            ans = eval(equation)
            # setting text to the label
            result_list.append(self.label.text())
            self.label.setText(str(ans))
            result_list.reverse()
        except:
            # setting text to the label
            self.label.setText("Wrong Input")

    def action_plus(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "+")
        self.label.setText(text + " + ")

    def action_minus(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "-")
        self.label.setText(text + " - ")

    def action_divd(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "/")
        self.label.setText(text + " / ")

    def action_mult(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "*")
        self.label.setText(text + " * ")

    def action_dot(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + ".")
        self.label.setText(text + ".")

    def action_0(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "0")
        self.label.setText(text + "0")

    def action_1(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "1")
        self.label.setText(text + "1")

    def action_2(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "2")
        self.label.setText(text + "2")

    def action_3(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "3")
        self.label.setText(text + "3")

    def action_4(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "4")
        self.label.setText(text + "4")

    def action_5(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "5")
        self.label.setText(text + "5")

    def action_6(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "6")
        self.label.setText(text + "6")

    def action_7(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "7")
        self.label.setText(text + "7")

    def action_8(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "8")
        self.label.setText(text + "8")

    def action_9(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "9")
        self.label.setText(text + "9")

    def action_leftparant(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "(")
        self.label.setText(text + "(")

    def action_rightparant(self):
        # appending label text
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + ")")
        self.label.setText(text + ")")

    def action_allclear(self):
        # clearing the label text
        self.label_equation.setText("")
        self.label.setText("")

    def action_clear(self):
        # clearing a single digit
        text = self.label.text()
        print(text[:len(text) - 1])
        self.label.setText(text[:len(text) - 1])
        self.label_equation.setText(text[:len(text) - 1])

    def action_sin(self):
        if self.radiodegree.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "sin(degrees(")
            self.label.setText(text + "sin(")
        if self.radioradian.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "sin(radians(")
            self.label.setText(text + "sin(")

    def action_cos(self):
        if self.radiodegree.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "cos(degrees(")
            self.label.setText(text + "cos(")
        if self.radioradian.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "cos(radians(")
            self.label.setText(text + "cos(")

    def action_tan(self):
        if self.radiodegree.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "tan(degrees(")
            self.label.setText(text + "tan(")
        if self.radioradian.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "tan(radians(")
            self.label.setText(text + "tan(")

    def action_pi(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "pi")
        self.label.setText(text + "π")

    def action_asin(self):
        if self.radiodegree.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "asin(degrees(")
            self.label.setText(text + "asin(")
        if self.radioradian.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "asin(radians(")
            self.label.setText(text + "asin(")

    def action_acos(self):
        if self.radiodegree.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "acos(degrees(")
            self.label.setText(text + "acos(")
        if self.radioradian.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "acos(radians(")
            self.label.setText(text + "acos(")

    def action_atan(self):
        if self.radiodegree.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "atan(degrees(")
            self.label.setText(text + "atan(")
        if self.radioradian.isChecked():
            text = self.label.text()
            equation_text = self.label_equation.text()
            self.label_equation.setText(equation_text + "atan(radians(")
            self.label.setText(text + "atan(")

    def action_e(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "e")
        self.label.setText(text + "e")

    def action_sqrt(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "sqrt(")
        self.label.setText(text + "sqrt(")

    def action_pow(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "pow(")
        self.label.setText(text + "pow(")

    def action_deg(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "degrees(")
        self.label.setText(text + "degrees(")

    def action_fact(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "factorial(")
        self.label.setText(text + "factorial(")

    def action_log2(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "log2(")
        self.label.setText(text + "log2(")

    def action_log10(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "log10(")
        self.label.setText(text + "log10(")

    def action_log(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "log(")
        self.label.setText(text + "log(")

    def action_comma(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + ",")
        self.label.setText(text + ",")

    def action_2pi(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "2*pi")
        self.label.setText(text + "2π")

    def action_rad(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "radians(")
        self.label.setText(text + "rad(")

    def action_exp(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "exp(")
        self.label.setText(text + "exp(")

    def action_gamma(self):
        text = self.label.text()
        equation_text = self.label_equation.text()
        self.label_equation.setText(equation_text + "gamma(")
        self.label.setText(text + "gamma(")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    scientific = Scientific_Calc()
    scientific.show()
    sys.exit(app.exec_())