from PyQt5 import QtCore, QtGui, QtWidgets
from ArashWidget.ALinkGUI import ALinkGUI
from ArashWidget.AGraphPort import AGraphPort
from ArashWidget.AGraphLink import AGraphLink
from ArashWidget.AUtil import APortType, AMath, ACache


class ALinkDrawer:

    def __init__(self, widget):
        self.link = ALinkGUI('link_drawer')
        # self.link.update_line(start=QtCore.QPointF(1000, 1000), end=QtCore.QPointF(1100, 1100))
        widget.get_scene().addItem(self.link)
        # self.link = AGraphLink('link_drawer',)
        self.widget = widget

        self.link.show()
        self.press_port = None
        self.end_port = None
        self.is_drag = False

    def mouse_press_event(self, widget: QtWidgets.QGraphicsView, event: QtGui.QMouseEvent):
        # self.widget = widget
        if event.button() == QtCore.Qt.LeftButton:
            self.press_port = widget.itemAt(event.pos())
            if self.press_port:
                if self.press_port.data(0) == 'port':
                    if self.press_port.port_type == APortType.OUTPUT:
                        print('1')
                        self.press_port.parentItem().setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
                        # pos = widget.mapToScene(QtCore.QPoint(self.press_node.x, self.press_node.y))
                        pos = QtCore.QPointF(self.press_port.pos.x(), self.press_port.pos.y())
                        widget.get_scene().removeItem(self.link)
                        del self.link
                        self.link = ALinkGUI('link_drawer',start=pos,end = pos)
                        widget.get_scene().addItem(self.link)
                        # self.link.show()
                        # self.link.start_point = pos
                        self.is_drag = True
                else:
                    self.press_port.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)

    def mouse_move_event(self, event: QtGui.QMouseEvent):
        # if event.button() == QtCore.Qt.LeftButton:

        if self.is_drag:
            pos = self.widget.mapToScene(event.pos())
            # print(str(pos.x()))
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

                self.link.update_line(self.link.start_point,self.link.end_point)

    def mouse_release_event(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            if self.is_drag:
                if self.end_port:
                    print(self.end_port.port_id)
                    link = self.widget.add_link(self.press_port.node_id, self.press_port.port_id,
                                                self.end_port.node_id, self.end_port.port_id)
                    self.widget.add_to_scene(link.gui)

                self.link.hide()
                self.is_drag = False
