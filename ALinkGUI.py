from PyQt5 import QtCore, QtGui, QtWidgets
import math


class ALinkGUI(QtWidgets.QGraphicsItem):
    def __init__(self, link_id, start=None, end=None):
        super().__init__()
        self.id = link_id

        self.setData(0, 'link')
        self.setZValue(1)
        self.link_type = None

        self.start_point = None
        self.end_point = None

        self.start = start
        self.end = end

        self.update_line(start, end)

    def update_line(self, start=None, end=None):
        # check exact type of the object "if type(o) is str:"
        # check whether instance or subclass of our type "isinstance(..,..)"
        if isinstance(self.start, QtCore.QPoint) and isinstance(self.end, QtCore.QPoint):
            self.start_point = start
            self.end_point = end
        elif isinstance(self.start, QtCore.QPoint) and isinstance(self.end, QtWidgets.QGraphicsItem):
            self.start_point = start
            self.end_point = QtCore.QPointF(self.end.x(), self.end.y())
        elif isinstance(self.start, QtWidgets.QGraphicsItem) and isinstance(self.end, QtCore.QPoint):
            self.start_point = QtCore.QPointF(self.start.pos.x(), self.start.pos.y())
            self.end_point = end
        elif isinstance(self.start, QtWidgets.QGraphicsItem) and isinstance(self.end, QtWidgets.QGraphicsItem):
            self.start_point = QtCore.QPointF(self.start.x(), self.start.y())
            self.end_point = QtCore.QPointF(self.end.x(), self.end.y())
        else:
            print('error')

    def paint(self, painter: QtGui.QPainter, QStyleOptionGraphicsItem, widget=None):
        self.draw_bezier_curve(painter, self.start_point, self.end_point)


    def boundingRect(self):
        start = self.start_point
        end = self.end_point
        ex = max([start.x(), end.x()])
        ey = max([start.y(), end.y()])
        sx = min([start.x(), end.x()])
        sy = min([start.y(), end.y()])
        w = ex - sx
        h = ey - sy

        return QtCore.QRectF(sx, sy, w, h)

    def distance(self, p1: QtCore.QPointF, p2: QtCore.QPointF):
        dist = math.hypot(p2.x() - p1.x(), p2.y() - p1.y())
        return dist

    def draw_bezier_curve(self, painter: QtGui.QPainter, start, end):
        path = QtGui.QPainterPath()
        path.moveTo(start.x(), start.y())
        # path.quadTo(30, 30, 30, 200)
        mx1 = (end.x() + start.x()) / 2
        my1 = (end.y() + start.y()) / 2
        mx2 = (end.x() + start.x()) / 2
        my2 = (end.y() + start.y()) / 2

        # dx1 = (end.x()-start.x())/4+start.x()
        # dy1 = (end.y()-start.y())/4+start.y()
        # dx2 = (end.x()-start.x())/4-end.x()
        # dy2 = (end.y()-start.y())/4-end.y()
        # dx = (end.x()-start.x())/4
        dist = self.distance(start, end) / 4
        dist = 100 if dist > 100 else dist

        path.cubicTo(start.x(), start.y(), start.x(), start.y() + dist, mx1, my1)
        # path.cubicTo(start.x(), start.y() + d, start.x(), my1, mx1, my1)
        # path.cubicTo(mx2, my2, end.x(), my2, end.x(), end.y() - d)
        path.cubicTo(mx2, my2, end.x(), end.y() - dist, end.x(), end.y())
        # else:
        #     path.cubicTo(start.x(), start.y(), mx1, start.y(), mx1, my1)
        #     path.cubicTo(mx2, my2, mx2, end.y(), end.x(), end.y())
        color = QtGui.QColor(255, 255, 255, 200)
        pen = QtGui.QPen(color, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)
