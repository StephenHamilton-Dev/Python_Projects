import re
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Ui_MainWindow(object):
    # setupUi
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(441, 753)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.outputLabel = QLabel(self.centralwidget)
        self.outputLabel.setObjectName(u"outputLabel")
        self.outputLabel.setGeometry(QRect(0, 0, 441, 101))
        font = QFont()
        font.setPointSize(36)
        self.outputLabel.setFont(font)
        self.outputLabel.setFrameShape(QFrame.Box)
        self.outputLabel.setFrameShadow(QFrame.Raised)
        self.outputLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.percent_Button = QPushButton(self.centralwidget, clicked= lambda: self.percentage_button())
        self.percent_Button.setObjectName(u"percent_Button")
        self.percent_Button.setGeometry(QRect(0, 100, 112, 100))
        self.percent_Button.setFont(font)
        self.clear_Button = QPushButton(self.centralwidget, clicked= lambda: self.button_click("C"))
        self.clear_Button.setObjectName(u"clear_Button")
        self.clear_Button.setGeometry(QRect(110, 100, 112, 100))
        self.clear_Button.setFont(font)
        self.backspace_Button = QPushButton(self.centralwidget, clicked= lambda: self.backspace())
        self.backspace_Button.setObjectName(u"backspace_Button")
        self.backspace_Button.setGeometry(QRect(220, 100, 112, 100))
        self.backspace_Button.setFont(font)
        self.add_Button = QPushButton(self.centralwidget, clicked= lambda: self.button_click("+"))
        self.add_Button.setObjectName(u"add_Button")
        self.add_Button.setGeometry(QRect(330, 100, 112, 100))
        self.add_Button.setFont(font)
        self.button_Nine = QPushButton(self.centralwidget, clicked= lambda: self.button_click("9"))
        self.button_Nine.setObjectName(u"button_Nine")
        self.button_Nine.setGeometry(QRect(220, 200, 112, 100))
        self.button_Nine.setFont(font)
        self.button_Eight = QPushButton(self.centralwidget, clicked= lambda: self.button_click("8"))
        self.button_Eight.setObjectName(u"button_Eight")
        self.button_Eight.setGeometry(QRect(110, 200, 112, 100))
        self.button_Eight.setFont(font)
        self.minus_Button = QPushButton(self.centralwidget, clicked= lambda: self.button_click("-"))
        self.minus_Button.setObjectName(u"minus_Button")
        self.minus_Button.setGeometry(QRect(330, 200, 112, 100))
        font1 = QFont()
        font1.setPointSize(48)
        self.minus_Button.setFont(font1)
        self.button_Seven = QPushButton(self.centralwidget, clicked= lambda: self.button_click("7"))
        self.button_Seven.setObjectName(u"button_Seven")
        self.button_Seven.setGeometry(QRect(0, 200, 112, 100))
        self.button_Seven.setFont(font)
        self.button_Six = QPushButton(self.centralwidget, clicked= lambda: self.button_click("6"))
        self.button_Six.setObjectName(u"button_Six")
        self.button_Six.setGeometry(QRect(220, 300, 112, 100))
        self.button_Six.setFont(font)
        self.button_Five = QPushButton(self.centralwidget, clicked= lambda: self.button_click("5"))
        self.button_Five.setObjectName(u"button_Five")
        self.button_Five.setGeometry(QRect(110, 300, 112, 100))
        self.button_Five.setFont(font)
        self.mult_Button = QPushButton(self.centralwidget, clicked= lambda: self.button_click("*"))
        self.mult_Button.setObjectName(u"mult_Button")
        self.mult_Button.setGeometry(QRect(330, 300, 112, 100))
        self.mult_Button.setFont(font)
        self.button_Four = QPushButton(self.centralwidget, clicked= lambda: self.button_click("4"))
        self.button_Four.setObjectName(u"button_Four")
        self.button_Four.setGeometry(QRect(0, 300, 112, 100))
        self.button_Four.setFont(font)
        self.button_Three = QPushButton(self.centralwidget, clicked= lambda: self.button_click("3"))
        self.button_Three.setObjectName(u"button_Three")
        self.button_Three.setGeometry(QRect(220, 400, 112, 100))
        self.button_Three.setFont(font)
        self.button_Two = QPushButton(self.centralwidget, clicked= lambda: self.button_click("2"))
        self.button_Two.setObjectName(u"button_Two")
        self.button_Two.setGeometry(QRect(110, 400, 112, 100))
        self.button_Two.setFont(font)
        self.div_Button = QPushButton(self.centralwidget, clicked= lambda: self.button_click("/"))
        self.div_Button.setObjectName(u"div_Button")
        self.div_Button.setGeometry(QRect(330, 400, 112, 100))
        self.div_Button.setFont(font)
        self.button_One = QPushButton(self.centralwidget, clicked= lambda: self.button_click("1"))
        self.button_One.setObjectName(u"button_One")
        self.button_One.setGeometry(QRect(0, 400, 112, 100))
        self.button_One.setFont(font)
        self.button_Zero = QPushButton(self.centralwidget, clicked= lambda: self.button_click("0"))
        self.button_Zero.setObjectName(u"button_Zero")
        self.button_Zero.setGeometry(QRect(220, 500, 112, 100))
        self.button_Zero.setFont(font)
        self.right_Paren = QPushButton(self.centralwidget, clicked= lambda: self.button_click(")"))
        self.right_Paren.setObjectName(u"right_Paren")
        self.right_Paren.setGeometry(QRect(110, 500, 112, 100))
        self.right_Paren.setFont(font)
        self.button_Decimal = QPushButton(self.centralwidget, clicked= lambda: self.add_decimal())
        self.button_Decimal.setObjectName(u"button_Decimal")
        self.button_Decimal.setGeometry(QRect(330, 500, 112, 100))
        self.button_Decimal.setFont(font)
        self.left_Paren = QPushButton(self.centralwidget, clicked= lambda: self.button_click("("))
        self.left_Paren.setObjectName(u"left_Paren")
        self.left_Paren.setGeometry(QRect(0, 500, 112, 100))
        self.left_Paren.setFont(font)
        self.button_Equals = QPushButton(self.centralwidget, clicked= lambda: self.perform_math())
        self.button_Equals.setObjectName(u"button_Equals")
        self.button_Equals.setGeometry(QRect(0, 600, 441, 100))
        self.button_Equals.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 441, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    '''
     Method: button_click
     
     Description: 
     This method will clear the values on the screen, 
     will not let the user add multiple zeros before a 
     number, and will concatenate the output of the 
     button clicks (i.e. 987654321 or 9 + 5)
     
     Author: Stephen Hamilton
     Return: NA
     Dependencies: The clear button
    '''
    def button_click(self, click):
        # clear button is clicked
        if click == "C":
            self.outputLabel.setText("0")  # erase all text and set to 0
        else:
            if self.outputLabel.text() == "0":   # if 0, put a blank after
                self.outputLabel.setText("")
                # take what is on the screen and what gets added to the screen and concatenate
            self.outputLabel.setText(f'{self.outputLabel.text()}{click}')

    '''
         Method: perform_math
         
         Description: 
         This method will take the equation present on the screen,
         then, in a try / except block, it uses the eval function
         to perform the order of operations calculation on the
         equation. It saves the evaluation in variable answer, 
         then outputs variable answer to screen as a string.
         If the evaluation cannot happen (i.e. incorrect equation entered),
         the method will then display ERROR
         
         Author: Stephen Hamilton
         Return: NA
         Dependencies: Proper equation entered by user
    '''
    def perform_math(self):
        # grab what is in the output label
        self.outputLabel.text()
        try:
            answer = eval(self.outputLabel.text())
            self.outputLabel.setText(str(answer))
        except:
            self.outputLabel.setText("ERROR")

    '''
          Method: percentage_button

          Description: 
          This method will save what is on the screen in variable screen,
          and will also take the same input seen on the screen and perform
          an evaluation of the equation with the eval function. When
          the answer is zero, we will take what is on the screen and 
          display it. When the answer is not equal to zero we will take
          the answer variable, perform the eval on what is stored in 
          the answer variable and then divide by 100 % and output
          the result to screen.

          Author: Stephen Hamilton
          Return: NA
          Dependencies: Proper equation entered by user
    '''
    def percentage_button(self):
        screen = self.outputLabel.text()  # grab what is in the output label and save to variable "screen"

        answer = eval(self.outputLabel.text())

        if answer == "0":
            self.outputLabel.setText(screen)
        elif answer != "0":
            answer = answer / 100
            self.outputLabel.setText(str(answer))

    '''
          Method: add_decimal

          Description: 
          This method saves what is on the calculator screen in variable screen
          The method then uses a list that splits at each operator symbol
          The list is used to knock off the last character on the screen,
          if the decimal is not in the list
          The method then writes a decimal to the screen
          if the decimal is already in the screen, we do nothing

          Author: Stephen Hamilton
          Return: NA
          Dependencies: NA
    '''
    def add_decimal(self):
        screen = self.outputLabel.text()   # grab what is in output label and save in variable "screen"

        operator_list = re.split("\+|-|/|\*", screen)  # split at each operator symbol in screen

        if ("+" in screen or "-" in screen or "*" in screen or "/" in screen) and "." not in operator_list[-1]:

            screen = f'{screen}.'
            self.outputLabel.setText(screen)

        elif "." in screen:
            pass  # do nothing

        else:
            screen = f"{screen}."  # concatenates the decimal to what is on the screen
            self.outputLabel.setText(screen)  # outputs what is on the screen and sets the text

    '''
              Method: backspace

              Description: 
              This method grabs what is on the screen and saves the input to variable screen
              then, what is held in variable screen will be split at the last index
              effectively taking away the last character
              then it re-outputs back to screen

              Author: Stephen Hamilton
              Return: NA
              Dependencies: NA
    '''
    def backspace(self):
        screen = self.outputLabel.text()  # grab what is in the outputLabel and store inside of variable "screen"
        screen = screen[:-1]              # split at last index - take the last character off
        self.outputLabel.setText(screen)  # output the characters again - set the current text

    # retranslateUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.outputLabel.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.percent_Button.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.clear_Button.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.backspace_Button.setText(QCoreApplication.translate("MainWindow", u"<<", None))
        self.add_Button.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.button_Nine.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.button_Eight.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.minus_Button.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.button_Seven.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.button_Six.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.button_Five.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.mult_Button.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.button_Four.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.button_Three.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.button_Two.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.div_Button.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.button_One.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.button_Zero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.right_Paren.setText(QCoreApplication.translate("MainWindow", u")", None))
        self.button_Decimal.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.left_Paren.setText(QCoreApplication.translate("MainWindow", u"(", None))
        self.button_Equals.setText(QCoreApplication.translate("MainWindow", u"=", None))





