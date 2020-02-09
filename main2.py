from PyQt5 import QtCore, QtGui, QtWidgets
from AGraphWidget.AWidget import AWidget
from AGraphWidget.AConfig import AConfig
from APlugin.AToolManager import AToolManager

class Window(QtWidgets.QWidget):
    def __init__(self):
        super(Window, self).__init__()

        # Instantiate AWidgeNo data returned (timeout while sending data).t
        self.awidget = AWidget(self, graph_id='graph_1')
        AConfig.awidget = self.awidget

        tm = AToolManager()
        tm.load_dir()
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
