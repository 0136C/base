import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(773, 680)
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setStyleSheet("QWidget {\n"
"    color: white;\n"
"    background-color: #7CC398;\n"
"    font-family: Oswald;\n"
"    font-size: 20pt;\n"
"    font-weight: 600;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #62A77C;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #153626;\n"
"}")
        
        
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(400, 560, 241, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 60, 91, 51))
        
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText(str(random.randint(90, 110)))            # (90, 99)
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 70, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 60, 91, 51))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText(str(random.randint(90, 110)))
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(240, 70, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(260, 60, 91, 51))
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(70, 10, 91, 51))
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        
        self.lineEdit_5 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(10, 190, 91, 51))
        self.lineEdit_5.setText("")
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText(str(random.randint(90, 110)))
        
        self.lineEdit_6 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(140, 190, 91, 51))
        self.lineEdit_6.setText("")
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText(str(random.randint(90, 110)))
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 200, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 200, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.lineEdit_7 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_7.setGeometry(QtCore.QRect(260, 190, 91, 51))
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        
        self.lineEdit_8 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 140, 91, 51))
        self.lineEdit_8.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_8.setObjectName("lineEdit_8")
        
        self.lineEdit_9 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_9.setGeometry(QtCore.QRect(10, 320, 91, 51))
        self.lineEdit_9.setText("")
        self.lineEdit_9.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_9.setText(str(random.randint(90, 110)))

        self.lineEdit_10 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_10.setGeometry(QtCore.QRect(140, 320, 91, 51))
        self.lineEdit_10.setText("")
        self.lineEdit_10.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_10.setText(str(random.randint(90, 110)))

        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(110, 330, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(240, 330, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.lineEdit_11 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_11.setGeometry(QtCore.QRect(260, 320, 91, 51))
        self.lineEdit_11.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_11.setObjectName("lineEdit_11")
        
        self.lineEdit_12 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_12.setGeometry(QtCore.QRect(70, 270, 91, 51))
        self.lineEdit_12.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_12.setObjectName("lineEdit_12")
        
        self.lineEdit_13 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_13.setGeometry(QtCore.QRect(10, 450, 91, 51))
        self.lineEdit_13.setText("")
        self.lineEdit_13.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.lineEdit_13.setText(str(random.randint(90, 110)))

        self.lineEdit_14 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_14.setGeometry(QtCore.QRect(140, 450, 91, 51))
        self.lineEdit_14.setText("")
        self.lineEdit_14.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.lineEdit_14.setText(str(random.randint(90, 110)))

        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(110, 460, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(240, 460, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
        self.lineEdit_15 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_15.setGeometry(QtCore.QRect(260, 450, 91, 51))
        self.lineEdit_15.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_15.setObjectName("lineEdit_15")
        
        self.lineEdit_16 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_16.setGeometry(QtCore.QRect(70, 400, 91, 51))
        self.lineEdit_16.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_16.setObjectName("lineEdit_16")
        
        self.lineEdit_17 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_17.setGeometry(QtCore.QRect(410, 450, 91, 51))
        self.lineEdit_17.setText("")
        self.lineEdit_17.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_17.setText(str(random.randint(90, 110)))

        self.lineEdit_18 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_18.setGeometry(QtCore.QRect(540, 450, 91, 51))
        self.lineEdit_18.setText("")
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_18.setText(str(random.randint(90, 110)))
        
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(510, 460, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(640, 460, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        
        self.lineEdit_19 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_19.setGeometry(QtCore.QRect(660, 450, 91, 51))
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setObjectName("lineEdit_19")
        
        self.lineEdit_20 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_20.setGeometry(QtCore.QRect(470, 400, 91, 51))
        self.lineEdit_20.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_20.setObjectName("lineEdit_20")
        
        self.lineEdit_21 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_21.setGeometry(QtCore.QRect(410, 320, 91, 51))
        self.lineEdit_21.setText("")
        self.lineEdit_21.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_21.setText(str(random.randint(90, 110)))
        
        self.lineEdit_22 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_22.setGeometry(QtCore.QRect(540, 320, 91, 51))
        self.lineEdit_22.setText("")
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setReadOnly(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_22.setText(str(random.randint(90, 110)))

        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(510, 330, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(640, 330, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        
        self.lineEdit_23 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_23.setGeometry(QtCore.QRect(660, 320, 91, 51))
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setObjectName("lineEdit_23")
        
        self.lineEdit_24 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_24.setGeometry(QtCore.QRect(470, 270, 91, 51))
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_24.setObjectName("lineEdit_24")
        
        self.lineEdit_25 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_25.setGeometry(QtCore.QRect(400, 190, 91, 51))
        self.lineEdit_25.setText("")
        self.lineEdit_25.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_25.setText(str(random.randint(90, 110)))
        
        self.lineEdit_26 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_26.setGeometry(QtCore.QRect(530, 190, 91, 51))
        self.lineEdit_26.setText("")
        self.lineEdit_26.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_26.setText(str(random.randint(90, 110)))

        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setGeometry(QtCore.QRect(500, 200, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setGeometry(QtCore.QRect(630, 200, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        
        self.lineEdit_27 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_27.setGeometry(QtCore.QRect(650, 190, 91, 51))
        self.lineEdit_27.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_27.setObjectName("lineEdit_27")
        
        self.lineEdit_28 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_28.setGeometry(QtCore.QRect(460, 140, 91, 51))
        self.lineEdit_28.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_28.setObjectName("lineEdit_28")
        
        self.lineEdit_29 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_29.setGeometry(QtCore.QRect(400, 60, 91, 51))
        self.lineEdit_29.setText("")
        self.lineEdit_29.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.lineEdit_29.setText(str(random.randint(90, 110)))

        self.lineEdit_30 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_30.setGeometry(QtCore.QRect(530, 60, 91, 51))
        self.lineEdit_30.setText("")
        self.lineEdit_30.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_30.setReadOnly(True)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.lineEdit_30.setText(str(random.randint(90, 110)))
        
        self.label_15 = QtWidgets.QLabel(Dialog)
        self.label_15.setGeometry(QtCore.QRect(500, 70, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(Dialog)
        self.label_16.setGeometry(QtCore.QRect(630, 70, 25, 25))
        font = QtGui.QFont()
        font.setFamily("Oswald")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        
        self.lineEdit_31 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_31.setGeometry(QtCore.QRect(650, 60, 91, 51))
        self.lineEdit_31.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_31.setObjectName("lineEdit_31")
        
        self.lineEdit_32 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_32.setGeometry(QtCore.QRect(460, 10, 91, 51))
        self.lineEdit_32.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_32.setObjectName("lineEdit_32")
        self.retranslateUi(Dialog)

        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_2.setText(_translate("Dialog", "ПРОВЕРИТЬ"))
        self.label.setText(_translate("Dialog", "×"))
        self.label_2.setText(_translate("Dialog", "="))
        self.label_3.setText(_translate("Dialog", "×"))
        self.label_4.setText(_translate("Dialog", "="))
        self.label_5.setText(_translate("Dialog", "×"))
        self.label_6.setText(_translate("Dialog", "="))
        self.label_7.setText(_translate("Dialog", "×"))
        self.label_8.setText(_translate("Dialog", "="))
        self.label_9.setText(_translate("Dialog", "×"))
        self.label_10.setText(_translate("Dialog", "="))
        self.label_11.setText(_translate("Dialog", "×"))
        self.label_12.setText(_translate("Dialog", "="))
        self.label_13.setText(_translate("Dialog", "×"))
        self.label_14.setText(_translate("Dialog", "="))
        self.label_15.setText(_translate("Dialog", "×"))
        self.label_16.setText(_translate("Dialog", "="))


class Dialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self) 
        
        self.pushButton_2.clicked.connect(self.check_answers)
        
        QtCore.QTimer.singleShot(
            10000,                 # вызов функции check_answers через 30 секунд
            self.check_answers
        ) 

    def check_answers(self):
        answers = [
            self.lineEdit_3.text(), self.lineEdit_7.text(), 
            self.lineEdit_11.text(), self.lineEdit_15.text(), 
            self.lineEdit_19.text(), self.lineEdit_23.text(),
            self.lineEdit_27.text(), self.lineEdit_31.text()
        ]

        correct_answers = [                                   
            str(int(self.lineEdit.text()) * int(self.lineEdit_2.text())),
            str(int(self.lineEdit_5.text()) * int(self.lineEdit_6.text())),
            str(int(self.lineEdit_9.text()) * int(self.lineEdit_10.text())),
            str(int(self.lineEdit_13.text()) * int(self.lineEdit_14.text())),
            str(int(self.lineEdit_17.text()) * int(self.lineEdit_18.text())),
            str(int(self.lineEdit_21.text()) * int(self.lineEdit_22.text())),
            str(int(self.lineEdit_25.text()) * int(self.lineEdit_26.text())),
            str(int(self.lineEdit_29.text()) * int(self.lineEdit_30.text()))
        ]        
        print()
        for i in range(len(answers)):
            try:                                                    # +
                my_answer = str(int(answers[i]))                    # +
            except:                                                 # +
                my_answer = 'invalid literal'                       # +
            
#            if answers[i] == correct_answers[i]:
            if my_answer == correct_answers[i]:                     # +
                print(f"Пример {i+1}: верен")
            else:
                print(f"Пример {i+1}: неверен")
        

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    w = Dialog()
    w.show()
    sys.exit(app.exec_())