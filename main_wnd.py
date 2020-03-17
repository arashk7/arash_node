from PyQt5 import QtCore, QtGui, QtWidgets, uic
from AGraphWidget.AWidget import AWidget
from AGraphWidget.AConfig import AConfig
from APlugin.APluginManager import APluginManager
from AGraphWidget.AUtil import ASharedItems


class DraggableLabel(QtWidgets.QLabel):
    # def __init__(self, parent, text,image):
    #     super(QtWidgets.QLabel, self).__init__(parent,image)
    #     self.setText(text)
    #     self.setAcceptDrops(True)
    #     self.show()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.drag_start_position = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & QtCore.Qt.LeftButton):
            return
        if (event.pos() - self.drag_start_position).manhattanLength() < QtWidgets.QApplication.startDragDistance():
            return
        drag = QtGui.QDrag(self)
        mimedata = QtCore.QMimeData()
        mimedata.setText(self.text())
        drag.setMimeData(mimedata)
        pixmap = QtGui.QPixmap(self.size())
        painter = QtGui.QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(QtCore.Qt.CopyAction | QtCore.Qt.MoveAction)


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Instantiate AWinode.ports_indget No data returned (timeout while sending data).t
        self.awidget = AWidget(self, graph_id='graph_1')
        uic.loadUi('ui/mainForm.ui', self)
        self.setCentralWidget(self.awidget)

        self.toolBox = self.findChild(QtWidgets.QToolBox, 'toolBox')
        page1 = QtWidgets.QWidget(self)
        self.toolBox.addItem(page1, 'page_test')
        page1.setLayout(QtWidgets.QVBoxLayout())
        label1 = DraggableLabel('testttt')
        # self.setAcceptDrops(True)

        # pal = label1.palette()
        # pal.setColor(QtGui.QPalette.Window, QtGui.QColor(200, 200, 200))
        # label1.setPalette(pal)
        # label1.setAutoFillBackground(True)
        label2 = QtWidgets.QLabel('test_label')
        page1.layout().addWidget(label1)
        page1.layout().addWidget(label2)
        page1.layout().setAlignment(QtCore.Qt.AlignTop)
        page1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        # spacer = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # empty = QtWidgets.QWidget()
        # empty.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        # spacer = self.findChild(QtWidgets.QSpacerItem,'verticalSpacer')
        # page1.layout().addItem(spacer)

        ASharedItems.awidget = self.awidget

        pm = APluginManager(self.awidget)
        pm.load_dir()
        pm.inset_to_widget(pm.items[0])
        pm.inset_to_widget(pm.items[1])
        pm.inset_to_widget(pm.items[2])
        pm.inset_to_widget(pm.items[2])


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(300, 300, 1768, 874)
    window.show()
    sys.exit(app.exec_())
