from PyQt5 import QtCore
from ArashWidget.ALogger import ALogger
from ArashWidget.ANodeGUI import ANodeGUI
from ArashWidget.AGraphPort import AGraphPort


class AGraphNode:
    def __init__(self, node_id, x=100, y=100):
        self.__node_id = node_id
        self.__caption = node_id
        self.__category = 'none'
        self.__params_in = {}
        self.__params_out = {}
        self.__ports_in = {}
        self.__ports_out = {}
        self.__num_params_in_created = 0
        self.__num_params_out_created = 0
        self.num_ports_in_created = 0
        self.num_ports_out_created = 0
        self.gui = ANodeGUI(graph_node=self, x=x, y=y)

    # Adding port to the entry node
    def add_port_in(self, port):
        self.__ports_in[port.port_id] = port

    # Check dict to make sure there is no other port with ID
    def is_port_in_exist(self, port_id):
        if port_id in self.__ports_in:
            return True
        return False

    # Adding port to the entry node
    def add_port_out(self, port):
        self.__ports_out[port.port_id] = port

    # Check dict to make sure there is no other port with ID
    def is_port_out_exist(self, port_id):
        if port_id in self.__ports_out:
            return True
        return False

    # Node ID
    @property
    def node_id(self):
        return self.__node_id

    @node_id.setter
    def node_id(self, node_id):
        if len(node_id) < 3:
            ALogger.print_error('The length of the ID must be more than 3 characters!')
            return
        else:
            self.__node_id = node_id

    # Entry ports getter
    @property
    def ports_in(self):
        return self.__ports_in

    # Output ports getter
    @property
    def ports_out(self):
        return self.__ports_out
