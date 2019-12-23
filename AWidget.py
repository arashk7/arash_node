from PyQt5 import QtCore, QtGui, QtWidgets
from AScene import AScene
from ASkin import *


# https://stackoverflow.com/questions/28349676/pyqt4-how-to-correct-qgraphicsitem-position

class AWidget(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(AWidget, self).__init__(parent)

        # Default skin has to be loaded here
        # But since this program is under development, we consider to just initialize the skin and save it as default
        ASkin.init_default()

        self.__zoom = 0
        self.__scene = AScene(self)
        self.__scene.setSceneRect(QtCore.QRectF(0, 0, 2500, 2000))

        self.setScene(self.__scene)

        # Setting up all the parameters regards QGraphicsView
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setBackgroundBrush(QtGui.QBrush(ASkin.color(ARole.BACKGROUND)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setDragMode(True)
        self.viewport().setCursor(QtCore.Qt.ArrowCursor)

        # Zooming variables
        self.__zoom=1
        self.__num_scheduled_scalings=0
        self.factor =1

        brush = QtGui.QBrush(QtGui.QColor(200, 50, 50))
        pen = QtGui.QPen()
        # sample rectangle
        p = self.__scene.sceneRect().center()
        rect = QtCore.QRectF(p.x(), p.y(), 100, 100)
        r = self.__scene.addRect(rect, pen, brush)

    # Zoom property
    # (this property is provided for the time that it is needed to access from th outside of the class)
    @property
    def zoom(self):
        return self.__zoom

    @zoom.setter
    def zoom(self, zoom):
        self.__zoom = zoom

    def drawForeground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        super(AWidget, self).drawForeground(painter, rect)

    def resizeEvent(self, event: QtGui.QResizeEvent):
        self.updateSceneRect(QtCore.QRectF(0, 0, 2500, 2000))
        self.render_grid()

    def render_grid(self):

        pen = QtGui.QPen(ASkin.color(ARole.GRID))
        width = 2500
        height = 2000
        # Draw horizontal lines
        for i in range(0, int(width + 0), 20):
            if i % 100 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            line = self.__scene.addLine(i, 0, i, height + 00, pen)
            line.setZValue(-1)
            line.setData(0, 'grid')
            line.setActive(False)

        # Draw vertical lines
        for i in range(0, int(height + 00), 20):
            if i % 100 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            line = self.__scene.addLine(0, i, width + 0, i, pen)
            line.setZValue(-1)
            line.setData(0, 'grid')
            line.setActive(False)

    # incomplete zooming
    def fitInView(self, scale=True):
        rect = QtCore.QRectF(self.rect())

        self.setSceneRect(rect)

        unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
        self.scale(1 / unity.width(), 1 / unity.height())
        viewrect = self.viewport().rect()
        scenerect = self.transform().mapRect(rect)
        factor = min(viewrect.width() / scenerect.width(),
                     viewrect.height() / scenerect.height())
        self.scale(factor, factor)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.factor = 1.0025
            self.__zoom += 1

        else:
            self.factor = 0.008
            self.__zoom -= 1

        if self.__zoom > 0:
            anim = QtCore.QTimeLine(300, self)
            anim.setUpdateInterval(5)
            anim.valueChanged.connect(self.anim_scale)
            anim.start()

        elif self.__zoom == 0:
            self.fitInView()
        else:
            self.__zoom = 0
    def anim_scale(self):
        # factor = 1.0 + float(self.__num_scheduled_scalings) / 300.0
        self.scale(self.factor, self.factor)

    def wheelEvent1(self, event:QtGui.QWheelEvent):

        num_degrees = event.angleDelta().y() / 8
        num_steps = num_degrees / 15  # see QWheelEvent documentation
        self.__num_scheduled_scalings += num_steps
        # if user moved the wheel in another direction, we reset previously scheduled scaling
        if self.__num_scheduled_scalings * num_steps < 0:
            self.__num_scheduled_scalings = num_steps

        anim = QtCore.QTimeLine(300, self)
        anim.setUpdateInterval(5)
        anim.valueChanged.connect(self.zoom_scaling_time)
        anim.start()

    def zoom_scaling_time(self, value):
        factor = 1.0 + float(self.__num_scheduled_scalings) / 300.0
        self.scale(factor, factor)

    def zoom_anim_finished(self):
        if self.__num_scheduled_scalings > 0:
            self.__num_scheduled_scalings -= 1
        else:
            self.__num_scheduled_scalings += 1
        self.sender().destroy()
