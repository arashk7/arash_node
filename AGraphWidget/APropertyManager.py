from PyQt5 import QtWidgets
from AGraphWidget.AUtil import APropertyLocation
class APropertyManager:
    def __init__(self, window):
        self.window = window
        self.graph_node = None
    def connect(self, agraphnode):
        print(agraphnode.node_type)
        self.graph_node = agraphnode
    def update_property_bar(self):
        # Test Property bar
        self.tw = QtWidgets.QTreeWidget(self.window)
        self.window.verticalLayout_PropertyBar.addWidget(self.tw)
        self.tw.setColumnCount(2)
        self.tw.setHeaderLabels(["Properties", "Value"])

        root_1 = QtWidgets.QTreeWidgetItem(self.tw)
        root_1.setText(0, "Option_1")
        root_1.setText(1, "Option_1 Description")
