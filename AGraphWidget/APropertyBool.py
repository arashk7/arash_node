from PyQt5 import QtWidgets
from AGraphWidget.ASkin import *
from AGraphWidget import APropertyGUI
from AGraphWidget.AUtil import ASharedItems, AMath, APropertyType


class APropertyBool(APropertyGUI.APropertyGUI):
    def __init__(self, property, property_id, property_location):
        super(APropertyBool, self).__init__(property, property_id, APropertyType.BOOL, property_location)
        self.property = property
        self.control = QtWidgets.QCheckBox()
        self.control.stateChanged.connect(self.change_event)
        self.control.setTristate(False)
        layout = QtWidgets.QHBoxLayout()
        label = QtWidgets.QLabel()
        label.setText(self.property_id)
        label.setStyleSheet('background: gray')
        self.control.setStyleSheet('background: gray')
        self.widget = QtWidgets.QWidget()
        self.widget.setStyleSheet('background: gray')
        layout.addWidget(label)
        layout.addWidget(self.control)
        self.widget.setLayout(layout)
        self.widget.setMaximumWidth(self.rect.width())
        self.widget.layout().setContentsMargins(0, 0, 0, 0)

    def init(self):
        super(APropertyBool, self).init()
        self.control_proxy: QtWidgets.QGraphicsProxyWidget = ASharedItems.awidget.scene().addWidget(self.widget)
        self.control_proxy.setParentItem(self)
        self.control_proxy.setZValue(1)

    def change_event(self, value):
        print('change text: ' + str(value))
        self.property.value = value

    def set_state(self, state):
        self.control.setCheckState(state)
