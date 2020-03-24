from AGraphWidget.APortGUI import APortGUI
from AGraphWidget.AUtil import APortType


class AGraphPort:
    def __init__(self, port_id, port_type, node):
        self.port_id = port_id
        self.caption = port_id
        self.node = node
        self.links = dict()

        self.data_type = None
        self.__value = None
        self.port_type = port_type
        self.gui = APortGUI(port=self, port_id=port_id, port_type=port_type)
        self.gui.setParentItem(node.gui)
        self.gui.node_id = node.node_id

    def is_connected(self):
        if len(self.links) > 0:
            return True
        return False

    # port value
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    # Port ID
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, port_id):
        self.__id = port_id
