from PyQt5 import QtCore
from ALogger import ALogger
from ANodeGUI import ANodeGUI
from AGraphPort import AGraphPort

class AGraphNode:
    def __init__(self, node_id, x=100, y=100):
        self.node_id = node_id
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
        self.gui = ANodeGUI(graph_node=self, x=x, y=y)

        # port = AGraphPort('port_1')
        # self.ports_in['port_1']=port

    # Node ID
    # @property
    # def id(self):
    #     return self.__no
    #
    # @id.setter
    # def id(self, node_id):
    #     if len(node_id) < 3:
    #         ALogger.print_error('The length of id must be more than 3!')
    #         return
    #     else:
    #         self.__id = node_id
