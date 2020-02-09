from PyQt5 import QtCore, QtGui, QtWidgets
import math
# from qtconsole.qt import QtGui
from AGraphWidget.AUtil import APortType

from AGraphWidget.ASkin import *


class APortGUI(QtWidgets.QGraphicsItem):
    def __init__(self, port ,port_id, port_type, x=100, y=100):
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
        pen = QtGui.QPen(QtGui.QColor(250, 250, 250, 100))
        # if self.isConnected:
        # pen = QtGui.QPen(self.connectedColor)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)

        if self.draw_collider:
            brush = QtGui.QBrush(QtGui.QColor(250, 250, 250, 50))
            painter.setBrush(brush)
            painter.drawRect(self.rect_collider)
