from PyQt5 import QtCore, QtGui, QtWidgets
from AGraphWidget.AGraphPort import AGraphPort
from AGraphWidget.ASkin import *


class ANodeGUI(QtWidgets.QGraphicsItem):
    def __init__(self, graph_node, x=100, y=100):
        super(ANodeGUI, self).__init__()
        self.pos = QtCore.QPointF(0, 0)
        self.id = graph_node.node_id
        self.caption = graph_node.node_id
        self.rect = QtCore.QRectF(x, y, 150, 50)
        self.setData(0, 'node')
        self.__selected = False
        self.graph_node = graph_node
        self.node_info = ''

        # Shadow Effect
        shadow = QtWidgets.QGraphicsDropShadowEffect()
        shadow.setBlurRadius(20)
        shadow.setOffset(5)
        self.setGraphicsEffect(shadow)

        # Node Setting
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable)
        self.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable)

        self.setZValue(1)
        self.__group = AGroup.NORMAL



        #     port.gui.x = 1000 #+ self.rect.x()
        # port.gui.y = 0 #self.rect.y()
        # i += 1
        # port.gui.update()
        # for i in range(1, len(graph_node.ports_in) + 1):
        #     port = AGraphPort()
        #     anchor = AAnchor(scene=scene, parent=self, x=self.rect.x() + (step * i) - 3.5, y=self.rect.y() - 6,
        #                      anchorType=AnchorType.INPUT)
        #     self.inputAnchors.append(anchor)
        #
        # step = self.rect.width() / (len(self.nn_params_out) + 1)
        # for i in range(1, len(self.nn_params_out) + 1):
        #     anchor = AAnchor(scene=scene, parent=self, x=self.rect.x() + (step * i) - 3.5, y=y + self.rect.height() - 2,
        #                      anchorType=AnchorType.OUTPUT)  # (len(node.properties_in) * anchorSize)
        #     self.outputAnchors.append(anchor)

    def init_ports_locations(self):
        step = self.rect.width() / (len(self.graph_node.ports_in) + 1)
        i = 1
        # graph_node.ports_in[0]
        for port in self.graph_node.ports_in.values():
            port.gui.x = ((step * i) + self.rect.x() - 10)
            port.gui.y = (self.rect.y() - 15)
            i += 1

        step = self.rect.width() / (len(self.graph_node.ports_out) + 1)
        i = 1
        for port in self.graph_node.ports_out.values():
            port.gui.x = ((step * i) + self.rect.x() - 10)
            port.gui.y = (self.rect.y() + self.rect.height() - 5)
            i += 1

    def init_params_props_locations(self):
        # init_step = 10
        step = 30

        prop_step = 0
        num_prop = 0
        init_step = self.rect.y() + step
        for prop in self.graph_node.props.values():
            num_prop += 1
            prop.gui.x = (self.rect.x())
            prop.gui.y = init_step
            init_step += prop.gui.property_height
            # prop.gui.y = init_step + ((step * num_prop) + self.rect.y() - 10)

            prop_step += prop.gui.property_height
            prop.gui.init()

        init_step -= step
        copy_init_step = init_step
        num_in_param = 1
        for param in self.graph_node.params_in.values():
            param.gui.x = (self.rect.x() - 15)
            copy_init_step += step
            param.gui.y = copy_init_step
            num_in_param += 1

        num_out_param = 1
        for param in self.graph_node.params_out.values():
            param.gui.x = (self.rect.x() + self.rect.width() - 5)
            init_step += step
            param.gui.y = init_step
            num_out_param += 1

        if num_out_param > num_in_param:
            self.rect.setHeight(50 + (step / 2) * (num_out_param - 1) + prop_step)
        else:
            self.rect.setHeight(50 + (step / 2) * (num_in_param - 1) + prop_step)

    def setSelected(self, selected):
        self.__selected = selected
        super(ANodeGUI, self).setSelected(selected)

    def isSelected(self):
        return self.__selected

    def boundingRect(self):

        # You will be able to edit this rectangle which affect your physical interaction with mouse
        rect = QtCore.QRectF(self.rect)
        p = self.scenePos() + self.rect.center()
        self.pos.setX(p.x())
        self.pos.setY(p.y())
        return rect

    def paint(self, painter: QtGui.QPainter, option: QtWidgets.QStyleOptionGraphicsItem, widget=None):
        x = self.rect.x()
        y = self.rect.y()
        w = self.rect.width()
        h = self.rect.height()
        # Highlighting rounded rectangle
        if self.__selected:
            path = QtGui.QPainterPath()
            path.addRoundedRect(x - 2.5, y - 2.5, w + 5, h + 5, 5, 5)
            brush = QtGui.QBrush(ASkin.color(ARole.SELECT_HIGHLIGHT))
            pen = QtGui.QPen()
            painter.setPen(pen)
            painter.setBrush(brush)
            painter.drawPath(path)

        # Main rounded rect
        path = QtGui.QPainterPath()
        path.addRoundedRect(x, y, w, h, 10, 10)
        brush = QtGui.QBrush(ASkin.color(ARole.NODE_WND, self.__group))
        pen = QtGui.QPen()
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)

        # add caption bar
        path = QtGui.QPainterPath()
        color = QtGui.QColor(20, 20, 20, 250)
        brush = QtGui.QBrush(color)
        pen = QtGui.QPen(color)
        pen.setWidth(0)
        path.moveTo(x, y + 20)
        path.lineTo(x, y + 10)
        path.cubicTo(x, y + 10, x, y, x + 10, y)
        path.lineTo(x + w - 10, y)
        path.cubicTo(x + w - 10, y, x + w, y, x + w, y + 10)
        path.lineTo(x + w, y + 20)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)

        # add caption text
        path = QtGui.QPainterPath()
        color = ASkin.color(ARole.NODE_WND_CAP_TEXT)
        brush = QtGui.QBrush(color)
        pen = QtGui.QPen(color)
        pen.setWidth(0)
        font = QtGui.QFont("arial", 7)

        # br = QtGui.QFontMetrics(font).boundingRect(self.caption)
        # print(str(br.width()))
        self.caption = self.graph_node.node_id
        self.id = self.graph_node.node_id
        path.addText(x + 5, y + 15, font, str(self.caption))
        painter.setFont(font)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)

        # add node_info text
        path = QtGui.QPainterPath()
        color = ASkin.color(ARole.NODE_WND_CAP_TEXT)
        brush = QtGui.QBrush(color)
        pen = QtGui.QPen(color)
        pen.setWidth(0)
        font = QtGui.QFont("arial", 6)

        path.addText(x + 5, y + h - 10, font, str(self.node_info))
        painter.setFont(font)
        painter.setPen(pen)
        painter.setBrush(brush)
        painter.drawPath(path)
