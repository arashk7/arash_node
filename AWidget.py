from PyQt5 import QtCore, QtGui, QtWidgets
from AScene import AScene

groups = ['Disabled', 'Active', 'Inactive', 'Normal']
roles = [
            'AlternateBase',
            'Background',
            'Base',
            'Button',
            'ButtonText',
            'BrightText',
            'Dark',
            'Foreground',
            'Highlight',
            'HighlightedText',
            'Light',
            'Link',
            'LinkVisited',
            'Mid',
            'Midlight',
            'Shadow',
            'ToolTipBase',
            'ToolTipText',
            'Text',
            'Window',
            'WindowText'
        ]

class AWidget(QtWidgets.QGraphicsView):
    def __init__(self, parent):
        super(AWidget, self).__init__(parent)
        self.__zoom = 0
        self.__scene = AScene(self)
        self.setScene(self.__scene)

        palette = QtGui.QPalette()
        palette.Background = QtGui.QColor(100, 100, 100)
        role = getattr(QtGui.QPalette, roles[0])
        group = getattr(QtGui.QPalette, groups[0])
        palette.setColor(group,role,QtGui.QColor(100, 100, 100))

        role = getattr(QtGui.QPalette, roles[0])
        group = getattr(QtGui.QPalette, groups[0])
        palette.color(group, role)

        # Setting up all the parameters regards QGraphicsView
        self.setTransformationAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setResizeAnchor(QtWidgets.QGraphicsView.AnchorUnderMouse)
        self.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.setBackgroundBrush(QtGui.QBrush(palette.color(group, role)))
        self.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.setDragMode(True)
        self.viewport().setCursor(QtCore.Qt.ArrowCursor)

        # self.renderGrid()

    def drawForeground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        super(AWidget, self).drawForeground(painter, rect)

    def resizeEvent(self, event: QtGui.QResizeEvent):
        self.renderGrid()
    def renderGrid(self):
        pen = QtGui.QPen(QtGui.QColor(60,60,60))

        for i in range(-40, int(self.size().width()+40), 20):
            if i % 100 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            line = self.__scene.addLine(i, -40, i, self.size().height()+40, pen)
            line.setActive(False)
            line.setZValue(-1)
            line.setData(0, 'grid')
        for i in range(-40, int(self.size().height()+40), 20):
            if i % 100 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            line = self.__scene.addLine(-40, i, self.size().width()+40, i, pen)
            line.setActive(False)
            line.setZValue(-1)
            line.setData(0, 'grid')
