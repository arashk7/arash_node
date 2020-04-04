from PyQt5 import QtWidgets
from AGraphWidget.ASkin import *
from AGraphWidget import APropertyGUI
from AGraphWidget.AUtil import ASharedItems, AMath, APropertyType


class APropertyFile(APropertyGUI.APropertyGUI):
    def __init__(self, property, property_id, property_location):
        super(APropertyFile, self).__init__(property, property_id, APropertyType.FILE, property_location)
        self.property = property
        self.control = QtWidgets.QPushButton()
        self.control.clicked.connect(self.open_click)
        self.control.setMinimumWidth(10)
        self.control.setMinimumHeight(10)
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

    def open_click(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(ASharedItems.awidget, 'Open file',
                                                      'c:/', "Image files (*.jpg *.gif)")
        if fname[0] != '':
            self.change_event(fname[0])

    def change_event(self, file_name):
        print('file name: ' + file_name)
        # self.property.value = value
        # self.control.setText(value)
        # print('clicked')

    def set_text(self, text):
        self.control.setText(text)
