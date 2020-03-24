from PyQt5 import QtCore, QtGui, QtWidgets
from AGraphWidget.ALinkGUI import ALinkGUI

from AGraphWidget.AUtil import APortType, AParamType, AMath, ACache


class ALinkDrawer:
    def __init__(self, widget):
        self.link = ALinkGUI('link_drawer')
        # self.link.update_line(start=QtCore.QPointF(1000, 1000), end=QtCore.QPointF(1100, 1100))
        widget.get_scene().addItem(self.link)
        # self.link = AGraphLink('link_drawer',)
        self.widget = widget

        self.link.show()
        self.press_port_param = None
        self.end_port_param = None
        self.is_drag_port = False
        self.is_drag_param = False
        self.key = None

    def mouse_press_event(self, widget: QtWidgets.QGraphicsView, event: QtGui.QMouseEvent):
        if self.key == QtCore.Qt.Key_Alt:
            return
        # self.widget = widget
        if event.button() == QtCore.Qt.LeftButton:
            self.press_port_param = widget.itemAt(event.pos())
            if self.press_port_param:
                if self.press_port_param.data(0) == 'port':
                    if self.press_port_param.port_type == APortType.OUTPUT:
                        self.press_port_param.parentItem().setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
                        # pos = widget.mapToScene(QtCore.QPoint(self.press_node.x, self.press_node.y))
                        pos = QtCore.QPointF(self.press_port_param.pos.x(), self.press_port_param.pos.y())
                        widget.get_scene().removeItem(self.link)
                        del self.link
                        self.link = ALinkGUI('link_drawer', start=pos, end=pos)
                        widget.get_scene().addItem(self.link)
                        # self.link.show()
                        # self.link.start_point = pos
                        self.is_drag_port = True
                        self.end_port_param = None

                elif self.press_port_param.data(0) == 'param':
                    if self.press_port_param.param_type == AParamType.OUTPUT:
                        self.press_port_param.parentItem().setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)

                        pos = QtCore.QPointF(self.press_port_param.pos.x(), self.press_port_param.pos.y())
                        widget.get_scene().removeItem(self.link)
                        del self.link
                        self.link = ALinkGUI('link_drawer', start=pos, end=pos)
                        widget.get_scene().addItem(self.link)
                        self.is_drag_param = True
                        self.end_port_param = None
                else:
                    self.press_port_param.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

    def mouse_move_event(self, event: QtGui.QMouseEvent):
        # if event.button() == QtCore.Qt.LeftButton:

        if self.is_drag_port:
            pos = self.widget.mapToScene(event.pos())
            mind = 100
            closest_port = None

            for p in ACache.input_ports_gui.values():
                if p.parentItem() is not self.press_port_param.parentItem():
                    p.highlight = True
                    d = AMath.distance(pos, p.pos)
                    if d < mind:
                        mind = d
                        closest_port = p
            if closest_port:
                if mind < 50:
                    self.link.end_point = closest_port.pos
                    self.end_port_param = closest_port
                else:
                    self.link.end_point = pos
                    self.end_port_param = None
            else:
                self.link.end_point = pos
                self.end_port_param = None

                self.link.update_line(self.link.start_point, self.link.end_point)

    def mouse_release_event(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            if self.is_drag_port:
                if self.end_port_param:
                    link = self.widget.add_link(self.press_port_param.node_id, self.press_port_param.port_id,
                                                self.end_port_param.node_id, self.end_port_param.port_id)
                    self.widget.add_to_scene(link.gui)

                self.link.hide()
                self.is_drag_port = False

                for p in ACache.input_ports_gui.values():
                    p.highlight = False

    def key_press_event(self, event):
        self.key = event.key()

    def key_release_event(self, event):
        self.key = None
