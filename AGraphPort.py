from APortGUI import APortGUI


class AGraphPort:
    class PortType:
        INPUT = 0
        OUTPUT = 1

    def __init__(self, port_id, port_type, node):
        self.__id = port_id
        self.caption = port_id
        self.__node = node
        self.link = None
        self.port_type: self.PortType = port_type
        self.gui = APortGUI(port_id=port_id, node_gui=node.gui)

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
