from PyQt5 import QtWidgets
class APropertyManager:
    def __init__(self, window):
        self.window = window

    def update(self):
        # Test Property bar
        self.tw = QtWidgets.QTreeWidget(self.window)
        self.window.verticalLayout_PropertyBar.addWidget(self.tw)
        self.tw.setColumnCount(2)
        self.tw.setHeaderLabels(["Properties", "Value"])

        root_1 = QtWidgets.QTreeWidgetItem(self.tw)
        root_1.setText(0, "Option_1")
        root_1.setText(1, "Option_1 Description")
