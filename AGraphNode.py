from PyQt5 import QtCore
from ALogger import ALogger
from ANodeGUI import ANodeGUI


class AGraphNode:
    def __init__(self, node_id, x=100, y=100):
        self._id = node_id
        self.__caption = node_id
        self.__category = 'none'
        self.__params_in = {}
        self.__params_out = {}
        self.ports_in = {}
        self.ports_out = {}
        self.__num_params_in_created = 0
        self.__num_params_out_created = 0
        self.num_ports_in_created = 0
        self.num_ports_out_created = 0
        self.gui = ANodeGUI(node_id=node_id, x=x, y=y)

    # Node ID
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, node_id):
        if len(node_id) < 3:
            ALogger.print_error('The length of id must be more than 3!')
            return
        else:
            self.__id = node_id
