from PyQt5 import QtCore, QtGui, QtWidgets
from AGraphWidget.AWidget import AWidget
from AGraphWidget.AConfig import AConfig
from APlugin.APluginManager import APluginManager
from AGraphWidget.AUtil import ASharedItems

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        # Instantiate AWinode.ports_indget No data returned (timeout while sending data).t
        self.awidget = AWidget(self, graph_id='graph_1')
        ASharedItems.awidget = self.awidget

        tm = APluginManager(self.awidget)
        tm.load_dir()
        tm.inset_to_widget(tm.items[0])
        tm.inset_to_widget(tm.items[1])
        tm.inset_to_widget(tm.items[2])
        tm.inset_to_widget(tm.items[2])

        # self.awidget.setDisabled(True)

        VBlayout = QtWidgets.QVBoxLayout(self)

        # Add awidget to the window
        VBlayout.addWidget(self.awidget)
        HBlayout = QtWidgets.QHBoxLayout()
        HBlayout.setAlignment(QtCore.Qt.AlignLeft)
        VBlayout.addLayout(HBlayout)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(300, 300, 1768, 874)
    window.show()
    sys.exit(app.exec_())
