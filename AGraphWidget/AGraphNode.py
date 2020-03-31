from PyQt5 import QtCore
from AGraphWidget.ALogger import ALogger
from AGraphWidget.ANodeGUI import ANodeGUI
from AGraphWidget.AGraphPort import AGraphPort


class AGraphNode:
    def __init__(self, node_id, node_type='', x=100, y=100):
        self.__node_id = node_id
        self.__caption = node_id
        self.node_type = node_type
        self.category = 'none'
        self.__params_in = {}
        self.__params_out = {}
        self.__ports_in = {}
        self.__ports_out = {}
        self.__props = {}
        self.__num_params_in_created = 0
        self.__num_params_out_created = 0
        self.num_ports_in_created = 0
        self.num_ports_out_created = 0
        self.gui = ANodeGUI(graph_node=self, x=x, y=y)

    # Add Property
    def add_prop(self, prop):
        self.__props[prop.property_id] = prop

    # Check dict to make sure there is no other prop with ID
    def is_prop_exist(self, prop_id):
        if prop_id in self.__props:
            return True
        return False

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

    # Adding param to the node
    def add_param_in(self, param):
        self.__params_in[param.param_id] = param

    # Check dict to make sure there is no other param with the param_id
    def is_param_in_exist(self, param_id):
        if param_id in self.__params_in:
            return True
        return False

    # Adding param to the entry node
    def add_param_out(self, param):
        self.__params_out[param.param_id] = param

    # Check dict to make sure there is no other param with param_id
    def is_param_out_exist(self, param_id):
        if param_id in self.__params_out:
            return True
        return False

    # Node ID
    @property
    def node_id(self):
        return self.__node_id

    @node_id.setter
    def node_id(self, node_id):
        if len(node_id) < 0:
            ALogger.print_error('The length of the ID must be more than 3 characters!')
            return
        else:
            self.__node_id = node_id

    # Entry ports property
    @property
    def ports_in(self):
        return self.__ports_in

    # Output ports property
    @property
    def ports_out(self):
        return self.__ports_out

    # Input params property
    @property
    def params_in(self):
        return self.__params_in

    # Output params property
    @property
    def params_out(self):
        return self.__params_out

    # Properties
    @property
    def props(self):
        return self.__props
