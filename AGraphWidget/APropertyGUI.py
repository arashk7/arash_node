from PyQt5 import QtCore, QtGui, QtWidgets
import math
# from qtconsole.qt import QtGui
from AGraphWidget.AUtil import APropertyType, APropertyLocation

from AGraphWidget.ASkin import *
from PyQt5.QtWidgets import QLineEdit, QBoxLayout
from AGraphWidget.AUtil import ASharedItems


class APropertyGUI(QtWidgets.QGraphicsItem):
    def __init__(self, property, property_id, property_type, property_location, x=100, y=100):
        super(APropertyGUI, self).__init__()
        self.property_id = property_id
        self.property = property
        self.property_type = property_type
        self.property_location = property_location
        self.setData(0, 'property')
        self.setZValue(1)

        self.node_id = None
        self.x = x
        self.y = y
        self.rect = QtCore.QRectF(x, y, 50, 10)
        self.rect_collider = QtCore.QRectF(x, y, 50, 10)

        self.pos = QtCore.QPointF(0, 0)
        self.draw_collider = False

    def init(self):
        self.item = QtWidgets.QLineEdit()
        self.item.setText(self.property_id)
        self.wid: QtWidgets.QGraphicsProxyWidget = ASharedItems.awidget.scene().addWidget(self.item)
        self.wid.setZValue(2)

    def boundingRect(self):
        p = self.scenePos() + QtCore.QPointF(self.x, self.y) + QtCore.QPointF(self.rect.width() / 2,
                                                                              self.rect.height() / 2)
        self.pos.setX(p.x())
        self.pos.setY(p.y())

        self.rect_collider = QtCore.QRectF(self.x, self.y,
                                           self.rect.width(), self.rect.height())
        # self.wid.setGeometry(QtCore.QRect(p.x(), p.y()-10, self.rect.width(), self.rect.height()))
        self.wid.setPos(p.x(), p.y())
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
        # path = QtGui.QPainterPath()
        # path.addEllipse(x, y, w, h)
        #
        # brush = QtGui.QBrush(QtGui.QColor(100, 250, 250, 100))
        #
        # pen = QtGui.QPen(QtGui.QColor(250, 250, 250, 100))
        # # if self.isConnected:
        # # pen = QtGui.QPen(self.connectedColor)
        # painter.setPen(pen)
        # painter.setBrush(brush)
        # painter.drawPath(path)
        #
        # # add param label
        # path = QtGui.QPainterPath()
        # color = ASkin.color(ARole.NODE_WND_PARAM_TEXT)
        # brush = QtGui.QBrush(color)
        # pen = QtGui.QPen(color)
        # pen.setWidth(0)
        # font = QtGui.QFont("arial", 7)
        #
        # # br = QtGui.QFontMetrics(font).boundingRect(self.caption)
        # # print(str(br.width()))
        #
        # if self.property_type == APropertyLocation.NODE:
        #     path.addText(x + 25, y + 12, font, str(self.property_id))
        # else:
        #     path.addText(x - 38, y + 12, font, str(self.property_id))
        # painter.setFont(font)
        # painter.setPen(pen)
        # painter.setBrush(brush)
        # painter.drawPath(path)
        #
        # if self.draw_collider:
        #     brush = QtGui.QBrush(QtGui.QColor(250, 250, 250, 50))
        #     painter.setBrush(brush)
        #     painter.drawRect(self.rect_collider)
