from PyQt5 import QtCore, QtGui, QtWidgets, uic
from AGraphWidget.AWidget import AWidget
from AGraphWidget.AConfig import AConfig
from APlugin.APluginManager import APluginManager
from AGraphWidget.AUtil import ASharedItems


class DraggableLabel(QtWidgets.QLabel):
    def __init__(self, text, item_id):
        super(QtWidgets.QLabel, self).__init__(text)
        self.item_id = item_id

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
        mimedata.setText(self.item_id)
        drag.setMimeData(mimedata)
        pixmap = QtGui.QPixmap(self.size())
        painter = QtGui.QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()
        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        drag.exec_(QtCore.Qt.CopyAction)


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
        page1.layout().setAlignment(QtCore.Qt.AlignTop)
        page1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)

        label1 = DraggableLabel('testttt', 1)
        #
        page1.layout().addWidget(label1)

        pm = APluginManager(self.awidget)
        pm.load_dir()
        ASharedItems.aPluginManager = pm
        for i in range(len(pm.items)):
            label = DraggableLabel(pm.items[i].node_type, str(i))
            page1.layout().addWidget(label)
            # pm.inset_to_widget(item=item)
            # pm.inset_to_widget(pm.items[0])
            # pm.inset_to_widget(pm.items[1])
            # pm.inset_to_widget(pm.items[2])
            # pm.inset_to_widget(pm.items[2])


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(300, 300, 1768, 874)
    window.show()
    sys.exit(app.exec_())
