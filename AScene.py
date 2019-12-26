from PyQt5 import QtCore, QtGui, QtWidgets


class AScene(QtWidgets.QGraphicsScene):
    def __init__(self, parent):
        super(AScene, self).__init__(parent)


    def drawForeground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        self.update()
        super(AScene, self).drawForeground(painter,rect)

