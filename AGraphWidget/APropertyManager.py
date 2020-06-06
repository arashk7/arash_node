from PyQt5 import QtWidgets, QtCore
from AGraphWidget.AUtil import APropertyLocation


class APropertyManager:
    def __init__(self, window):
        self.window = window
        self.graph_node = None

    def connect(self, agraphnode):
        print(agraphnode.node_type)
        self.graph_node = agraphnode
        self.update_property_bar()

    def update_property_bar(self):
        for i in reversed(range(self.window.verticalLayout_PropertyBar.count())):
            self.window.verticalLayout_PropertyBar.itemAt(i).widget().deleteLater()

        # Test Property bar
        self.tw = QtWidgets.QTreeWidget(self.window)
        self.window.verticalLayout_PropertyBar.addWidget(self.tw)
        self.tw.setColumnCount(2)
        self.tw.setHeaderLabels(["Properties", "Value"])

        root_1 = QtWidgets.QTreeWidgetItem(self.tw)
        root_1.setText(0, "Option_1")
        root_1.setText(1, "Option_1 Description")

        for prop in self.graph_node.props.values():
            if prop.property_location == APropertyLocation.PROPERTYBAR:
                print(prop.property_id)

        # item_1 = QtWidgets.QTreeWidgetItem()
        # item_1.setText(0, "enabled")
        # item_1.setFlags(item_1.flags() | QtCore.Qt.ItemIsUserCheckable)
        # item_1.setCheckState(1, QtCore.Qt.Checked)
