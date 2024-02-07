from PyQt6 import QtCore, QtGui, QtWidgets
import result


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, main):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setStyleSheet("background-color:\"#F8D347\";\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-30, 530, 831, 71))
        self.label.setStyleSheet("background-color:\"#2A3542\"")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_m = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_m.setGeometry(QtCore.QRect(80, 180, 151, 31))
        self.label_m.setStyleSheet("font: 24pt \"PT Sans\"; color:\"#2A3542\"")
        self.label_m.setObjectName("label_m")
        self.label_m_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_m_2.setGeometry(QtCore.QRect(80, 260, 151, 31))
        self.label_m_2.setStyleSheet("font: 24pt \"PT Sans\"; color:\"#2A3542\"")
        self.label_m_2.setObjectName("label_m_2")
        self.label_m_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_m_3.setGeometry(QtCore.QRect(80, 330, 91, 31))
        self.label_m_3.setStyleSheet("font: 24pt \"PT Sans\"; color:\"#2A3542\"")
        self.label_m_3.setObjectName("label_m_3")
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(200, 180, 91, 31))
        self.spinBox.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 21pt \"PT Sans\"; color:\"#2A3542\"")
        self.spinBox.setObjectName("spinBox")
        self.spinBox.setValue(main.delta1)
        self.dolgota = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.dolgota.setGeometry(QtCore.QRect(200, 260, 141, 31))
        self.dolgota.setStyleSheet("background-color: rgb(255, 255, 255); color:\"#2A3542\"")
        self.dolgota.setObjectName("dolgota")
        self.shirota = QtWidgets.QTextEdit(parent=self.centralwidget)
        self.shirota.setGeometry(QtCore.QRect(200, 330, 141, 31))
        self.shirota.setStyleSheet("background-color: rgb(255, 255, 255); color:\"#2A3542\"")
        self.shirota.setObjectName("shirota")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(380, 430, 81, 81))
        self.pushButton.setStyleSheet(f"image: url(data/start_bttn.png);\n"
"border: none")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(-140, -50, 1051, 231))
        self.logo.setStyleSheet("image: url(data/logo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.result)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Главное меню"))
        self.label_m.setText(_translate("MainWindow", "Масштаб"))
        self.label_m_2.setText(_translate("MainWindow", "Долгота"))
        self.label_m_3.setText(_translate("MainWindow", "Широта"))

    def result(self):
        res = result.Main(delta1=str(self.spinBox.value()), delta2=str(self.spinBox.value()), lattitude=self.dolgota.toPlainText(), longitude=self.shirota.toPlainText())
        res.show_result(res.get_result())
