from PyQt5 import QtCore, QtGui, QtWidgets
import math
from qtconsole.qt import QtGui

from ASkin import *


class APortGUI(QtWidgets.QGraphicsItem):
    def __init__(self, port_id,node_gui, x=100, y=100):
        super(APortGUI, self).__init__()
        self.__id = port_id
        self.setData(0, 'port')
        self.__node_gui = node_gui
        self.x = x
        self.y = y
        self.__rect = QtCore.QRectF(x, y, 10, 10)
        self.setParentItem(self.__node_gui)


    def boundingRect(self):
        rect = QtCore.QRectF(self.__rect)
        return rect

    def distance(self, p1: QtCore.QPointF, p2: QtCore.QPointF):
        dist = math.hypot(p2.x() - p1.x(), p2.y() - p1.y())
        return dist

    def paint(self, painter: QtGui.QPainter, style: QtWidgets.QStyleOptionGraphicsItem, widget=None):
        x = self.__rect.x()
        y = self.__rect.y()
        w = self.__rect.width()
        h = self.__rect.height()

        # main rounded rect
        path = QtGui.QPainterPath()
        path.addEllipse(x, y, w, h)

        brush = QtGui.QBrush(QtGui.QColor(100, 250, 250, 100))
        pen = QtGui.QPen(QtGui.QColor(250, 250, 250, 100))
        # if self.isConnected:
        # pen = QtGui.QPen(self.connectedColor)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)
