from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import re

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(359, 650)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.outputLabel = QLabel(self.centralwidget)
        self.outputLabel.setObjectName(u"outputLabel")
        self.outputLabel.setGeometry(QRect(10, 10, 341, 101))
        font = QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QFrame.Box)
        self.outputLabel.setFrameShadow(QFrame.Raised)
        self.outputLabel.setLineWidth(2)
        self.outputLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.percentButton = QPushButton(self.centralwidget, clicked= lambda: self.percentage_calculation())
        self.percentButton.setObjectName(u"percentButton")
        self.percentButton.setGeometry(QRect(10, 120, 75, 75))
        font1 = QFont()
        font1.setPointSize(26)
        self.percentButton.setFont(font1)
        self.percentButton.setFlat(False)
        self.clearButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("C"))
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(100, 120, 75, 75))
        self.clearButton.setFont(font1)
        self.clearButton.setFlat(False)
        self.divideButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("/"))
        self.divideButton.setObjectName(u"divideButton")
        self.divideButton.setGeometry(QRect(280, 120, 75, 75))
        self.divideButton.setFont(font1)
        self.divideButton.setFlat(False)
        self.arrowButton = QPushButton(self.centralwidget, clicked= lambda: self.back_space())
        self.arrowButton.setObjectName(u"arrowButton")
        self.arrowButton.setGeometry(QRect(190, 120, 75, 75))
        self.arrowButton.setFont(font1)
        self.arrowButton.setFlat(False)
        self.multiplyButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("*"))
        self.multiplyButton.setObjectName(u"multiplyButton")
        self.multiplyButton.setGeometry(QRect(280, 200, 75, 75))
        self.multiplyButton.setFont(font1)
        self.multiplyButton.setFlat(False)
        self.sevenButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("7"))
        self.sevenButton.setObjectName(u"sevenButton")
        self.sevenButton.setGeometry(QRect(10, 200, 75, 75))
        self.sevenButton.setFont(font1)
        self.sevenButton.setFlat(False)
        self.nineButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("9"))
        self.nineButton.setObjectName(u"nineButton")
        self.nineButton.setGeometry(QRect(190, 200, 75, 75))
        self.nineButton.setFont(font1)
        self.nineButton.setFlat(False)
        self.eightButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("8"))
        self.eightButton.setObjectName(u"eightButton")
        self.eightButton.setGeometry(QRect(100, 200, 75, 75))
        self.eightButton.setFont(font1)
        self.eightButton.setFlat(False)
        self.minusButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("-"))
        self.minusButton.setObjectName(u"minusButton")
        self.minusButton.setGeometry(QRect(280, 280, 75, 75))
        self.minusButton.setFont(font1)
        self.minusButton.setFlat(False)
        self.fourButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("4"))
        self.fourButton.setObjectName(u"fourButton")
        self.fourButton.setGeometry(QRect(10, 280, 75, 75))
        self.fourButton.setFont(font1)
        self.fourButton.setFlat(False)
        self.sixButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("6"))
        self.sixButton.setObjectName(u"sixButton")
        self.sixButton.setGeometry(QRect(190, 280, 75, 75))
        self.sixButton.setFont(font1)
        self.sixButton.setFlat(False)
        self.fiveButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("5"))
        self.fiveButton.setObjectName(u"fiveButton")
        self.fiveButton.setGeometry(QRect(100, 280, 75, 75))
        self.fiveButton.setFont(font1)
        self.fiveButton.setFlat(False)
        self.addButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("+"))
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(280, 360, 75, 75))
        self.addButton.setFont(font1)
        self.addButton.setFlat(False)
        self.oneButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("1"))
        self.oneButton.setObjectName(u"oneButton")
        self.oneButton.setGeometry(QRect(10, 360, 75, 75))
        self.oneButton.setFont(font1)
        self.oneButton.setFlat(False)
        self.threeButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("3"))
        self.threeButton.setObjectName(u"threeButton")
        self.threeButton.setGeometry(QRect(190, 360, 75, 75))
        self.threeButton.setFont(font1)
        self.threeButton.setFlat(False)
        self.twoButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("2"))
        self.twoButton.setObjectName(u"twoButton")
        self.twoButton.setGeometry(QRect(100, 360, 75, 75))
        self.twoButton.setFont(font1)
        self.twoButton.setFlat(False)
        self.equalsButton = QPushButton(self.centralwidget, clicked= lambda: self.perform_calculation())
        self.equalsButton.setObjectName(u"equalsButton")
        self.equalsButton.setGeometry(QRect(10, 520, 341, 75))
        font2 = QFont()
        font2.setPointSize(48)
        self.equalsButton.setFont(font2)
        self.equalsButton.setFlat(False)
        '''
        self.plus_minusButton = QPushButton(self.centralwidget, clicked= lambda: self.plus_minus())
        self.plus_minusButton.setObjectName(u"plus_minusButton")
        self.plus_minusButton.setGeometry(QRect(10, 440, 75, 75))
        self.plus_minusButton.setFont(font1)
        self.plus_minusButton.setFlat(False)
        '''
        self.decimalButton = QPushButton(self.centralwidget, clicked= lambda: self.decimal_point())
        self.decimalButton.setObjectName(u"decimalButton")
        self.decimalButton.setGeometry(QRect(280, 440, 75, 75))
        self.decimalButton.setFont(font1)
        self.decimalButton.setFlat(False)
        self.zeroButton = QPushButton(self.centralwidget, clicked= lambda: self.on_click("0"))
        self.zeroButton.setObjectName(u"zeroButton")
        self.zeroButton.setGeometry(QRect(190, 440, 75, 75))
        self.zeroButton.setFont(font1)
        self.zeroButton.setFlat(False)
        self.left_Paren = QPushButton(self.centralwidget, clicked= lambda: self.on_click("("))
        self.left_Paren.setObjectName(u"left_Paren")
        self.left_Paren.setGeometry(QRect(10, 440, 75, 75))
        self.left_Paren.setFont(font1)
        self.left_Paren.setFlat(False)
        self.right_Paren = QPushButton(self.centralwidget, clicked= lambda: self.on_click(")"))
        self.right_Paren.setObjectName(u"right_Paren")
        self.right_Paren.setGeometry(QRect(100, 440, 75, 75))
        self.right_Paren.setFont(font1)
        self.right_Paren.setFlat(False)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 362, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def percentage_calculation(self):
        # grab what is on the screen
        screen = self.outputLabel.text()
        answer = eval(self.outputLabel.text())
        if answer == '0':
            self.outputLabel.setText(screen)
        else:
            answer = answer / 100
            self.outputLabel.setText(str(answer))

    def perform_calculation(self):
        self.outputLabel.text()
        try:
            answer = eval(self.outputLabel.text())
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("ERROR")

    '''
    def plus_minus(self):
        # Grab what's on the screen already
        screen = self.outputLabel.text()
        #value = float(screen)
        if "-" in screen:
            self.outputLabel.setText(screen.replace("-", ""))
        elif "-" not in screen:
            self.outputLabel.setText(f'-{screen}')
       '''

    def back_space(self):
        # grab what is on the screen
        screen = self.outputLabel.text()
        # remove last item in list using slice to cut off the last item
        screen = screen[:-1]
        # output back to the screen
        self.outputLabel.setText(screen)

    # set the decimal point
    def decimal_point(self):
        screen = self.outputLabel.text()  # variable to hold
        num_list = re.split("\+|\*|-|/|%", screen)

        if ("+" in screen or "-" in screen or "*" in screen or "/" in screen or "%" in screen) and "." not in \
                num_list[-1]:
            screen = f"{screen}."
            self.outputLabel.setText(screen)

        elif '.' in screen:
            pass

        else:
            screen = f'{screen}.'
            self.outputLabel.setText(screen)

    # set the text of the output label
    def on_click(self, click):
        # if clear button is clicked
        if click == "C":
            self.outputLabel.setText("0")  # change output text to 0
        else:
            # if the text of the output label starts with a 0
            if self.outputLabel.text() == "0":
                self.outputLabel.setText("")  # replace text with a blank
            # concatenate the output text with every new value that was previously present
            self.outputLabel.setText(f'{self.outputLabel.text()}{click}')

    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculator", None))
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.percentButton.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.divideButton.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.arrowButton.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.multiplyButton.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.sevenButton.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.nineButton.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.eightButton.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.minusButton.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.fourButton.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.sixButton.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.fiveButton.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.addButton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.oneButton.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.threeButton.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.twoButton.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.equalsButton.setText(QCoreApplication.translate("MainWindow", u"=", None))
        #self.plus_minusButton.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.decimalButton.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.zeroButton.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.right_Paren.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.left_Paren.setText(QCoreApplication.translate("MainWindow", u"(", None))
