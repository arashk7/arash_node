from PyQt5 import QtWidgets
from AGraphWidget.ASkin import *
from AGraphWidget import APropertyGUI
from AGraphWidget.AUtil import ASharedItems, AMath,APropertyType


class APropertyCombo(APropertyGUI.APropertyGUI):
    def __init__(self, property, property_id, property_location):
        super(APropertyCombo, self).__init__(property, property_id, APropertyType.COMBO, property_location)
        self.property = property
        self.control = QtWidgets.QComboBox()
        self.control.currentTextChanged.connect(self.change_event)
        layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel()
        label.setText(self.property_id)
        label.setStyleSheet('background: gray')
        self.control.setStyleSheet('background: lightgray')
        self.widget = QtWidgets.QWidget()
        self.widget.setStyleSheet('background: gray')
        layout.addWidget(label)
        layout.addWidget(self.control)
        self.widget.setLayout(layout)
        self.widget.setMaximumWidth(self.rect.width())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)

    def init(self):
        self.control_proxy: QtWidgets.QGraphicsProxyWidget = ASharedItems.awidget.scene().addWidget(self.widget)
        self.control_proxy.setParentItem(self)
        self.control_proxy.setZValue(2)

    def change_event(self, value):
        print('change combo: ' + value)
        self.property.value = value

    def add_item(self, item):
        self.control.addItem(item)

    def add_items(self, items):
        for item in items:
            self.add_item(item)
