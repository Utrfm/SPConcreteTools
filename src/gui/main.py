import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
# from PySide6.QtUiTools import QUiLoader
# from PySide6.QtWidgets import *
# from PySide6.QtCore import QFile, QIODevice
from main_gui import Ui_MainWindow

# import modules.sofistik_cdb.cdbwork as cdb

# if __name__ == "__main__":
#     app = QApplication(sys.argv)

#     ui_file_name = "src\gui\main_gui.ui"
#     ui_file = QFile(ui_file_name)
#     if not ui_file.open(QIODevice.ReadOnly):
#         print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
#         sys.exit(-1)
#     loader = QUiLoader()
#     window = loader.load(ui_file)
#     ui_file.close()
#     if not window:
#         print(loader.errorString())
#         sys.exit(-1)
#     window.show()
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    
    def OpenReadCDB():
        pass

    

    

    def testprint():
        print('test')
        # Draw()
        h = window.sb_SectionHeight.value()
        print(h)
        # a1 = window.comboBox.currentIndex()
        # a2 = window.comboBox.currentText()
        # print(a1, a2)


    def Draw():
        sectB = int(window.tableWidget.item(0, 0).text())
        print(sectB)
        sectH = int(window.tableWidget.item(1, 0).text())
        print(sectH)
        scene = QtWidgets.QGraphicsScene()
        scene.addText("Hello, world!")
        scene.addRect(0, 0, sectB, sectH)
        window.graphicsView.setScene(scene)
        window.graphicsView.scale(0.5, 0.5)
        # view = graphicsView(scene)
        # view.setBackgroundBrush(QtGui.QBrush(QtGui.QColor(127,100,255,80)))
        # view.show()

    def Dg():
        file , check = QFileDialog.getOpenFileName(None, "QFileDialog.getOpenFileName()",
                                               "", "All Files (*);;Sofistik Database (*.cdb)")
        if check:
            print(file)
            window.OpenFileLabel.setText(file)

    # window.pushButton.clicked.connect(testprint)
    window.pBOpenFile.clicked.connect(Dg)
    
    # window.listWidget.addItem(QListWidgetItem(QCheckBox("text")))
    # listGroups = [14,15,25,35]
    # for i in range(len(listGroups)):
    #     window.listWidget.addItem(QCheckBox('text'))
    

    app.exec()
