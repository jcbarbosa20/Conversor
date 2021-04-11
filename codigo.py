#EXALTE A MINHA ALMA E O MEU PROGRAMA, AO ÚNICO DEUS!!!

from PyQt5 import QtWidgets, uic

janela = QtWidgets.QApplication([])
interface = uic.loadUi("tela.ui")

def main():
    dolar = 5.78
    euro = 6.88
    bitcoin = 332030.61

    if interface.radioButton.isChecked():
        interface.lineEdit_2.setText(str(float(interface.lineEdit.text()) * float (dolar)))

    elif interface.radioButton_2.isChecked():
        interface.lineEdit_2.setText(str(float(interface.lineEdit.text()) * float (euro)))

    elif interface.radioButton_3.isChecked():
        interface.lineEdit_2.setText(str(float(interface.lineEdit.text()) * float (bitcoin)))

def clear():
    interface.lineEdit.setText("")
    interface.lineEdit_2.setText("")
    
interface.lineEdit_2.setReadOnly(True)
interface.pushButton.clicked.connect(main)
interface.pushButton_2.clicked.connect(clear)

interface.show()
janela.exec()
