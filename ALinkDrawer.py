from PyQt5 import QtCore, QtGui, QtWidgets
from ALinkGUI import ALinkGUI


class ALinkDrawer:
    def __init__(self):
        self.link = ALinkGUI('link_drawer', QtCore.QPoint(0, 0), QtCore.QPoint(1, 1))
        self.widget =None
        self.link.hide()

    def mouse_press_event(self, widget: QtWidgets.QGraphicsView, event: QtGui.QMouseEvent):
        self.widget = widget
        if event.button() == QtCore.Qt.LeftButton:
            pos = widget.mapToScene(QtCore.QPoint(event.x(), event.y()))
            self.link.show()
            self.link.start_point = pos


    def mouse_move_event(self, event: QtGui.QMouseEvent):
        if self.widget:
            pos = self.widget.mapToScene(QtCore.QPoint(event.x(), event.y()))
            self.link.end_point = pos


    def mouse_release_event(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            self.link.hide()

