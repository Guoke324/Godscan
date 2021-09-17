# !/usr/bin/env python
# coding=utf-8
# ---- ---- ---- ----
# @Author: Guoke324 
# @Date: 2021-08-14 10:45:06
# @Email: querysoft2019@outlook.com
# @LastEditTime: 2021-08-14 10:45:07

import sys
from vuln_scan_GUI import Ui_MainWindow
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor,QBrush,QIcon
from PyQt5.QtWidgets import QHeaderView, QTableWidgetItem, QHBoxLayout


class MainUI(Ui_MainWindow, QMainWindow):

    def __init__(self, parent=None):
        super(MainUI, self).__init__(parent)
        self.setupUi(self)        
        self.actionFOFA.triggered.connect(self.fofa)
        self.action_6.triggered.connect(self.project)
        self.action_3.triggered.connect(self.helps)
        self.action_4.triggered.connect(self.updata)
        self.action_5.triggered.connect(self.about)
        self.menu_3.triggered[QAction].connect(self.theme)



    def about(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.about(self, '关于作者', '这家伙很懒什么也没留下！')

    def fofa(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.warning(self, '提示', '暂未发开完成，敬请期待！', QMessageBox.Yes | QMessageBox.Yes)

    def theme(self,q):
        print(q.text()+'is triggeres')
        if q.text() == '默认风格':
            MainUI.setStyleSheet(self,'')
        elif q.text() == "灰暗炫酷":
            MainUI.setStyleSheet(self,'')
            MainUI.setStyleSheet(self,"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(158, 99, 79, 255), stop:1 rgba(255, 255, 255, 255));")
        elif q.text() == "蓝色渐变":
            MainUI.setStyleSheet(self,'')
            MainUI.setStyleSheet(self,"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 139, 159, 255), stop:1 rgba(255, 255, 255, 255));")
        elif q.text() == "青青草原":
            MainUI.setStyleSheet(self,'')
            MainUI.setStyleSheet(self,"background-color: rgb(85, 170, 127);")
        elif q.text() == "test":
            MainUI.setStyleSheet(self,'')
            MainUI.setStyleSheet(self,"background-image: url(:/新前缀/1223.jpg);")
            box = QtWidgets.QMessageBox()
            box.setIcon(1)
            box.warning(self, '提示', '还没想好，敬请期待！', QMessageBox.Yes | QMessageBox.Yes)

    def helps(self):
        webbrowser.open("file://test.html")

    def project(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.information (self, '项目地址', 'http://baidu.com', QMessageBox.Yes | QMessageBox.Yes)

    def updata(self):
        box = QtWidgets.QMessageBox()
        box.setIcon(1)
        box.warning(self, '提示', '请前往项目地址进行更新查看！', QMessageBox.Yes | QMessageBox.Yes)

      

    def closeEvent(self, event):       
        reply = QMessageBox.question(self, '提示',
            "你确认退出吗?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()   


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainUI()
    main.show()
    sys.exit(app.exec_())