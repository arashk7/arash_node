from PyQt5 import QtCore, QtGui, QtWidgets
from AGraphWidget.AUtil import ALinkType
import math


class ALinkGUI(QtWidgets.QGraphicsItem):
    def __init__(self, link_id, start=QtCore.QPointF(0, 0), end=QtCore.QPointF(1, 1)):
        super(ALinkGUI, self).__init__()
        self.id = link_id

        self.setData(0, 'link')
        self.setZValue(0)
        self.link_type = ALinkType.PORT

        self.start_point = None
        self.end_point = None

        self.start = start
        self.end = end
        self.update_line(start, end)

        self.setEnabled(False)

        self.draw_collider = False
        # if isinstance(self.start,type(APortGUI))
        # self.setParentItem(self.start)

    def update_line(self, start=None, end=None):
        # check exact type of the object "if type(o) is str:"
        # check whether instance or subclass of our type "isinstance(..,..)"
        if start and end:
            if isinstance(start, QtCore.QPointF) and isinstance(end, QtCore.QPointF):
                self.start_point = start
                self.end_point = end
            elif isinstance(start, QtCore.QPointF) and isinstance(end, QtWidgets.QGraphicsItem):
                self.start_point = start
                self.end_point = QtCore.QPointF(end.x(), end.y())
            elif isinstance(start, QtWidgets.QGraphicsItem) and isinstance(end, QtCore.QPointF):
                self.start_point = QtCore.QPointF(start.pos.x(), start.pos.y())
                self.end_point = end
            elif isinstance(start, QtWidgets.QGraphicsItem) and isinstance(end, QtWidgets.QGraphicsItem):
                self.start_point = QtCore.QPointF(start.pos.x(), start.pos.y())
                self.end_point = QtCore.QPointF(end.pos.x(), end.pos.y())
            else:
                print('error in updating line gui 1')
        else:

            if isinstance(self.start, QtCore.QPointF) and isinstance(self.end, QtCore.QPointF):
                self.start_point = self.start
                self.end_point = self.end
            elif isinstance(self.start, QtCore.QPointF) and isinstance(self.end, QtWidgets.QGraphicsItem):
                self.start_point = self.start
                self.end_point = QtCore.QPointF(self.end.x(), self.end.y())
            elif isinstance(self.start, QtWidgets.QGraphicsItem) and isinstance(self.end, QtCore.QPointF):
                self.start_point = QtCore.QPointF(self.start.pos.x(), self.start.pos.y())
                self.end_point = self.end
            elif isinstance(self.start, QtWidgets.QGraphicsItem) and isinstance(self.end, QtWidgets.QGraphicsItem):
                self.start_point = QtCore.QPointF(self.start.pos.x(), self.start.pos.y())
                self.end_point = QtCore.QPointF(self.end.pos.x(), self.end.pos.y())
            else:
                print('error in updating line gui 2')

    def paint(self, painter: QtGui.QPainter, QStyleOptionGraphicsItem, widget=None):
        if self.link_type == ALinkType.PORT:
            self.draw_link_port(painter, self.start_point, self.end_point)
        elif self.link_type == ALinkType.PARAM:
            self.draw_link_param(painter, self.start_point, self.end_point)

    def boundingRect(self):
        if self.start_point and self.end_point:
            start = self.start_point
            end = self.end_point
            ex = max([start.x(), end.x()])
            ey = max([start.y(), end.y()])
            sx = min([start.x(), end.x()])
            sy = min([start.y(), end.y()])
            w = ex - sx
            h = ey - sy
        else:
            sx = sy = w = h = 1

        return QtCore.QRectF(sx, sy, w, h)

    def distance(self, p1: QtCore.QPointF, p2: QtCore.QPointF):
        dist = math.hypot(p2.x() - p1.x(), p2.y() - p1.y())
        return dist

    def draw_link_port(self, painter: QtGui.QPainter, start, end):

        # draw collider
        if self.draw_collider:
            path = QtGui.QPainterPath()
            path.addRect(self.boundingRect().x(), self.boundingRect().y(), self.boundingRect().width(),
                         self.boundingRect().height())
            brush = QtGui.QBrush(QtGui.QColor(100, 250, 100, 100))
            pen = QtGui.QPen()
            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawPath(path)

        path = QtGui.QPainterPath()
        path.moveTo(start.x(), start.y())

        dist_p = end - start

        # dist_y = (end.y() - start.y())
        # p1
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
        # dist = self.distance(start, end) / 4
        # dist = 100 #if dist > 100 else dist
        dist_x = end.x() - start.x()
        dist_y = end.y() - start.y()

        if dist_y > 0:
            path.cubicTo(start.x(), start.y(), start.x(), start.y() + dist_y / 2, mx1, my1)
            path.cubicTo(mx2, my2, end.x(), end.y() - dist_y / 2, end.x(), end.y())
        else:
            dist = dist_y
            if abs(dist_y) > abs(dist_x / 2):
                dist = -abs(dist_x / 2)

            p2_x = start.x()
            p2_y = start.y() - dist / 2

            p3_x = start.x() + dist_x / 4
            p3_y = start.y() - dist / 2

            p4_x = (end.x() + start.x()) / 2
            p4_y = start.y() - dist / 2

            p5_x = (end.x() + start.x()) / 2
            p5_y = start.y()

            p6_x = (end.x() + start.x()) / 2
            p6_y = end.y()

            p7_x = (end.x() + start.x()) / 2
            p7_y = end.y() + dist / 2

            p8_x = end.x() - dist_x / 4
            p8_y = end.y() + dist / 2

            p9_x = end.x()
            p9_y = end.y() + dist / 2

            path.cubicTo(start.x(), start.y(), p2_x, p2_y, p3_x, p3_y)
            path.cubicTo(p3_x, p3_y, p4_x, p4_y, p5_x, p5_y)

            path.lineTo(p6_x, p6_y)

            path.cubicTo(p6_x, p6_y, p7_x, p7_y, p8_x, p8_y)
            path.cubicTo(p8_x, p8_y, p9_x, p9_y, end.x(), end.y())
        # path.cubicTo(start.x(), start.y(), p1_x, p1_y, mx1, my1)
        # path.cubicTo(mx2, my2, end.x(), my2, end.x(), end.y() - d)

        # else:
        #     path.cubicTo(start.x(), start.y(), mx1, start.y(), mx1, my1)
        #     path.cubicTo(mx2, my2, mx2, end.y(), end.x(), end.y())
        color = QtGui.QColor(255, 255, 255, 200)
        pen = QtGui.QPen(color, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)

    def draw_link_param(self, painter: QtGui.QPainter, start, end):
        path = QtGui.QPainterPath()
        path.moveTo(start.x(), start.y())

        dist_p = end - start

        # dist_y = (end.y() - start.y())
        # p1
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
        # dist = self.distance(start, end) / 4
        # dist = 100 #if dist > 100 else dist
        dist_x = end.x() - start.x()
        dist_y = end.y() - start.y()

        if dist_x > 0:
            path.cubicTo(start.x(), start.y(), start.x() + dist_x / 2, start.y(), mx1, my1)
            path.cubicTo(mx2, my2, end.x() - dist_x / 2, end.y(), end.x(), end.y())
        else:
            dist = dist_x
            if abs(dist_x) > abs(dist_y / 2):
                dist = -abs(dist_y / 2)

            p2_x = start.x() - dist / 2
            p2_y = start.y()

            p3_x = start.x() - dist / 2
            p3_y = start.y() + dist_y / 4

            p4_x = start.x() - dist / 2
            p4_y = (end.y() + start.y()) / 2

            p5_x = start.x()
            p5_y = (end.y() + start.y()) / 2

            p6_x = end.x()
            p6_y = (end.y() + start.y()) / 2

            p7_x = end.x() + dist / 2
            p7_y = (end.y() + start.y()) / 2

            p8_x = end.x() + dist / 2
            p8_y = end.y() - dist_y / 4

            p9_x = end.x() + dist / 2
            p9_y = end.y()

            path.cubicTo(start.x(), start.y(), p2_x, p2_y, p3_x, p3_y)
            path.cubicTo(p3_x, p3_y, p4_x, p4_y, p5_x, p5_y)

            path.lineTo(p6_x, p6_y)

            path.cubicTo(p6_x, p6_y, p7_x, p7_y, p8_x, p8_y)
            path.cubicTo(p8_x, p8_y, p9_x, p9_y, end.x(), end.y())
        # path.cubicTo(start.x(), start.y(), p1_x, p1_y, mx1, my1)
        # path.cubicTo(mx2, my2, end.x(), my2, end.x(), end.y() - d)

        # else:
        #     path.cubicTo(start.x(), start.y(), mx1, start.y(), mx1, my1)
        #     path.cubicTo(mx2, my2, mx2, end.y(), end.x(), end.y())
        color = QtGui.QColor(255, 255, 255, 200)
        pen = QtGui.QPen(color, 3, QtCore.Qt.SolidLine, QtCore.Qt.RoundCap)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 0))
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)
