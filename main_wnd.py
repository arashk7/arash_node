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
        ASharedItems.awidget = self.awidget
        uic.loadUi('ui/mainForm.ui', self)
        self.setCentralWidget(self.awidget)

        self.toolBox = self.findChild(QtWidgets.QToolBox, 'toolBox')
        # page1 = QtWidgets.QWidget(self)
        #
        # page = self.toolBox.addItem(page1, 'page_test')
        #
        # if page:
        #     print('ok')
        # else:
        #     print('nok')
        # page1.setLayout(QtWidgets.QVBoxLayout())
        # page1.layout().setAlignment(QtCore.Qt.AlignTop)
        # page1.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        #
        # label1 = DraggableLabel('testttt', 1)
        # #
        # page1.layout().addWidget(label1)
        # w=self.toolBox.findChild(QtWidgets.QWidget,'page_2')

        # if w:
        #     print('ok')
        # else:
        #     print('nok')

        pm = APluginManager(self.awidget)
        pm.load_dir()
        ASharedItems.aPluginManager = pm
        pages=dict()

        for i in range(len(pm.items)):
            if pm.items[i].category not in pages:
                pages[pm.items[i].category] = QtWidgets.QWidget(self)
                self.toolBox.addItem(pages[pm.items[i].category], pm.items[i].category)
                pages[pm.items[i].category].setLayout(QtWidgets.QVBoxLayout())
                pages[pm.items[i].category].layout().setAlignment(QtCore.Qt.AlignTop)
                pages[pm.items[i].category].setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
                label = DraggableLabel(pm.items[i].node_type, str(i))
                pages[pm.items[i].category].layout().addWidget(label)
            else:
                label = DraggableLabel(pm.items[i].node_type, str(i))
                pages[pm.items[i].category].layout().addWidget(label)





if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(300, 300, 1768, 874)
    window.show()
    sys.exit(app.exec_())
