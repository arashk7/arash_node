from PyQt5 import QtCore, QtGui, QtWidgets
import math
# from qtconsole.qt import QtGui
from AGraphWidget.AUtil import APortType

from AGraphWidget.ASkin import *


class APortGUI(QtWidgets.QGraphicsItem):
    def __init__(self, port, port_id, port_type, x=100, y=100):
        super(APortGUI, self).__init__()
        self.port_id = port_id
        self.port = port
        self.setData(0, 'port')
        self.setZValue(1)
        self.port_type = port_type
        self.node_id = None
        self.x = x
        self.y = y
        self.rect = QtCore.QRectF(x, y, 20, 20)
        self.rect_collider = QtCore.QRectF(x, y, 20, 20)

        self.pos = QtCore.QPointF(0, 0)
        self.draw_collider = False

        self.__highlight = False

    @property
    def highlight(self):
        return self.__highlight

    @highlight.setter
    def highlight(self, is_highlight):
        self.__highlight = is_highlight
        self.update()

    def boundingRect(self):
        p = self.scenePos() + QtCore.QPointF(self.x, self.y) + QtCore.QPointF(self.rect.width() / 2,
                                                                              self.rect.height() / 2)
        self.pos.setX(p.x())
        self.pos.setY(p.y())

        self.rect_collider = QtCore.QRectF(self.x, self.y,
                                           self.rect.width(), self.rect.height())
        return self.rect_collider

    def set_pos(self, x, y):
        self.x = x
        self.y = y

    def paint(self, painter: QtGui.QPainter, style: QtWidgets.QStyleOptionGraphicsItem, widget=None):
        # self.__rect.setX(self.x)
        # self.__rect.setY(self.y)
        x = self.x  # .__rect.x()
        y = self.y  # __rect.y()
        w = self.rect.width()
        h = self.rect.height()

        # main rounded rect
        path = QtGui.QPainterPath()
        path.addEllipse(x, y, w, h)

        brush = QtGui.QBrush(QtGui.QColor(100, 250, 250, 100))
        if self.__highlight:
            brush = QtGui.QBrush(QtGui.QColor(250, 250, 250, 200))
        elif self.port.is_connected():
            brush = QtGui.QBrush(QtGui.QColor(100, 100, 100, 150))
        pen = QtGui.QPen(QtGui.QColor(250, 250, 250, 100))

        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)

        # Connect circle
        if self.port.is_connected():
            path = QtGui.QPainterPath()
            path.addEllipse(x + w / 2 - 5, y + h / 2 - 5, 10, 10)
            brush = QtGui.QBrush(QtGui.QColor(250, 250, 250, 100))
            pen = QtGui.QPen(QtGui.QColor(250, 250, 250, 100))
            painter.setBrush(brush)
            painter.setPen(pen)
            painter.drawPath(path)

        if self.draw_collider:
            brush = QtGui.QBrush(QtGui.QColor(250, 250, 250, 50))
            painter.setBrush(brush)
            painter.drawRect(self.rect_collider)
