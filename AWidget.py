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

        # self.renderGrid()

    def drawForeground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        super(AWidget, self).drawForeground(painter, rect)

    def resizeEvent(self, event:QtGui.QResizeEvent):
        self.updateSceneRect(QtCore.QRectF(0, 0, 2500, 2000))
        self.render_grid()


    def render_grid(self):

        pen = QtGui.QPen(ASkin.color(ARole.GRID))
        width = 2500
        height = 2000
        # Draw horizontal lines
        for i in range(0, int( width + 0), 20):
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

        brush = QtGui.QBrush(QtGui.QColor(200, 50, 50))
        pen = QtGui.QPen()

        # sample rectangle
        p = self.__scene.sceneRect().center()
        rect = QtCore.QRectF(p.x(), p.y(), 100, 100)
        r = self.__scene.addRect(rect, pen, brush)

