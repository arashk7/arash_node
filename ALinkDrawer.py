from PyQt5 import QtCore, QtGui, QtWidgets
from ALinkGUI import ALinkGUI
from AGraphPort import AGraphPort
from AUtil import APortType, AMath, ACache


class ALinkDrawer:
    def __init__(self):
        self.link = ALinkGUI('link_drawer', QtCore.QPoint(0, 0), QtCore.QPoint(1, 1))
        self.widget = None
        self.link.hide()
        self.press_port = None
        self.end_port = None

    def mouse_press_event(self, widget: QtWidgets.QGraphicsView, event: QtGui.QMouseEvent):
        self.widget = widget
        if event.button() == QtCore.Qt.LeftButton:
            self.press_port = widget.itemAt(event.pos())
            if self.press_port:
                if self.press_port.data(0) == 'port':
                    if self.press_port.port_type == APortType.OUTPUT:

                        # pos = widget.mapToScene(QtCore.QPoint(self.press_node.x, self.press_node.y))
                        pos = QtCore.QPoint(self.press_port.pos.x(), self.press_port.pos.y())
                        self.link.show()
                        self.link.start_point = pos

    def mouse_move_event(self, event: QtGui.QMouseEvent):
        if self.link.isVisible():
            pos = self.widget.mapToScene(QtCore.QPoint(event.x(), event.y()))
            mind = 100
            closest_port = None
            for p in ACache.input_ports_gui.values():
                if p.parentItem() is not self.press_port.parentItem():
                    d = AMath.distance(pos, p.pos)
                    if d < mind:
                        mind = d
                        closest_port = p
            if closest_port:
                if mind < 50:
                    self.link.end_point = closest_port.pos
                    self.end_port = closest_port
                else:
                    self.link.end_point = pos
                    self.end_port = None
            else:
                self.link.end_point = pos
                self.end_port = None

    def mouse_release_event(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            if self.link.isVisible():
                if self.end_port:
                    print(self.end_port.port_id)
                    link = self.widget.add_link(self.press_port.node_id, self.press_port.port_id,
                                         self.end_port.node_id, self.end_port.port_id)
                    self.widget.add_to_scene(link.gui)

            self.link.hide()
