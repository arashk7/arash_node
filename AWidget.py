from PyQt5 import QtCore, QtGui, QtWidgets
from AScene import AScene
from ASkin import *
from ARubberBand import ARubberBand
from ANode import ANode


# https://stackoverflow.com/questions/28349676/pyqt4-how-to-correct-qgraphicsitem-position

class AWidget(QtWidgets.QGraphicsView):
    # Rubber band signal
    rectChanged = QtCore.pyqtSignal(QtCore.QRect)
    # Mouse Signals
    mouse_press_event = QtCore.pyqtSignal(QtWidgets.QGraphicsView, QtGui.QMouseEvent)
    mouse_move_event = QtCore.pyqtSignal(QtGui.QMouseEvent)
    mouse_release_event = QtCore.pyqtSignal(QtGui.QMouseEvent)

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
        self.setDragMode(False)
        self.viewport().setCursor(QtCore.Qt.ArrowCursor)

        # Active AntiAliasing
        self.setRenderHint(QtGui.QPainter.Antialiasing, True)
        # shadow
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(5)
        self.setGraphicsEffect(shadow)

        # Init RubberBand
        self.__rubber_band = ARubberBand(self, ASkin.color(ARole.RUBBER_BAND))
        # Connect all the mouse event to rubber band
        self.mouse_press_event.connect(self.__rubber_band.mouse_press_event)
        self.mouse_move_event.connect(self.__rubber_band.mouse_move_event)
        self.mouse_release_event.connect(self.__rubber_band.mouse_release_event)

        # Selected item group
        empty_list = list()
        self.__selected_item_group = self.__scene.createItemGroup(empty_list)
        self.__selected_item_group.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

        # Zooming variables
        self.__zoom = 1


        # self.render_sample_rect()
        p = self.__scene.sceneRect().center()
        node = ANode(QtCore.QRectF(p.x(), p.y(), 100, 100))
        self.__scene.addItem(node)

        # Draw grid
        self.draw_grid()

    # Zoom property
    # (this property is provided for the time that it is needed to access from th outside of the class)
    # @property
    # def zoom(self):
    #     return self.__zoom
    #
    # @zoom.setter
    # def zoom(self, zoom):
    #     self.__zoom = zoom

    def drawForeground(self, painter: QtGui.QPainter, rect: QtCore.QRectF):
        super(AWidget, self).drawForeground(painter, rect)

    # This function is called every time the window size changed
    def resizeEvent(self, event: QtGui.QResizeEvent):
        self.updateSceneRect(QtCore.QRectF(0, 0, 2500, 2000))
        super(AWidget, self).resizeEvent(event)
    # The draw function in this app is different from Qt
    # This draw means darw fixed object on scene (Not a rendering).
    def draw_grid(self):
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

    # Mouse Press Event
    def mousePressEvent(self, event: QtGui.QMouseEvent):
        super(AWidget, self).mousePressEvent(event)
        self.mouse_press_event.emit(self,event)

        if event.button() == QtCore.Qt.LeftButton:
            p = self.mapToScene(QtCore.QPoint(event.x(), event.y()))
            print(str(p.x()) + " " + str(p.y()))

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        super(AWidget, self).mouseReleaseEvent(event)
        self.mouse_release_event.emit(event)

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        super(AWidget, self).mouseMoveEvent(event)
        self.mouse_move_event.emit(event)

    # Zooming V0.1
    def fit_in_view(self, scale=True):
        rect = QtCore.QRectF(0, 0, 2500, 2000)

        # self.updateSceneRect(QtCore.QRectF(0, 0, 2500, 2000))
        self.setSceneRect(rect)

        unity = self.transform().mapRect(QtCore.QRectF(0, 0, 1, 1))
        self.scale(1 / unity.width(), 1 / unity.height())
        viewrect = self.viewport().rect()
        scenerect = self.transform().mapRect(rect)
        factor = min(viewrect.width() / scenerect.width(),
                     viewrect.height() / scenerect.height())
        self.scale(factor, factor)

    ###### This is the basic version of zooming ####
    # Uing animation is recommended for smooth zooming
    # Search for Qt smooth zooming
    # Here is an example:
    #         if self.__zoom > 0:
    #             self.scale(self.factor, self.factor)
    #             anim = QtCore.QTimeLine(200, self)
    #             anim.setUpdateInterval(10)
    #             anim.set
    #             anim.valueChanged.connect(self.anim_scale)
    #             anim.start()

    #     def anim_scale(self):
    #         factor = 1.0 + float(self.factor) / 300.0
    #         self.scale(factor, factor)
    ################################################
    def wheelEvent(self, event):
        factor = 1
        if event.angleDelta().y() > 0:
            factor = 1.15
            self.__zoom += 1

        else:
            factor = 0.90
            self.__zoom -= 1

        if self.__zoom > 0:
            self.scale(factor, factor)
        elif self.__zoom == 0:
            self.fit_in_view()
        else:
            self.__zoom = 0

    def render_sample_rect(self):
        # sample rectangle
        brush = QtGui.QBrush(QtGui.QColor(200, 50, 50))
        pen = QtGui.QPen()

        p = self.__scene.sceneRect().center()
        rect = QtCore.QRectF(p.x(), p.y(), 100, 100)
        r = self.__scene.addRect(rect, pen, brush)
