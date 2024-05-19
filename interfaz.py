# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loadGUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 680)
        MainWindow.setStyleSheet("background-color: rgb(45, 58, 85);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(370, 20, 131, 61))
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(290, 110, 271, 111))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(51)
        self.formLayout.setVerticalSpacing(24)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setStyleSheet("font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.line1 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line1.setObjectName("line1")
        self.verticalLayout_2.addWidget(self.line1)
        self.line2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.line2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.line2.setObjectName("line2")
        self.verticalLayout_2.addWidget(self.line2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        self.Calcular = QtWidgets.QPushButton(self.formLayoutWidget)
        self.Calcular.setEnabled(True)
        self.Calcular.setMinimumSize(QtCore.QSize(7, 3))
        self.Calcular.setStyleSheet("background-color: rgb(53, 68, 98);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.Calcular.setIconSize(QtCore.QSize(22, 16))
        self.Calcular.setAutoRepeat(False)
        self.Calcular.setAutoExclusive(False)
        self.Calcular.setAutoRepeatDelay(298)
        self.Calcular.setAutoDefault(False)
        self.Calcular.setObjectName("Calcular")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Calcular)
        self.delete_2 = QtWidgets.QPushButton(self.formLayoutWidget)
        self.delete_2.setStyleSheet("background-color: rgb(53, 68, 98);\n"
"font: 11pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.delete_2.setObjectName("delete_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.delete_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(290, 230, 271, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(20, 90, 211, 391))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_12 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_4.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_13.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_4.addWidget(self.label_13)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(590, 50, 231, 671))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Cambiar QLabel a QListWidget
        self.value1 = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.value1.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.value1.setObjectName("value1")
        self.verticalLayout_3.addWidget(self.value1)

        self.value2 = QtWidgets.QListWidget(self.verticalLayoutWidget)
        self.value2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.value2.setObjectName("value2")
        self.verticalLayout_3.addWidget(self.value2)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(590, 30, 211, 16))
        self.label_9.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 10pt \"MS Shell Dlg 2\";")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 828, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Tiro parabolico"))
        self.label_4.setText(_translate("MainWindow", "Posición en x en cm"))
        self.label_3.setText(_translate("MainWindow", "Posición y en cm"))
        self.Calcular.setText(_translate("MainWindow", "Calcular datos"))
        self.delete_2.setText(_translate("MainWindow", "Borrar datos"))
        self.label_12.setText(_translate("MainWindow", "Bienvenidos"))
        self.label_13.setText(_translate("MainWindow", "En este programa podras calcular\n"
"las distancias que necesitaras para\n"
"tu competencia naval, deberás\n"
"proporcionar los datos que se\n"
"encuentra en la parte de la mitad\n"
"de la pagina."))
        self.label_9.setText(_translate("MainWindow", "Distancia:"))