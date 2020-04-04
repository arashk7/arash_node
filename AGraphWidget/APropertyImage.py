from PyQt5 import QtWidgets
from AGraphWidget.ASkin import *
from AGraphWidget import APropertyGUI
from AGraphWidget.AUtil import ASharedItems, AMath, APropertyType


class APropertyImage(APropertyGUI.APropertyGUI):
    def __init__(self, property, property_id, property_location):
        super(APropertyImage, self).__init__(property, property_id, APropertyType.IMAGE, property_location)
        self.property = property
        self.property_height = 90
        self.control = QtWidgets.QLabel()
        self.control.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.control.setAlignment(QtCore.Qt.AlignCenter)
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

        self.widget.setMaximumWidth(self.rect.width())
        self.widget.layout().setContentsMargins(5, 5, 5, 5)

    def init(self):
        self.control_proxy: QtWidgets.QGraphicsProxyWidget = ASharedItems.awidget.scene().addWidget(self.widget)
        self.control_proxy.setParentItem(self)
        self.control_proxy.setZValue(1)

    def set_image(self, image):
        self.control.setPixmap(image)
