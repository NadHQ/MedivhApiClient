# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileForm(object):
    def setupUi(self, ProfileForm):
        ProfileForm.setObjectName("ProfileForm")
        ProfileForm.resize(1025, 538)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ProfileForm.sizePolicy().hasHeightForWidth())
        ProfileForm.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(ProfileForm)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 100, 371, 223))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.nameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameInput.setFont(font)
        self.nameInput.setObjectName("nameInput")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameInput)
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.secondNameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.secondNameInput.setFont(font)
        self.secondNameInput.setObjectName("secondNameInput")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.secondNameInput)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.thirdNameInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.thirdNameInput.setFont(font)
        self.thirdNameInput.setObjectName("thirdNameInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.thirdNameInput)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.specializationInput = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.specializationInput.setFont(font)
        self.specializationInput.setObjectName("specializationInput")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.specializationInput)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(7, QtWidgets.QFormLayout.SpanningRole, spacerItem3)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.licenseNumber = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.licenseNumber.setFont(font)
        self.licenseNumber.setObjectName("licenseNumber")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.licenseNumber)
        self.changeButton = QtWidgets.QPushButton(self.formLayoutWidget)
        self.changeButton.setObjectName("changeButton")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.SpanningRole, self.changeButton)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(440, 100, 561, 351))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(170, 40, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        ProfileForm.setCentralWidget(self.centralwidget)

        self.retranslateUi(ProfileForm)
        QtCore.QMetaObject.connectSlotsByName(ProfileForm)

    def retranslateUi(self, ProfileForm):
        _translate = QtCore.QCoreApplication.translate
        ProfileForm.setWindowTitle(_translate("ProfileForm", "MainWindow"))
        self.label.setText(_translate("ProfileForm", "Имя"))
        self.label_2.setText(_translate("ProfileForm", "Фамилия"))
        self.label_3.setText(_translate("ProfileForm", "Отчество"))
        self.label_4.setText(_translate("ProfileForm", "Специальность"))
        self.label_6.setText(_translate("ProfileForm", "Номер лицензии"))
        self.licenseNumber.setText(_translate("ProfileForm", "TextLabel"))
        self.changeButton.setText(_translate("ProfileForm", "Изменить"))
        self.tableWidget.setSortingEnabled(False)
        self.label_5.setText(_translate("ProfileForm", "Профиль"))
