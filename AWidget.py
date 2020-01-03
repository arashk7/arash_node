from PyQt5 import QtCore, QtGui, QtWidgets
import math
from AScene import AScene
from ASkin import *
from ARubberBand import ARubberBand
from APortGUI import APortGUI
from ANodeGUI import ANodeGUI
from AGraphNode import AGraphNode
from AGraph import AGraph

from ALinkGUI import ALinkGUI
from ALinkDrawer import ALinkDrawer


# https://stackoverflow.com/questions/28349676/pyqt4-how-to-correct-qgraphicsitem-position

class AWidget(QtWidgets.QGraphicsView, AGraph):
    # Rubber band signal
    rectChanged = QtCore.pyqtSignal(QtCore.QRect)
    # Mouse Signals
    mouse_press_event = QtCore.pyqtSignal(QtWidgets.QGraphicsView, QtGui.QMouseEvent)
    mouse_move_event = QtCore.pyqtSignal(QtGui.QMouseEvent)
    mouse_release_event = QtCore.pyqtSignal(QtGui.QMouseEvent)

    def __init__(self, parent, graph_id):
        # super(AWidget, self).__init__(parent)
        AGraph.__init__(self, graph_id=graph_id)
        QtWidgets.QGraphicsView.__init__(self, graph_id=graph_id)

        # Default skin has to be loaded here
        # But since this program is under development, we consider to just initialize the skin and save it as default
        ASkin.init_default()

        self.__zoom = 0
        self.__scene = AScene(self)
        self.__scene.setSceneRect(QtCore.QRectF(0, 0, 1768, 874))
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

        # Init RubberBand
        self.__rubber_band = ARubberBand(self)
        # Connect all the mouse event to rubber band
        self.mouse_press_event.connect(self.__rubber_band.mouse_press_event)
        self.mouse_move_event.connect(self.__rubber_band.mouse_move_event)
        self.mouse_release_event.connect(self.__rubber_band.mouse_release_event)

        # Init LinkDrawer
        self.__link_drawer = ALinkDrawer()
        self.__scene.addItem(self.__link_drawer.link)
        # Connect events to LinkDrawer
        self.mouse_press_event.connect(self.__link_drawer.mouse_press_event)
        self.mouse_move_event.connect(self.__link_drawer.mouse_move_event)
        self.mouse_release_event.connect(self.__link_drawer.mouse_release_event)

        # Selected item group
        empty_list = list()
        self.__selected_item_group = self.__scene.createItemGroup(empty_list)
        self.__selected_item_group.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

        # Zooming variables
        self.__zoom = 1

        self.__press_node = None
        self.__press_point = None

        # self.render_sample_rect()
        p = self.__scene.sceneRect().center()

        self.add_node('node_1', p.x(), p.y())
        self.add_node('node_2', p.x(), p.y() + 300)

        self.add_node('node_3', p.x() + 200, p.y())
        self.add_port_in('node_1', 'port1')
        self.add_port_in('node_1', 'port2')
        self.add_port_out('node_1', 'port1')
        self.add_port_in('node_2', 'port1')
        self.add_port_out('node_2', 'port1')
        self.add_link('node_1', 'port1', 'node_2', 'port1')

        for n in self.nodes.values():
            self.__scene.addItem(n.gui)

            for p_in in n.ports_in.values():
                self.__scene.addItem(p_in.gui)
            for p_out in n.ports_out.values():
                self.__scene.addItem(p_out.gui)
        for l in self.links.values():
            self.__scene.addItem(l.gui)

        # Deselect all the Node items
        # [i.setSelected(False) for i in self.__scene.items()]

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
        for l in self.links.values():
            l.gui.update_line(l.start.gui, l.end.gui)

    # This function is called every time the window size changed
    def resizeEvent(self, event: QtGui.QResizeEvent):
        self.updateSceneRect(QtCore.QRectF(0, 0, 2500, 2000))
        super(AWidget, self).resizeEvent(event)

    # The draw function in this app is different from Qt
    # This draw means darw fixed object on scene (Not a rendering).
    def draw_grid(self):
        pen = QtGui.QPen(ASkin.color(ARole.GRID))
        width = self.__scene.sceneRect().width()
        height = self.__scene.sceneRect().height()
        # Draw horizontal lines
        for i in range(0, int(width + 0), 20):
            if i % 100 == 0:
                pen.setWidth(2)
            else:
                pen.setWidth(1)
            line = self.__scene.addLine(i, 0, i, height + 00, pen)
            line.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
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
            line.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
            line.setZValue(-1)
            line.setData(0, 'grid')
            line.setActive(False)

    def distance(self, p1: QtCore.QPointF, p2: QtCore.QPointF):
        dist = math.hypot(p2.x() - p1.x(), p2.y() - p1.y())
        return dist

    # Mouse Press Event
    def mousePressEvent(self, event: QtGui.QMouseEvent):
        super(AWidget, self).mousePressEvent(event)
        self.mouse_press_event.emit(self, event)

        if event.button() == QtCore.Qt.LeftButton:
            self.__press_node = self.itemAt(event.pos())
            self.__press_point = self.mapToScene(QtCore.QPoint(event.x(), event.y()))
            if self.__press_node and self.__press_node.data(0) == 'port':
                # print('port')
                self.__link_drawer.link.show()

            # p = self.mapToScene(QtCore.QPoint(event.x(), event.y()))
            # print(str(p.x()) + " " + str(p.y()))

    def mouseReleaseEvent(self, event: QtGui.QMouseEvent):
        super(AWidget, self).mouseReleaseEvent(event)
        self.mouse_release_event.emit(event)

        if event.button() == QtCore.Qt.LeftButton:

            release_node = self.itemAt(event.pos())
            release_point = self.mapToScene(QtCore.QPoint(event.x(), event.y()))

            # If the mouse pressed on grid or any other items means all the Nodes have to be deselected
            if not self.__press_node or self.__press_node.data(0) == 'grid':
                if not release_node or release_node.data(0) == 'grid':
                    # Deselect all the Node items
                    [i.setSelected(False) for i in self.__scene.items()]
                    [i.update() for i in self.__scene.items()]

            # If mouse button pressed on a node and release at the same place means the node has to be selected
            if self.__press_node and self.__press_node.data(0) == 'node':
                if release_node and release_node.data(0) == 'node':
                    if self.__press_node == release_node:
                        if self.distance(release_point, self.__press_point) < 2:
                            # Deselect all the Node items
                            [i.setSelected(False) for i in self.__scene.items()]
                            [i.update() for i in self.__scene.items()]
                            release_node.setSelected(True)
                            release_node.update()
                            return

            # RubberBand
            rubber_rect = self.__rubber_band.get_rect()
            if rubber_rect.width() > 10:
                rect = self.mapToScene(rubber_rect)
                items = self.__scene.items(rect)
                for i in items:
                    if i.data(0) == 'node':
                        i.setSelected(True)
                        i.update()

                return

    def mouseMoveEvent(self, event: QtGui.QMouseEvent):
        super(AWidget, self).mouseMoveEvent(event)
        self.mouse_move_event.emit(event)

    # Zooming V0.1
    def fit_in_view(self, scale=True):
        rect = self.sceneRect()

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
