from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QLabel,QPushButton
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
ans=0
result_list=[]
class Standard_Calc(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setMaximumSize(280, 430)
        self.setMinimumSize(280, 430)
        self.resize(280, 430)
        self.buttons_and_label()
    def buttons_and_label(self):
        self.label=QLabel(self)
        self.label_equation=QLabel(self)
        self.label_equation.setVisible(False)
        self.label.setGeometry(1,30,280,70)
        self.label.setWordWrap(True)
        self.label.setStyleSheet("QLabel"
                                 "{"
                                 "border : 4px solid orange;"
                                 "background : white;"
                                 "}")
        self.label.setAlignment(Qt.AlignRight)
        self.label.setFont(QFont("Arial",15))

        # Buttons

        buttonleftparant  = QPushButton("(", self)
        buttonleftparant.setGeometry(1, 100, 70, 65)
        buttonrightparant = QPushButton(")", self)
        buttonrightparant.setGeometry(71,100, 70, 65)
        buttonclear       = QPushButton("DEL", self)
        buttonclear.setGeometry(141,100, 70, 65)
        buttonclear.setStyleSheet("QPushButton"
                                 "{"
                                 "background : orange;"
                                 "}")
        buttonallclear    = QPushButton("AC", self)
        buttonallclear.setGeometry(211,100, 70, 65)
        buttonallclear.setStyleSheet("QPushButton"
                                 "{"
                                 "background : orange;"
                                 "}")


        button7    = QPushButton("7", self)
        button7.setGeometry(1, 160, 70, 65)
        button8    = QPushButton("8", self)
        button8.setGeometry(71, 160, 70, 65)
        button9    = QPushButton("9", self)
        button9.setGeometry(141, 160, 70, 65)
        buttondivd = QPushButton("÷", self)
        buttondivd.setGeometry(211, 160, 70, 65)
        buttondivd.setStyleSheet("QPushButton"
                                 "{"
                                 "background : #C0C0C0;"
                                 "}")


        button4    = QPushButton("4", self)
        button4.setGeometry(1, 220, 70, 65)
        button5    = QPushButton("5", self)
        button5.setGeometry(71, 220, 70, 65)
        button6    = QPushButton("6", self)
        button6.setGeometry(141, 220, 70, 65)
        buttonmult = QPushButton("X", self)
        buttonmult.setGeometry(211, 220, 70, 65)
        buttonmult.setStyleSheet("QPushButton"
                                 "{"
                                 "background : #C0C0C0;"
                                 "}")


        button1    = QPushButton("1", self)
        button1.setGeometry(1, 280, 70, 65)
        button2    = QPushButton("2", self)
        button2.setGeometry(71, 280, 70, 65)
        button3    = QPushButton("3", self)
        button3.setGeometry(141, 280, 70, 65)
        buttonplus = QPushButton("+", self)
        buttonplus.setGeometry(211, 280, 70, 65)
        buttonplus.setStyleSheet("QPushButton"
                                 "{"
                                 "background :#C0C0C0;"
                                 "}")



        button0     = QPushButton("0", self)
        button0.setGeometry(1, 340, 70, 65)
        buttondot   = QPushButton(".", self)
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

    def action_equal(self):
        # get the label text
        equation = self.label_equation.text()
        leftparantheses=self.label_equation.text().count("(")
        rightparantheses=self.label.text().count(")")
        addparantheses=leftparantheses-rightparantheses
        for i in range(addparantheses):
            self.label_equation.setText(equation + ")")
            equation = self.label_equation.text()
        try:
            # getting the ans
            ans  = eval(equation)
            # setting text to the label
            result_list.append(self.label.text())
            self.label.setText(str(ans))
            result_list.reverse()
        except:
            # setting text to the label
            self.label.setText("Wrong Input")

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
    standard = Standard_Calc()
    standard.show()
    sys.exit(app.exec_())