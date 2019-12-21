from PyQt5 import QtCore, QtGui, QtWidgets
from AScene import AScene
from ASkin import *

class AWidget(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(AWidget, self).__init__(parent)

        # Default skin has to be loaded here
        ASkin.init_default()

        self.__zoom = 0
        self.__scene = AScene(self)
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

        # self.renderGrid()

    def drawForeground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        super(AWidget, self).drawForeground(painter, rect)

    def resizeEvent(self, event: QtGui.QResizeEvent):
        self.render_grid()

    def render_grid(self):

        pen = QtGui.QPen(ASkin.color(ARole.GRID))

        # Draw horizontal lines
        for i in range(-40, int(self.size().width() + 40), 20):
            if i % 100 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            line = self.__scene.addLine(i, -40, i, self.size().height() + 40, pen)
            line.setActive(False)
            line.setZValue(-1)
            line.setData(0, 'grid')

        # Draw vertical lines
        for i in range(-40, int(self.size().height() + 40), 20):
            if i % 100 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            line = self.__scene.addLine(-40, i, self.size().width() + 40, i, pen)
            line.setActive(False)
            line.setZValue(-1)
            line.setData(0, 'grid')
