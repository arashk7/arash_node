from APortGUI import APortGUI


class AGraphPort:
    def __init__(self, port_id, node):
        self.__id = port_id
        self.caption=port_id
        self.__node = node
        self.link = None
        self.gui = APortGUI(port_id=port_id, node_gui=node.gui)

    # Port ID
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, port_id):
        self.__id = port_id
