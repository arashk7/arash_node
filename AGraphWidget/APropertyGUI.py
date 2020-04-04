from PyQt5 import QtCore, QtGui, QtWidgets
import math
# from qtconsole.qt import QtGui
from AGraphWidget.AUtil import APropertyType, APropertyLocation, ASharedItems, AMath

from AGraphWidget.ASkin import *
from PyQt5.QtWidgets import QLineEdit, QBoxLayout


class APropertyGUI(QtWidgets.QGraphicsItem):
    def __init__(self, property, property_id, property_type, property_location):
        super(APropertyGUI, self).__init__()
        self.property_id = property_id
        self.property = property
        self.property_type = property_type
        self.property_location = property_location
        self.setData(0, 'property')
        self.setZValue(1)
        self.value = None

        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)

        self.node_id = None
        self.x = 0
        self.y = 0
        self.rect = QtCore.QRectF(self.x, self.y, property.node.gui.rect.width(), 20)
        self.rect_collider = QtCore.QRectF(self.x, self.y, property.node.gui.rect.width(),
                                           20)

        self.pos = QtCore.QPointF(0, 0)
        self.draw_collider = False

        self.control_proxy = None
        self.control = None

        self.first = True

    def init(self):
        self.control = QtWidgets.QLineEdit()
        self.control.setText(self.property_id)
        self.control.setFixedSize(self.rect.width(), self.rect.height())
        self.control_proxy: QtWidgets.QGraphicsProxyWidget = ASharedItems.awidget.scene().addWidget(self.control)
        self.control_proxy.setZValue(2)

        ASharedItems.awidget.mouse_press_event.connect()

    def boundingRect(self):
        p = self.scenePos() + QtCore.QPointF(self.x, self.y) + QtCore.QPointF(self.rect.width() / 2,
                                                                              self.rect.height() / 2)
        self.pos.setX(p.x())
        self.pos.setY(p.y())

        p -= QtCore.QPointF(self.rect.width() / 2, self.rect.height() / 2)
        self.rect_collider = QtCore.QRectF(self.x, self.y,
                                           self.rect.width(), self.rect.height())
        # print(str(p.x())+' , '+str(p.y()))
        if self.first:
            self.control_proxy.setPos(p.x(), p.y())
            self.first = False

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

        path = QtGui.QPainterPath()
        path.addRect(x, y, w, h)
        brush = QtGui.QBrush(ASkin.color(ARole.NODE_PROPERTY, AGroup.NORMAL))
        pen = QtGui.QPen()
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)

        # draw collider
        if self.draw_collider:
            path = QtGui.QPainterPath()
            path.addRect(self.rect_collider.x(), self.rect_collider.y(), self.rect_collider.width(),
                         self.rect_collider.height())
            brush = QtGui.QBrush(QtGui.QColor(100, 250, 100, 250))
            pen = QtGui.QPen()
            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawPath(path)

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
