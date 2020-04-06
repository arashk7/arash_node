from PyQt5 import QtWidgets
from AGraphWidget.ASkin import *
from AGraphWidget import APropertyGUI
from AGraphWidget.AUtil import ASharedItems, AMath, APropertyType


class APropertyFile(APropertyGUI.APropertyGUI):

    def __init__(self, property, property_id, property_location):
        super(APropertyFile, self).__init__(property, property_id, APropertyType.FILE, property_location)
        self.property = property
        self.open_file_filter= 'All files (*.*)' #"All files (*.jpg *.gif *.png)"
        self.control = QtWidgets.QPushButton()
        self.control.clicked.connect(self.open_click)
        self.control.setText('...')
        self.control.setFixedHeight(20)
        self.control.setMaximumWidth(25)
        layout = QtWidgets.QHBoxLayout()
        self.label = QtWidgets.QLabel()
        self.label.setText(self.property_id)
        self.label.setStyleSheet('background: gray')
        self.label.setMinimumHeight(10)
        self.label.setMaximumWidth(120)
        self.control.setStyleSheet('background: lightgray')
        self.widget = QtWidgets.QWidget()
        self.widget.setStyleSheet('background: gray')
        layout.addWidget(self.label)
        layout.addWidget(self.control)
        self.widget.setLayout(layout)
        self.widget.setMaximumWidth(self.rect.width())
        self.widget.setMinimumHeight(10)
        self.widget.layout().setContentsMargins(0, 0, 0, 0)

    def init(self):

        self.control_proxy: QtWidgets.QGraphicsProxyWidget = ASharedItems.awidget.scene().addWidget(self.widget)
        self.control_proxy.setParentItem(self)
        self.control_proxy.setZValue(1)
        super(APropertyFile, self).init()
        print('init file')

    def open_click(self):
        fname = QtWidgets.QFileDialog.getOpenFileName(ASharedItems.awidget, 'Open file',
                                                      'c:/', self.open_file_filter)
        if fname[0] != '':
            self.change_event(fname[0])

    def change_event(self, file_name):

        print('file name: ' + file_name)
        # self.file_name = file_name
        self.property.value = file_name
        self.property.node.change_event(self.property_id)

        self.label.setText(file_name)
        # self.control.setText(value)
        # print('clicked')

    def set_file_path(self, file_path):
        self.property.value = file_path
