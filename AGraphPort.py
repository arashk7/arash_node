from APortGUI import APortGUI
from AUtil import APortType


class AGraphPort:
    def __init__(self, port_id, port_type, node):
        self.port_id = port_id
        self.caption = port_id
        self.node = node
        self.link = None
        self.port_type: self.PortType = port_type
        self.gui = APortGUI(port=self, port_id=port_id, port_type=port_type)
        self.gui.setParentItem(node.gui)
        self.gui.node_id = node.node_id

    def is_connected(self):
        if self.link:
            return True
        return False

    # Port ID
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, port_id):
        self.__id = port_id
