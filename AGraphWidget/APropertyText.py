from PyQt5 import QtWidgets
from AGraphWidget.ASkin import *
from AGraphWidget import APropertyGUI
from AGraphWidget.AUtil import ASharedItems, AMath,APropertyType


class APropertyText(APropertyGUI.APropertyGUI):
    def __init__(self, property, property_id, property_location):
        super(APropertyText, self).__init__(property, property_id, APropertyType.TEXT, property_location)
        self.property = property
        self.control = QtWidgets.QLineEdit()
        self.control.textEdited.connect(self.change_event)
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
        self.control_proxy.setZValue(1)
        super(APropertyText, self).init()

    def change_event(self, value):
        print('change text: ' + value)
        self.property.value = value
        self.control.setText(value)

    def set_text(self, text):
        self.control.setText(text)
