#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QLineEdit, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap
import DB, graphCreate

class AddDataWindow(QMainWindow):
    def __init__(self, parent=None):
        super(AddDataWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        glayout = QGridLayout()
        self.setLayout(glayout)

        global productNameText
        global productBuyText
        global productCountText
        global sendDataButton
        global productNameLabel
        global productCountLabel
        global productBuyLabel

        productNameText = QLineEdit(self)
        productCountText = QLineEdit(self)
        productBuyText = QLineEdit(self)

        productNameLabel = QLabel('Имя продукта', self)
        productCountLabel = QLabel('Кол-во', self)
        productBuyLabel = QLabel('True or false', self)

        sendDataButton = QPushButton('Send data', self)

        glayout.addWidget(productNameText, 0, 0)
        glayout.addWidget(productCountText, 0, 1)
        glayout.addWidget(productNameText, 0, 2)
        glayout.addWidget(productNameLabel, 0, 0)
        glayout.addWidget(productCountLabel, 0, 1)
        glayout.addWidget(productNameLabel, 0, 2)
        
        productNameLabel.move(5, 0)
        productCountLabel.move(115, 0)
        productBuyLabel.move(220, 0)

        productNameText.move(5, 30)
        productCountText.move(115, 30)
        productBuyText.move(220, 30)

        sendDataButton.move(115, 80)
        sendDataButton.clicked.connect(self.sendData)

        self.setGeometry(325, 325, 325, 150)
        self.setWindowTitle('Add data')


    def sendData(self):
        sendData = DB.DBClass()
        sendData.addData(productNameText.text(), productCountText.text(), productBuyText.text())




class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.dialog = AddDataWindow(self)

        self.initUI()


    def initUI(self):

        glayout = QGridLayout()

        createAction = QAction('&Create graphic', self)
        createAction.triggered.connect(self.createGraph)

        uploadAction = QAction('&Upload graphic', self)
        uploadAction.triggered.connect(self.uploadGraph)

        addDataAction = QAction('&Add data', self)
        addDataAction.triggered.connect(self.DbAddData)

        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(createAction)
        fileMenu.addAction(uploadAction)
        fileMenu.addAction(addDataAction)

        global graphicLabel
        graphicLabel = QLabel('test', self)
        global pixmap 
        
        glayout.addWidget(graphicLabel, 1, 1)
        graphicLabel.move(0, 100)

        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Graphic viewer')
        self.setLayout(glayout)
        self.show()        
    
    
    def createGraph(self):
        graphCreate.drawGraphs()

    def uploadGraph(self):
        pixmap = QPixmap()
        pixmap.load('outputGraph.png')

        graphicLabel.resize(pixmap.width(), pixmap.height())
        graphicLabel.setPixmap(pixmap)

    def DbAddData(self):
        self.dialog.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())