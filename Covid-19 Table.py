# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'koronatablosu.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from selenium import webdriver
import time


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Covid-19 Table")
        MainWindow.resize(656, 421)
        MainWindow.setMinimumSize(656, 421)
        MainWindow.setMaximumSize(656, 421)
        MainWindow.setStyleSheet("""
        background:#ff003c;
        """)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(320, 40, 312, 183))
        self.calendarWidget.setMinimumDate(QtCore.QDate(2020, 3, 11))
        self.calendarWidget.setMaximumDate(QtCore.QDate(2021, 12, 31))
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.calendarWidget.setStyleSheet("""
        background:dark;
        """)
        self.calendarWidget.setObjectName("calendarWidget")
        self.search_button = QtWidgets.QPushButton(self.centralwidget)
        self.search_button.setGeometry(QtCore.QRect(410, 280, 121, 61))
        self.search_button.setObjectName("search_button")
        self.search_button.setStyleSheet("""
        color:#ff003c;
        background:white;
        """)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 40, 121, 21))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet("""
                color:white;
                """)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 121, 21))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("""
                color:white;
                """)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 121, 21))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("""
                color:white;
                """)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 130, 121, 21))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("""
                color:white;
                """)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 160, 161, 21))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_5.setStyleSheet("""
                color:white;
                """)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(5, 190, 161, 21))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("""
                color:white;
                """)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 220, 161, 21))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("""
                color:white;
                """)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 250, 131, 21))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_8.setStyleSheet("""
                color:white;
                """)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 280, 121, 21))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("""
                color:white;
                """)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 310, 121, 21))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_10.setStyleSheet("""
        color:white;
        """)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(20, 340, 121, 21))
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("""
                color:white;
                """)
        self.textEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(160, 40, 121, 26))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setStyleSheet("""
                        background:white;
                        """)
        self.textEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(160, 70, 121, 26))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setStyleSheet("""
                                background:white;
                                """)
        self.textEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(160, 100, 121, 26))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_3.setStyleSheet("""
                                        background:white;
                                        """)
        self.textEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(160, 130, 121, 26))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_4.setStyleSheet("""
                                        background:white;
                                        """)
        self.textEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_5.setGeometry(QtCore.QRect(160, 160, 121, 26))
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_5.setStyleSheet("""
                                        background:white;
                                        """)
        self.textEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_6.setGeometry(QtCore.QRect(160, 190, 121, 26))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_6.setStyleSheet("""
                                        background:white;
                                        """)
        self.textEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_7.setGeometry(QtCore.QRect(160, 220, 121, 26))
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_7.setStyleSheet("""
                                        background:white;
                                        """)
        self.textEdit_8 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_8.setGeometry(QtCore.QRect(160, 250, 121, 26))
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_8.setStyleSheet("""
                                        background:white;
                                        """)
        self.textEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_9.setGeometry(QtCore.QRect(160, 280, 121, 26))
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_9.setStyleSheet("""
                                        background:white;
                                        """)
        self.textEdit_10 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_10.setGeometry(QtCore.QRect(160, 310, 121, 26))
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_10.setStyleSheet("""
                                        background:white;
                                        """)
        self.textEdit_11 = QtWidgets.QLineEdit(self.centralwidget)
        self.textEdit_11.setGeometry(QtCore.QRect(160, 340, 121, 26))
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_11.setStyleSheet("""
                                        background:white;
                                        """)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covid-19"))
        self.search_button.setText(_translate("MainWindow", "Search"))
        self.label.setText(_translate("MainWindow", "Date"))
        self.label_2.setText(_translate("MainWindow", "Total Number of Tests"))
        self.label_3.setText(_translate("MainWindow", "Total Number of Cases"))
        self.label_4.setText(_translate("MainWindow", "Total Number of Deaths"))
        self.label_5.setText(_translate("MainWindow", "Pneumonia Rate in Patients (%)"))
        self.label_6.setText(_translate("MainWindow", "Number of Critical Patients"))
        self.label_7.setText(_translate("MainWindow", "Total Number of Healed Patients"))
        self.label_8.setText(_translate("MainWindow", "Number of Patients Today"))
        self.label_9.setText(_translate("MainWindow", "Number of Tests Today"))
        self.label_10.setText(_translate("MainWindow", "Number of Deaths Today"))
        self.label_11.setText(_translate("MainWindow", "Number of Healed Today"))
        self.search_button.clicked.connect(self.data_extraction)

    def data_extraction(self):
        tarih=self.calendarWidget.selectedDate().getDate()
        year=str(tarih[0])
        month=tarih[1]
        day=str(tarih[2])
        if month==1:
            month="OCAK"
        if month==2:
            month="ŞUBAT"
        if month==3:
            month="MART"
        if month==4:
            month="NİSAN"
        if month==5:
            month="MAYIS"
        if month==6:
            month="HAZİRAN"
        if month==7:
            month="TEMMUZ"
        if month==8:
            month="AĞUSTOS"
        if month==9:
            month="EYLÜL"
        if month==10:
            month="EKİM"
        if month==11:
            month="KASIM"
        if month==12:
            month="ARALIK"
        month=str(month)
        date=str(day+" "+month+" "+year)
        url = "https://covid19.saglik.gov.tr/TR-66935/genel-koronavirus-tablosu.html"
        browser = webdriver.Firefox(executable_path="C:/Users/batuh/Desktop/geckodriver.exe")
        browser.get(url)
        time.sleep(1)
        elements = browser.find_elements_by_tag_name("td")
        k = 0
        i = 0
        liste = []
        for element in elements:
            if element.text == date:
                i = 1
            if i == 1:
                k += 1
                liste.append(element.text)
            if k == 11:
                break
        self.textEdit.setText(liste[0])
        if len(self.textEdit.text())== 0:
            self.textEdit.setText("0")
        self.textEdit_2.setText(liste[1])
        if len(self.textEdit_2.text())== 0:
            self.textEdit_2.setText("0")
        self.textEdit_3.setText(liste[2])
        if len(self.textEdit_3.text())== 0:
            self.textEdit_3.setText("0")
        self.textEdit_4.setText(liste[3])
        if len(self.textEdit_4.text())== 0:
            self.textEdit_4.setText("0")
        self.textEdit_5.setText(liste[4])
        if len(self.textEdit_5.text())== 0:
            self.textEdit_5.setText("0")
        self.textEdit_6.setText(liste[5])
        if len(self.textEdit_6.text())== 0:
            self.textEdit_6.setText("0")
        self.textEdit_7.setText(liste[6])
        if len(self.textEdit_7.text())== 0:
            self.textEdit_7.setText("0")
        self.textEdit_8.setText(liste[7])
        if len(self.textEdit_8.text())== 0:
            self.textEdit_8.setText("0")
        self.textEdit_9.setText(liste[8])
        if len(self.textEdit_9.text())== 0:
            self.textEdit_9.setText("0")
        self.textEdit_10.setText(liste[9])
        if len(self.textEdit_10.text())== 0:
            self.textEdit_10.setText("0")
        self.textEdit_11.setText(liste[10])
        if len(self.textEdit_11.text())== 0:
            self.textEdit_11.setText("0")
        browser.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
