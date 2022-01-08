import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice

if __name__ == "__main__":
    app = QApplication(sys.argv)

    ui_file_name = "src\gui\main_gui.ui"
    ui_file = QFile(ui_file_name)
    if not ui_file.open(QIODevice.ReadOnly):
        print(f"Cannot open {ui_file_name}: {ui_file.errorString()}")
        sys.exit(-1)
    loader = QUiLoader()
    window = loader.load(ui_file)
    ui_file.close()
    if not window:
        print(loader.errorString())
        sys.exit(-1)
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


    window.pushButton.clicked.connect(testprint)

    app.exec()
