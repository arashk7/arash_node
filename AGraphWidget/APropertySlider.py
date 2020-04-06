from PyQt5 import QtWidgets
from AGraphWidget.ASkin import *
from AGraphWidget import APropertyGUI
from AGraphWidget.AUtil import ASharedItems, AMath, APropertyType


class APropertySlider(APropertyGUI.APropertyGUI):
    def __init__(self, property, property_id, property_location):
        super(APropertySlider, self).__init__(property, property_id, APropertyType.SLIDER, property_location)
        self.property = property
        self.control = QtWidgets.QSlider()
        self.control.valueChanged.connect(self.change_event)
        self.control.setOrientation(QtCore.Qt.Horizontal)
        layout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel()
        self.label.setText(self.property_id)
        self.label.setStyleSheet('background: gray')
        self.control.setStyleSheet('background: lightgray')
        self.widget = QtWidgets.QWidget()
        self.widget.setStyleSheet('background: gray')
        layout.addWidget(self.label)
        layout.addWidget(self.control)
        self.widget.setLayout(layout)
        self.widget.setMaximumWidth(self.rect.width())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)

    def init(self):
        self.control_proxy: QtWidgets.QGraphicsProxyWidget = ASharedItems.awidget.scene().addWidget(self.widget)
        self.control_proxy.setParentItem(self)
        self.control_proxy.setZValue(1)
        super(APropertySlider, self).init()

    def change_event(self, value):
        print('change value: ' + str(value))
        self.property.value = value
        # self.control.setText(value)
        self.label.setToolTip(str(value))



    def set_value(self, default_value):
        self.control.setValue(default_value)
