from PyQt5 import QtWidgets
from PyQt5 import QtCore, QtGui

from AGraphWidget.ASkin import *
from AGraphWidget import APropertyGUI
from AGraphWidget.AUtil import ASharedItems, AMath, APropertyType


class APropertyImage(APropertyGUI.APropertyGUI):
    def __init__(self, property, property_id, property_location):
        super(APropertyImage, self).__init__(property, property_id, APropertyType.IMAGE, property_location)
        self.property = property
        self.property_height = 120
        self.control = QtWidgets.QLabel()
        self.control.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.control.setAlignment(QtCore.Qt.AlignCenter)
        # self.control.setMinimumHeight(self.property_height - 10)

        # self.control.setFixedSize(,90)
        # self.control.c.connect(self.change_event)
        # self.control.setTristate(False)
        layout = QtWidgets.QHBoxLayout()
        # label = QtWidgets.QLabel()
        # label.setText(self.property_id)
        # label.setStyleSheet('background: gray')
        self.control.setStyleSheet('background: white')
        self.widget = QtWidgets.QWidget()
        self.widget.setStyleSheet('background: gray')
        # layout.addWidget(label)
        layout.addWidget(self.control)
        self.widget.setLayout(layout)

        # self.widget.setMaximumHeight(self.property_height)
        # self.widget.setMaximumWidth(self.rect.width())
        self.widget.layout().setContentsMargins(5, 5, 5, 5)

        self.image = None
        self.first_image = False
        self.image = None

    def init(self):
        self.control_proxy: QtWidgets.QGraphicsProxyWidget = ASharedItems.awidget.scene().addWidget(self.widget)
        self.control_proxy.setParentItem(self)
        self.control_proxy.setZValue(1)

        self.control.setMinimumHeight(self.property_height - 10)
        self.widget.setMaximumHeight(self.property_height)
        self.widget.setMaximumWidth(self.rect.width())
        super(APropertyImage, self).init()

    # def paint(self, painter: QtGui.QPainter, style: QtWidgets.QStyleOptionGraphicsItem, widget=None):
    #     x = self.x  # .__rect.x()
    #     y = self.y  # __rect.y()
    #     w = self.rect.width()
    #     h = self.rect.height()
    #     painter.drawPixmap()
    def boundingRect(self):
        rect = super(APropertyImage, self).boundingRect()
        p = QtCore.QPointF(rect.x() + 5, rect.y() + 5)
        if self.first_image:
            # w = (self.rect.width() - self.control.width()) / 2
            # h = (self.rect.height() - self.control.height()) / 2
            self.image.setPos(p.x(), p.y())
            self.first_image = False

        return rect

    def set_pixmap(self, pixmap):

        # image = pixmap.scaledToHeight(self.property_height-10)
        # self.image = pixmap.scaledToWidth(self.rect.width()-10)
        # self.control.setStyleSheet('background: gray')
        # self.control.setPixmap(pixmap)
        if self.image:
            ASharedItems.awidget.get_scene().removeItem(self.image)
            del self.image

        self.image = QtWidgets.QGraphicsPixmapItem(pixmap)
        self.image.setZValue(2)

        # item.setPos(self.control.pos())
        self.image.setParentItem(self)
        self.first_image = True

        if pixmap.width() > pixmap.height():
            self.image.setScale(self.control.width() / pixmap.width())
        else:
            self.image.setScale((self.control.height()) / pixmap.height())

        self.image.setFlag(QtWidgets.QGraphicsItem.ItemIsMovable, False)
        self.image.setFlag(QtWidgets.QGraphicsItem.ItemIsSelectable, False)
        # self.property_height = self.image.sceneBoundingRect().height() + 10

        # print(self.property_height)
        # self.property.node.gui.init_params_props_locations()
        # self.property.node.gui.init_ports_locations()

        # else:
        #     self.image.setScale((self.control.height()) / pixmap.height())
        # ASharedItems.awidget.scene().addItem(item)

    def set_image_file(self, file_path):
        pix = QtGui.QPixmap(file_path)

        self.set_pixmap(pix)
