# -*- coding: utf-8 -*-

from PyQt5 import QtWidgets
 
# Импортируем наш шаблон.
from  QLabel import Ui_MainWindow5
from main_window import Ui_MainWindow
import sys
from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setGeometry(
            QtCore.QRect(5, 5, 20, 200)
        )
        self.ui.label.adjustSize()
        self.ui.label.adjustSize()
        self.setWindowTitle('PyQt5')
        self.ui.pushButton.clicked.connect(self.openDialog) # Открыть новую форму
        
    def openDialog(self):
        self.dialog = QLabel()        
        self.dialog.show()
        
        


        
class QLabel(QtWidgets.QMainWindow):
    def __init__(self):
        super(QLabel, self).__init__()
        self.ui = Ui_MainWindow5()
        self.ui.setupUi(self)
        self.setWindowTitle('QLabel')
       


        




 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mywindow()
    w.show()

    sys.exit(app.exec_())   
