# Form implementation generated from reading ui file 'Lab_1.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import UiParamList
from Validators import setValidator
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt
from LineEditListClass import LineEditListClass
from CheckBoxListClass import CheckBoxListClass
from myQTFunctions import getIntFromLineEdit, getFloatFromLineEdit, getValueFromLineEdit
from UiValues import UiValues
import UiParamList


class Ui_MainWindow(object):
    photoWidth = 600
    maxLengthOfList = 30
    def setupUi(self, MainWindow):
        self.paramList = UiParamList.paramList()

        self.mainWindow = MainWindow
        MainWindow.setObjectName("Lab_3 Тютюнов, Лукьяненко, Букин")
        MainWindow.resize(412, 483)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)#Главный виджет
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutMain = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayoutMain.setObjectName("verticalLayoutMain")

        self.Function_ComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.Function_ComboBox.setObjectName("Function_ComboBox")

        for i in range(7):
            self.Function_ComboBox.addItem("")
        self.verticalLayoutMain.addWidget(self.Function_ComboBox)

        self.Text_Task_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Text_Task_Label.setObjectName("Text_Task_Label")
        self.verticalLayoutMain.addWidget(self.Text_Task_Label)

        self.Photo_Task_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Photo_Task_Label.setObjectName("Photo_Task_Label")
        self.verticalLayoutMain.addWidget(self.Photo_Task_Label)

        self.NumberInput_FormLayout = QtWidgets.QFormLayout()
        self.NumberInput_FormLayout.setContentsMargins(10, 10, 10, 10)
        self.NumberInput_FormLayout.setSpacing(7)
        self.NumberInput_FormLayout.setObjectName("NumberInput_FormLayout")

        self.inputLabellist = []
        self.inputLineEditList = []
        self.numInputLine = 5
        for i in range(self.numInputLine):
            label = QtWidgets.QLabel(parent=self.centralwidget)
            label.setObjectName("Input_Label"+str(i))

            LineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
            LineEdit.setObjectName("Input_LineEdit"+str(i))

            self.NumberInput_FormLayout.setWidget(i, QtWidgets.QFormLayout.ItemRole.LabelRole, label)
            self.NumberInput_FormLayout.setWidget(i, QtWidgets.QFormLayout.ItemRole.FieldRole, LineEdit)

            self.inputLabellist.append(label)
            self.inputLineEditList.append(LineEdit)
        """
        self.Input_Label1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Input_Label1.setObjectName("Input_Label1")
        self.Input_Label2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Input_Label2.setObjectName("Input_Label2")
        self.Input_Label3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Input_Label3.setObjectName("Input_Label3")
        self.Input_LineEdit1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Input_LineEdit1.setObjectName("Input_LineEdit1")
        self.Input_LineEdit2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Input_LineEdit2.setObjectName("Input_LineEdit2")
        self.Input_LineEdit3 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.Input_LineEdit3.setObjectName("Input_LineEdit3")

        self.NumberInput_FormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Input_Label1)
        self.NumberInput_FormLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Input_LineEdit1)
        self.NumberInput_FormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Input_Label2)
        self.NumberInput_FormLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Input_LineEdit2)
        self.NumberInput_FormLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.Input_Label3)
        self.NumberInput_FormLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.Input_LineEdit3)
"""
        self.verticalLayoutMain.addLayout(self.NumberInput_FormLayout)

        self.Scroll_BoxLayout = QtWidgets.QVBoxLayout()
        self.Scroll_BoxLayout.setContentsMargins(10, 10, 10, 10)
        self.Scroll_BoxLayout.setObjectName("Scroll_BoxLayout")

        self.numScrollObjectList = 2
        self.scrollLineEditList = []
        self.scrollLabelList = []
        for i in range(self.numScrollObjectList):
            Scroll_Label = QtWidgets.QLabel(parent=self.centralwidget)
            Scroll_Label.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
            Scroll_Label.setObjectName("Scroll_Label"+str(i))
            self.Scroll_BoxLayout.addWidget(Scroll_Label)

            lineEditListClass = LineEditListClass(self.centralwidget)
            self.Scroll_BoxLayout.addWidget(lineEditListClass.scrollArea)

            self.scrollLineEditList.append(lineEditListClass)
            self.scrollLabelList.append(Scroll_Label)

        self.Scroll_Label3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.Scroll_Label3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.Scroll_Label3.setObjectName("Scroll_Label3")
        self.Scroll_BoxLayout.addWidget(self.Scroll_Label3)

        self.checkBoxListClass = CheckBoxListClass(self.centralwidget)
        self.Scroll_BoxLayout.addWidget(self.checkBoxListClass.scrollArea)

        self.verticalLayoutMain.addLayout(self.Scroll_BoxLayout)

        self.Result_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Result_Label.setObjectName("Result_Label")
        self.verticalLayoutMain.addWidget(self.Result_Label)

        self.Formula_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Formula_Label.setObjectName("Formula_Label")
        self.verticalLayoutMain.addWidget(self.Formula_Label)

        self.Photo_Result_Label = QtWidgets.QLabel(parent=self.centralwidget)
        self.Photo_Result_Label.setObjectName("Photo_Result_Label")
        self.verticalLayoutMain.addWidget(self.Photo_Result_Label)

        self.Calculate_Button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Calculate_Button.setObjectName("Calculate_Button")
        self.verticalLayoutMain.addWidget(self.Calculate_Button)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 412, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.setTabOder(MainWindow)

        self.setListeners()
        self.changeMod(self.Function_ComboBox.currentIndex(), self.Function_ComboBox.currentText())
    def setListeners(self):
        self.Function_ComboBox.currentIndexChanged.connect(lambda: self.changeMod(self.Function_ComboBox.currentIndex(), self.Function_ComboBox.currentText()))

        for i in range(self.numInputLine):
            self.inputLineEditList[i].textChanged.connect(
                lambda text, index = i: self.lineEditListener(
                    self.Function_ComboBox.currentIndex(),
                    index,
                    getValueFromLineEdit(self.inputLineEditList[index], self.paramList[self.Function_ComboBox.currentIndex()].lines[index].validatorType)
                )
            )

        self.Calculate_Button.clicked.connect(lambda: self.calculateResult(self.Function_ComboBox.currentIndex()))


    def changeMod(self, index, text):
        #проверка на диапазон
        if index < 0 or index >= len(self.paramList):
            print("Выход за пределы массивы параметров!")
            return
        param = self.paramList[index] #параметры для текущей формулы

        self.changeTextParam(self.Text_Task_Label, param.textTask)

        for i in range(self.numInputLine):
            self.changeInputLineParam(self.inputLabellist[i], self.inputLineEditList[i], param.lines[i])

        for i in range(self.numScrollObjectList):
            self.changeInputListParam(self.scrollLabelList[i], self.scrollLineEditList[i], param.lists[i])

        self.changeInputListParam(self.Scroll_Label3, self.checkBoxListClass, param.checkBoxList)

        self.changePhotoParam(self.Photo_Task_Label, param.pictureTask)
        self.changePhotoParam(self.Photo_Result_Label, param.pictureResult)
        pixmap = QPixmap(param.pictureResult.getPictureName()).scaledToWidth(self.photoWidth)
        self.Photo_Result_Label.setPixmap(pixmap)
    def changeInputLineParam(self, inputLable, inputLineEdit, lineParam):
        inputLable.setVisible(lineParam.visibility)
        inputLineEdit.setVisible(lineParam.visibility)
        if lineParam.visibility:
            setValidator(inputLineEdit, lineParam.validatorType)
            inputLable.setText(lineParam.lableText)
    def changeInputListParam(self, scrollLabel, listWidgetClass, listParam):
        listWidgetClass.setParam(listParam)
        scrollLabel.setVisible(listParam.visibility)
        if listParam.visibility:
            scrollLabel.setText(listParam.lableText)
    def changePhotoParam(self, photo, photoParam):
        if (photoParam.width < 1):
            photoWidth = self.mainWindow.width()
        else:
            photoWidth = photoParam.width
        print("photo width:", photoWidth)
        photo.setVisible(photoParam.visibility())
        if photoParam.visibility():
            pixmap = QPixmap(photoParam.getPictureName()).scaledToWidth(photoWidth)
            photo.setPixmap(pixmap)
    def changeTextParam(self, lable, textParam):
        lable.setVisible(textParam.visibility)
        if (textParam.visibility):
            lable.setText(textParam.text)
    def calculateResult(self, numOfOperation):
        # проверка на диапазон
        if numOfOperation < 0 or numOfOperation >= len(self.paramList):
            print("Выход за пределы массивы параметров!")
            return
        param = self.paramList[numOfOperation]  # параметры для текущей формулы
        try:
            values = UiValues()
            for i in range(self.numInputLine):
                if param.lines[i].needValue:
                    values.nums[i] = getValueFromLineEdit(self.inputLineEditList[i], param.lines[i].validatorType)

            for i in range(self.numScrollObjectList):

                if param.lists[i].needValues:
                    values.lists[i] = self.scrollLineEditList[i].getList()

            if param.checkBoxList.needValues:
                values.lists[2] = self.checkBoxListClass.getList()
            print (values.nums)
            res = param.function(values)
            print(str(res))
            if type(res) is not str and res < 0:
                text = "Некорректный ввод!"
            else:
                text = "Результат: "+str(res)
        except:
            text = "Невозможно посчитать значение"
        self.Result_Label.setText(text)
    def lineEditListener(self, currentFunctionIndex, numLineEdit, number):
        # проверка на диапазон
        if currentFunctionIndex < 0 or currentFunctionIndex >= len(self.paramList):
            print("Выход за пределы массива параметров!")
            return
        param = self.paramList[currentFunctionIndex]  # параметры для текущей формулы

        for i in range(self.numScrollObjectList):
            self.setNumForList(self.scrollLineEditList[i], param.lists[i], numLineEdit, number)

        self.setNumForList(self.checkBoxListClass, param.checkBoxList, numLineEdit, number)

    def setNumForList (self, listWidgetParam, listParam, numLineEdit, number):
        if (listParam.visibility and not listParam.constNumElements and listParam.numOfLineEditListenerList == numLineEdit):
            listWidgetParam.setNumOfListElements(number)
    def setTabOder(self, MainWindow):
        tabOrderList = [self.Function_ComboBox]
        tabOrderList += [lineEdit for lineEdit in self.inputLineEditList]
        tabOrderList += [listClass.scrollArea for listClass in self.scrollLineEditList]
        tabOrderList.append(self.Calculate_Button)
        for i in range(len(tabOrderList) - 1):
            MainWindow.setTabOrder(tabOrderList[i], tabOrderList[i + 1])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab_3 Тютюнов, Лукьяненко, Букин"))

        self.Function_ComboBox.setItemText(0, _translate("MainWindow", "Формула Бернулли k = m"))
        self.Function_ComboBox.setItemText(1, _translate("MainWindow", "Формула Бернулли k < m"))
        self.Function_ComboBox.setItemText(2, _translate("MainWindow", "Формула Бернулли k >= m"))
        self.Function_ComboBox.setItemText(3, _translate("MainWindow", "Формула Бернулли m1 <= k <= m2"))
        self.Function_ComboBox.setItemText(4, _translate("MainWindow", "Формула Пуассона"))
        self.Function_ComboBox.setItemText(5, _translate("MainWindow", "Локальная теорема Муавра-Лапласа"))
        self.Function_ComboBox.setItemText(6, _translate("MainWindow", "Интегральная теорема Муавра-Лапласа"))

        for i in range(self.numInputLine):
            self.inputLabellist[i].setText(_translate("MainWindow", "Input_Label"+str(i)))

        for i in range(self.numScrollObjectList):
            self.scrollLabelList[i].setText(_translate("MainWindow", "Scroll_Label1"))

        self.Result_Label.setText(_translate("MainWindow", "Результат:"))
        self.Formula_Label.setText(_translate("MainWindow", "Формула:"))
        self.Calculate_Button.setText(_translate("MainWindow", "Рассчитать"))