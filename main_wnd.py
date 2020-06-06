from PyQt5 import QtCore, QtGui, QtWidgets, uic
from AGraphWidget.AWidget import AWidget
from APlugin.APluginManager import APluginManager
from AGraphWidget.AUtil import ASharedItems
from ANodeRunner.ANodePlayer import ANodePlayer
from AGraphWidget.APropertyManager import APropertyManager

class DraggableLabel(QtWidgets.QLabel):
    def __init__(self, text, item_id):
        super(QtWidgets.QLabel, self).__init__(text)
        self.item_id = item_id



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


class Color(QtWidgets.QWidget):
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QtGui.QPalette.Window, QtGui.QColor(color))
        self.setPalette(palette)

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Instantiate AWinode.ports_indget No data returned (timeout while sending data).t
        self.awidget = AWidget(self, graph_id='graph_1')
        ASharedItems.awidget = self.awidget
        uic.loadUi('ui/mainForm.ui', self)
        self.setCentralWidget(self.awidget)

        # Node Player
        # node_player = ANodePlayer(self.awidget)
        # self.toolBox = self.findChild(QtWidgets.QToolBox, 'toolBox')
        # self.act_play = self.findChild(QtWidgets.QPushButton, 'pushButton')
        # if self.act_play:
        #     print ('found')
        #     self.act_play.clicked.connect(node_player.exec_recursive)


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


        property_manager = APropertyManager(self)
        # property_manager.update_property_bar()
        ASharedItems.aPropertyManager = property_manager
        # Test Property bar
        # self.tw = QtWidgets.QTreeWidget(self)
        # self.verticalLayout_PropertyBar.addWidget(self.tw)
        # self.tw.setColumnCount(2)
        # self.tw.setHeaderLabels(["Properties", "Value"])
        #
        # root_1 = QtWidgets.QTreeWidgetItem(self.tw)
        # root_1.setText(0, "Option_1")
        # root_1.setText(1, "Option_1 Description")
        #
        # item_1 = QtWidgets.QTreeWidgetItem()
        # item_1.setText(0, "enabled")
        # item_1.setFlags(item_1.flags() | QtCore.Qt.ItemIsUserCheckable)
        # item_1.setCheckState(1, QtCore.Qt.Checked)
        # root_1.addChild(item_1)
        #
        # item_1 = QtWidgets.QTreeWidgetItem()
        # item_1.setText(0, "height")
        # root_1.addChild(item_1)
        # self.tw.setItemWidget(item_1, 1, QtWidgets.QSpinBox())
        #
        # root_2 = QtWidgets.QTreeWidgetItem(self.tw)
        # root_2.setText(0, "Option_2")
        # root_2.setText(1, "Option_2 Description")
        #
        # item_2 = QtWidgets.QTreeWidgetItem()
        # item_2.setText(0, "width")
        # item_2.setText(1, "300")
        # root_2.addChild(item_2)
        #
        # item_2 = QtWidgets.QTreeWidgetItem()
        # item_2.setText(0, "height")
        # item_2.setText(1, "200")
        # root_2.addChild(item_2)
        #
        # btnNext = QtWidgets.QPushButton("Next")
        #
        # self.verticalLayout_PropertyBar.addWidget(btnNext)
        # self.verticalLayout_PropertyBar.setAlignment(QtCore.Qt.AlignTop)









if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(150, 150, 1768, 874)
    window.show()
    sys.exit(app.exec_())
