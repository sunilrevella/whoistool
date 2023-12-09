from PyQt6 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup
import sys
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 738)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 1021, 711))
        self.frame.setStyleSheet("background-color: rgb(185, 218, 236);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(310, 40, 471, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(36)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(11, 9, 28);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(11, 9, 28);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(220, 170, 311, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.lineEdit.setText("")
        self.lineEdit.setCursorPosition(0)
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setGeometry(QtCore.QRect(120, 260, 791, 401))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(13)
        font.setBold(True)
        font.setItalic(False)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 900 13pt \"Arial Black\";\n"
"color: rgb(31, 66, 212);\n"
"\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(550, 180, 100, 32))
        self.pushButton.setStyleSheet("border-radius:10px;\n"
"color: rgb(0, 0, 0);\n"
"background-color: rgb(117, 251, 122);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 180, 100, 32))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(233, 52, 94);\n"
"border-radius:10px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(780, 180, 100, 32))
        self.pushButton_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"background-color: rgb(82, 35, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(230, 220, 291, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 255, 255, 0));\n"
"color: rgb(229, 51, 92);")
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Infomation Displayer"))
        self.label_2.setText(_translate("MainWindow", "Enter the Website link :"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "                  Eg : www.sample.com"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial Black\'; font-size:24pt; font-weight:900; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Get Details"))
        self.pushButton_2.setText(_translate("MainWindow", "Clear"))
        self.pushButton_3.setText(_translate("MainWindow", "Exit"))
    def getdit(self):
        url="https://www.whois.com/whois/"
        aa=self.lineEdit.text()
        if(len(aa)==0):
            self.label_3.setText("Enter the Domain name");
        else:
            self.label_3.setText("");
            url=url+aa
            req=requests.get(url)
            soup=BeautifulSoup(req.content,"html.parser")
            dd=soup.find_all('div',class_='df-label')
            d=[]
            for i in range(len(dd)):
                d.append(str(dd[i]))
            for i in range(len(dd)):
                 d[i]=d[i].replace('''<div class="df-label">''','')
                 d[i]=d[i].replace(''':</div>''','')
            dd1=soup.find_all('div',class_='df-value')
            d1=[]
            for i in range(len(dd1)):
                d1.append(str(dd1[i]))
            for i in range(len(dd1)):
               d1[i]=d1[i].replace('''<div class="df-value">''','')
               d1[i]=d1[i].replace('''</div>''','')
               d1[i]=d1[i].replace('''<br>''','   ')
               d1[i]=d1[i].replace('''<br/>''','')
            for i in range(len(d)):
                self.textEdit.append(d[i]+" :  "+d1[i])
    def clean(self):
        self.lineEdit.setText("")
        self.textEdit.setText("")
        self.label_3.setText("")
    def exitt(self):
        sys.exit()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.pushButton.clicked.connect(ui.getdit)
    ui.pushButton_2.clicked.connect(ui.clean)
    ui.pushButton_3.clicked.connect(ui.exitt)
    MainWindow.show()
    sys.exit(app.exec())
