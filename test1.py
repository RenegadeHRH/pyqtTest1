# author: HRH

# date: 2022/3/9

# PyCharm
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QMainWindow,QDesktopWidget,QPushButton,QHBoxLayout
from PyQt5.QtGui import QIcon
import time


class FirstMainWin(QMainWindow):
    def __init__(self,parent=None):
        super(FirstMainWin,self).__init__(parent)
        self.setWindowTitle("第一个主窗口应用")
        self.resize(400,300)
        # self.staus=self.statusBar()
        self.move(int(0),int(0))
        # self.staus.showMessage('初始化：'+str(i),1000)
        self.button1=QPushButton('退出应用')
        self.button1.clicked.connect(self.onClick_Button1)
        layout=QHBoxLayout()
        layout.addWidget(self.button1)
        self.center()
        mainFrame=QWidget()
    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size=self.geometry()
        newLeft=(screen.width()-size.width())/2
        newTop=(screen.height()-size.height())/2
        self.move(int(newLeft),int(newTop))
    def onClick_Button1(self):
        sender = self.sender()
        print(sender.text()+'Button push')
        app=QApplication.instance()
        app.quit()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    mainWin=FirstMainWin()

    mainWin.show()
    sys.exit(app.exec_())