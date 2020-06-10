from PyQt5 import QtWidgets, QtCore
from AGraphWidget.AUtil import APropertyLocation,APropertyType


class APropertyManager:
    def __init__(self, window):
        self.window = window
        self.graph_node = None

    def connect(self, agraphnode):
        print(agraphnode.node_type)
        self.graph_node = agraphnode
        self.update_property_bar()
    def update_node(self,item,column):
        print(item.text(1))
        print(str(column))
        if self.graph_node.is_prop_ext_exist(item.text(0)):
            self.graph_node.props_ext[item.text(0)].value = item.text(1)

    def update_property_bar(self):
        for i in reversed(range(self.window.verticalLayout_PropertyBar.count())):
            self.window.verticalLayout_PropertyBar.itemAt(i).widget().deleteLater()

        # Test Property bar
        self.tw = QtWidgets.QTreeWidget(self.window)
        self.window.verticalLayout_PropertyBar.addWidget(self.tw)
        self.tw.setColumnCount(2)
        self.tw.setHeaderLabels(["Properties", "Value"])
        self.tw.itemChanged.connect(self.update_node)

        root_1 = QtWidgets.QTreeWidgetItem(self.tw)
        root_1.setExpanded(True)
        root_1.setText(0, "Option_1")
        root_1.setText(1, "Option_1 Description")

        for prop in self.graph_node.props_ext.values():
            if prop.property_location == APropertyLocation.PROPERTYBAR:
                if prop.property_type == APropertyType.BOOL:
                    item_1 = QtWidgets.QTreeWidgetItem()
                    item_1.setText(0, prop.property_id)
                    item_1.setFlags(item_1.flags() | QtCore.Qt.ItemIsUserCheckable)
                    item_1.setCheckState(1, QtCore.Qt.Checked)
                    root_1.addChild(item_1)
                elif prop.property_type == APropertyType.TEXT:
                    item_1 = QtWidgets.QTreeWidgetItem()
                    item_1.setText(0, prop.property_id)
                    item_1.setText(1, prop.value)
                    item_1.setFlags(item_1.flags() | QtCore.Qt.ItemIsEditable)

                    # item_1.setCheckState(1, QtCore.Qt.Checked)
                    root_1.addChild(item_1)


