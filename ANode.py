from PyQt5 import QtCore, QtGui, QtWidgets
from ABaseNode import ABaseNode
from ASkin import *


class ANode(QtWidgets.QGraphicsItem, ABaseNode):
    def __init__(self, node_id, rect: QtCore.QRectF):
        ABaseNode.__init__(self, node_id)
        QtWidgets.QGraphicsItem.__init__(self, node_id=node_id)

        self.id = node_id
        self.caption = node_id
        self.__rect = rect
        self.setData(0, 'node')
        self.__selected = True

        # Node Setting
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

        self.setZValue(1)
        self.__group = AGroup.NORMAL

    def setSelected(self,selected):
        self.__selected=selected
        super(ANode,self).setSelected(selected)


    def isSelected(self):
        return self.__selected


    def boundingRect(self):
        # You will be able to edit this rectangle which affect your physical interaction with mouse
        rect = QtCore.QRectF(self.__rect)
        return rect

    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionGraphicsItem, widget=None):
        x = self.__rect.x()
        y = self.__rect.y()
        w = self.__rect.width()
        h = self.__rect.height()

        # Highlighting rounded rectangle
        if self.__selected:
            path = QtGui.QPainterPath()
            path.addRoundedRect(x - 2.5, y - 2.5, w + 5, h + 5, 5, 5)
            brush = QtGui.QBrush(ASkin.color(ARole.SELECT_HIGHLIGHT))
            pen = QtGui.QPen()
            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawPath(path)

        # Main rounded rect
        path = QtGui.QPainterPath()
        path.addRoundedRect(x, y, w, h, 10, 10)
        brush = QtGui.QBrush(ASkin.color(ARole.NODE_WND, self.__group))
        pen = QtGui.QPen()
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)

        # add caption bar
        path = QtGui.QPainterPath()
        color = QtGui.QColor(20, 20, 20, 250)
        brush = QtGui.QBrush(color)
        pen = QtGui.QPen(color)
        pen.setWidth(0)
        path.moveTo(x, y + 20)
        path.lineTo(x, y + 10)
        path.cubicTo(x, y + 10, x, y, x + 10, y)
        path.lineTo(x + w - 10, y)
        path.cubicTo(x + w - 10, y, x + w, y, x + w, y + 10)
        path.lineTo(x + w, y + 20)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)

        # add caption text
        path = QtGui.QPainterPath()
        color = ASkin.color(ARole.NODE_WND_CAP_TEXT)
        brush = QtGui.QBrush(color)
        pen = QtGui.QPen(color)
        pen.setWidth(0)
        font = QtGui.QFont("arial", 7)
        path.addText(x + 5, y + 15, font, str(self.caption))
        painter.setFont(font)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)
