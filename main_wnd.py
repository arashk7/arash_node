from PyQt5 import QtCore, QtGui, QtWidgets, uic
from AGraphWidget.AWidget import AWidget
from AGraphWidget.AConfig import AConfig
from APlugin.APluginManager import APluginManager
from AGraphWidget.AUtil import ASharedItems

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        # Instantiate AWinode.ports_indget No data returned (timeout while sending data).t
        self.awidget = AWidget(self, graph_id='graph_1')
        uic.loadUi('ui/mainForm.ui',self)
        self.vl = self.findChild(QtWidgets.QVBoxLayout, 'vLayout')
        # self.vl.
        self.vl.addWidget(self.awidget)
        # self.wnd.addWidget(self.awidget)
        ASharedItems.awidget = self.awidget

        pm = APluginManager(self.awidget)
        pm.load_dir()
        pm.inset_to_widget(pm.items[0])
        pm.inset_to_widget(pm.items[1])
        pm.inset_to_widget(pm.items[2])
        pm.inset_to_widget(pm.items[2])

        # self.awidget.setDisabled(True)

        VBlayout = QtWidgets.QVBoxLayout(self)

        # Add awidget to the window
        VBlayout.addWidget(self.awidget)
        # HBlayout = QtWidgets.QHBoxLayout()
        # HBlayout.setAlignment(QtCore.Qt.AlignLeft)
        # VBlayout.addLayout(HBlayout)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = Window()
    window.setGeometry(300, 300, 1768, 874)
    window.show()
    sys.exit(app.exec_())
