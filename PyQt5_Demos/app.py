from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (QMainWindow, QApplication, QInputDialog, QColorDialog, QFontDialog, QFileDialog)
from PyQt5.QtGui import QColor
from demo import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.ui = QInputDialog
        self.uf = QFileDialog
        self.ut = QFontDialog
        self.cl = QColorDialog

        col = QColor(0, 255, 255)
        self.Frame.setStyleSheet("QWidget { background-color: %s }" % col.name())

        self.textEdit.setStyleSheet("QWidget { background-color: %s }" % col.name())

        openfile = self.actionOpen
        openfile.setShortcut('Ctrl+O')
        openfile.setStatusTip('Open new files')
        openfile.triggered.connect(self.showFDialog)

        savefile = self.actionSave
        savefile.setShortcut('Ctrl+S')
        savefile.setStatusTip('Save changed files')
        lcd = self.LcdNumber
        self.HorizontalSlider.valueChanged.connect(lcd.display)

        self.PushButton1.clicked.connect(self.showDialog)
        self.PushButton2.clicked.connect(self.showFRDialog)
        self.pushButton3.clicked.connect(self.showCLDialog)
        self.show()

    def showDialog(self):
        text, ok = self.ui.getText(self, 'Input Dialog', 'Enter your name')
        if ok:
            self.label.setText(str(text))

    def showFDialog(self):
        fname = self.uf.getOpenFileName(self, 'open file', '/home')

        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)

    def showFRDialog(self):
        font, ok = self.ut.getFont()
        if ok:
            self.textEdit.setFont(font)

    def showCLDialog(self):
        col = self.cl.getColor()
        if col.isValid():
            self.Frame.setStyleSheet("QWidget { background-color: %s }" % col.name())

if __name__ == "__main__":
    import sys

    QCoreApplication.setApplicationName("Teddy")
    QCoreApplication.setApplicationVersion("1.02")
    QCoreApplication.setOrganizationName("Zhang")
    QCoreApplication.setOrganizationDomain("http://luckboy.com")

    app = QApplication(sys.argv)
    form = Main()
    sys.exit(app.exec_())
