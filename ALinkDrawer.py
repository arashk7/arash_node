from PyQt5 import QtCore, QtGui, QtWidgets
from ALinkGUI import ALinkGUI
from AGraphPort import AGraphPort


class ALinkDrawer:
    def __init__(self):
        self.link = ALinkGUI('link_drawer', QtCore.QPoint(0, 0), QtCore.QPoint(1, 1))
        self.widget = None
        self.link.hide()
        self.press_node = None

    def mouse_press_event(self, widget: QtWidgets.QGraphicsView, event: QtGui.QMouseEvent):
        self.widget = widget
        if event.button() == QtCore.Qt.LeftButton:
            self.press_node = widget.itemAt(event.pos())
            if self.press_node:
                if self.press_node.data(0) == 'port':
                    # if self.press_node.port_type == AGraphPort.PortType.OUTPUT:
                    print('port')
            pos = widget.mapToScene(QtCore.QPoint(event.x(), event.y()))
            # self.link.show()
            self.link.start_point = pos

    def mouse_move_event(self, event: QtGui.QMouseEvent):
        if self.widget:
            pos = self.widget.mapToScene(QtCore.QPoint(event.x(), event.y()))
            self.link.end_point = pos

    def mouse_release_event(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            self.link.hide()
