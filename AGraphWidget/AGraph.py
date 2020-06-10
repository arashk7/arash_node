from PyQt5 import QtCore
from random import randint

from AGraphWidget.AGraphNode import AGraphNode

from AGraphWidget.AGraphPort import AGraphPort
from AGraphWidget.AGraphParam import AGraphParam
from AGraphWidget.AGraphProperty import AGraphProperty
from AGraphWidget.ALogger import ALogger
from AGraphWidget.AGraphLink import AGraphLink
from AGraphWidget.AUtil import APortType, AParamType, ACache, ALinkType, APropertyType, APropertyLocation


class AGraph:
    def __init__(self, graph_id):
        self.graph_id = graph_id
        self.nodes = {}
        self.links = {}
        # self.ports_in = {}
        # self.ports_out = {}
        self.__num_nodes_created = 0
        self.__num_links_created = 0
        self.__num_ports_in_created = 0
        self.__num_ports_out_created = 0
        self.__num_params_in_created = 0
        self.__num_params_out_created = 0
        self.__num_props_created = 0
        self.__num_nodes_active = 0

    def copy_node(self, node: AGraphNode,x=100,y=100):
        node_id = node.node_id
        if node.node_id in self.nodes:
            i = 0
            while True:
                node_id = 'node_' + str(self.__num_nodes_created + i)
                if node_id not in self.nodes:
                    break
                i += 1

        new_node = AGraphNode(node_id=node_id,node_type=node.node_type, x=int(x), y=int(y))
        self.nodes[node_id] = new_node

        # Copy Properties
        for p in node.props.values():
            self.add_prop(node_id=node_id, property_id=p.property_id, property_type=p.property_type,
                          property_location=p.property_location)

        # Copy Params
        for p in node.params_in.values():
            self.add_param_in(node_id=node_id, param_id=p.param_id)
        for p in node.params_out.values():
            self.add_param_out(node_id=node_id, param_id=p.param_id)

        # Copy ports
        for p in node.ports_in.values():
            self.add_port_in(node_id=node_id, port_id=p.port_id)
        for p in node.ports_out.values():
            self.add_port_out(node_id=node_id, port_id=p.port_id)


        self.nodes[node_id].gui.init_params_props_locations()
        self.nodes[node_id].gui.init_ports_locations()
        self.__num_nodes_created += 1
        return new_node

    # Add Node to the Graph
    def add_node(self, node_id='', x=100, y=100):
        # Node ID has to be exclusive
        # Check dict to make sure there is no other node with ID
        if node_id in self.nodes:
            ALogger.print_error("The node ID is already taken!")
            return
        # If user does not give the ID parameter, it will be generated by random number
        if node_id is '':
            i = 0
            while True:
                node_id = 'node_' + str(self.__num_nodes_created + i)
                if node_id not in self.nodes:
                    break
                i += 1
        # Instantiate new Node object
        node = AGraphNode(node_id, 'void', x, y)
        self.nodes[node_id] = node
        self.__num_nodes_created += 1
        return node

    # Add Node to the Graph
    def add_full_node(self, node):
        # Node ID has to be exclusive
        # Check dict to make sure there is no other node with ID
        node_id = node.node_id
        if node_id in self.nodes:
            # ALogger.print_error("The node ID is already taken!")
            node_id = ''
        # If user does not give the ID parameter, it will be generated by random number
        if node_id is '':
            i = 0
            while True:
                node_id = node.node_type + '_' + str(self.__num_nodes_created + i)
                if node_id not in self.nodes:
                    break
                i += 1
        # Set node name
        # new_node = AGraphNode(node_id)
        node.node_id = node_id

        # Add ports
        for _port in node.ports_in.values():
            _port.node_id = node_id
            _port.gui.node_id = node_id
            ACache.input_ports_gui[_port.port_id + '_' + node_id] = _port.gui
            self.__num_ports_in_created += 1
            # print('port '+ _port.port_id +' added to '+ node.node_id)
        for _port in node.ports_out.values():
            _port.node_id = node_id
            _port.gui.node_id = node_id
            ACache.output_ports_gui[_port.port_id + '_' + node_id] = _port.gui
            self.__num_ports_out_created += 1

        # Add params
        for _param in node.params_in.values():
            _param.node_id = node_id
            _param.gui.node_id = node_id
            ACache.input_params_gui[_param.param_id + '_' + node_id] = _param.gui
            self.__num_params_in_created += 1
            # print('port '+ _port.port_id +' added to '+ node.node_id)
        for _param in node.params_out.values():
            _param.node_id = node_id
            _param.gui.node_id = node_id
            ACache.output_params_gui[_param.param_id + '_' + node_id] = _param.gui
            self.__num_params_out_created += 1

        # Add properties
        for _prop in node.props.values():
            _prop.node_id = node_id
            if _prop.gui:
                _prop.gui.node_id = node_id
            # _prop.gui.init()
            # ACache.input_params_gui[_param.param_id + '_' + node_id] = _param.gui
            self.__num_props_created += 1

        self.nodes[node_id] = node
        self.__num_nodes_created += 1
        self.nodes[node_id].gui.init_params_props_locations()
        self.nodes[node_id].gui.init_ports_locations()
        return node

    # Remove Node
    def remove_node(self, node_id):
        del self.nodes[node_id]

    # Add Input Port to the Node
    def add_port_in(self, node_id, port_id=None):
        # Check node ID existence
        if node_id not in self.nodes:
            ALogger.print_error("The node ID does not exist!")
            return

        # Port ID has to be exclusive
        # Check dict to make sure there is no other node with ID
        if self.nodes[node_id].is_port_in_exist(port_id=port_id):
            ALogger.print_error("The port ID is already taken!")
            return

        # If user does not give the ID parameter, it will be generated
        if port_id is None:
            i = 0
            while True:
                port_id = 'port_' + str(self.__num_ports_in_created + i)
                if port_id not in self.nodes[node_id].ports_in:
                    break
                i += 1

        # Instantiate new Port object
        p_in = AGraphPort(port_id, APortType.INPUT, self.nodes[node_id])
        self.nodes[node_id].add_port_in(p_in)
        ACache.input_ports_gui[port_id + '_' + node_id] = p_in.gui
        # self.nodes[node_id].gui.init_ports_locations()
        self.__num_ports_in_created += 1
        return p_in

    # Add Output Port to the Node
    def add_port_out(self, node_id, port_id=None):
        # Check node ID existence
        if node_id not in self.nodes:
            ALogger.print_error("The node ID does not exist!")
            return

        # Port ID has to be exclusive
        # Check dict to make sure there is no other port with ID
        if self.nodes[node_id].is_port_out_exist(port_id=port_id):
            ALogger.print_error("The port ID is already taken!")
            return

        # If user does not give the ID parameter, it will be generated
        if port_id is None:
            i = 0
            while True:
                port_id = 'port_' + str(self.__num_ports_out_created + i)
                if port_id not in self.nodes[node_id].ports_out:
                    break
                i += 1

        # Instantiate new Port object
        p_out = AGraphPort(port_id, APortType.OUTPUT, self.nodes[node_id])
        self.nodes[node_id].add_port_out(p_out)
        ACache.output_ports_gui[port_id + '_' + node_id] = p_out.gui

        # self.nodes[node_id].gui.init_ports_locations()
        self.__num_ports_out_created += 1
        return p_out

    # Add Input Parameter to the Node
    def add_param_in(self, node_id, param_id=None):
        # Check node ID existence
        if node_id not in self.nodes:
            ALogger.print_error("The node ID does not exist!")
            return

        # Port ID has to be exclusive
        # Check dict to make sure there is no other node with ID
        if self.nodes[node_id].is_param_in_exist(param_id=param_id):
            ALogger.print_error("The param ID is already taken!")
            return

        # If user does not give the ID parameter, it will be generated
        if param_id is None:
            i = 0
            while True:
                param_id = 'param_' + str(self.__num_params_in_created + i)
                if param_id not in self.nodes[node_id].param_in:
                    break
                i += 1

        # Instantiate new Port object
        p_in = AGraphParam(param_id, AParamType.INPUT, self.nodes[node_id])
        self.nodes[node_id].add_param_in(p_in)
        ACache.input_params_gui[param_id + '_' + node_id] = p_in.gui
        # self.nodes[node_id].gui.init_params_props_locations()
        self.__num_params_in_created += 1
        return p_in

    # Add Output Param to the Node
    def add_param_out(self, node_id, param_id=None):
        # Check node ID existence
        if node_id not in self.nodes:
            ALogger.print_error("The node ID does not exist!")
            return

        # Port ID has to be exclusive
        # Check dict to make sure there is no other port with ID
        if self.nodes[node_id].is_param_out_exist(param_id=param_id):
            ALogger.print_error("The param ID is already taken!")
            return

        # If user does not give the ID parameter, it will be generated
        if param_id is None:
            i = 0
            while True:
                param_id = 'param_' + str(self.__num_params_out_created + i)
                if param_id not in self.nodes[node_id].params_out:
                    break
                i += 1

        # Instantiate new Port object
        p_out = AGraphParam(param_id, AParamType.OUTPUT, self.nodes[node_id])
        self.nodes[node_id].add_param_out(p_out)
        ACache.output_params_gui[param_id + '_' + node_id] = p_out.gui
        # self.nodes[node_id].gui.init_params_props_locations()
        self.__num_params_out_created += 1
        return p_out

    # Add Output Param to the Node
    def add_prop(self, node_id, property_id=None, property_type=APropertyType.INT, property_location=APropertyLocation.NODE):
        # Check node ID existence
        if node_id not in self.nodes:
            ALogger.print_error("The node ID does not exist!")
            return

        # property ID has to be exclusive
        # Check dict to make sure there is no other Prop with ID
        if self.nodes[node_id].is_prop_exist(prop_id=property_id):
            ALogger.print_error("The property ID is already taken!")
            return

        # If user does not give the ID parameter, it will be generated
        if property_id is None:
            i = 0
            while True:
                property_id = 'prop_' + str(self.__num_props_created + i)
                if property_id not in self.nodes[node_id].props:
                    break
                i += 1

        # Instantiate new Port object
        prop = AGraphProperty(property_id=property_id, property_type=property_type, property_location=property_location, node=self.nodes[node_id])
        self.nodes[node_id].add_prop(prop)
        # ACache.output_params_gui[property_id + '_' + node_id] = prop.gui
        # self.nodes[node_id].gui.init_params_props_locations()
        self.__num_props_created += 1
        return prop

    # Add Link to port
    def add_link_to_port(self, node_id_from, port_id_from, node_id_to, port_id_to, link_id=None):
        # Check source and target nodes availability
        if node_id_from not in self.nodes or node_id_to not in self.nodes:
            ALogger.print_error("The node ID does not exist!")
            return
        # Check source and target ports availability
        if port_id_from not in self.nodes[node_id_from].ports_out or \
                        port_id_to not in self.nodes[node_id_to].ports_in:
            ALogger.print_error("The port ID does not exist!")
            return

        # If user does not give the link ID parameter, it will be generated
        if link_id is None:
            i = 0
            while True:
                link_id = 'link_' + str(self.__num_links_created + i)
                if link_id not in self.links:
                    break
                i += 1

        # Instantiate new link object
        link = AGraphLink(link_id=link_id, start=self.nodes[node_id_from].ports_out[port_id_from],
                          end=self.nodes[node_id_to].ports_in[port_id_to])

        link.gui.link_type = ALinkType.PORT
        self.links[link_id] = link
        self.nodes[node_id_from].ports_out[port_id_from].links[link_id] = link
        self.nodes[node_id_to].ports_in[port_id_to].links[link_id] = link
        self.__num_links_created += 1
        return link

    # Add Link to param
    def add_link_to_param(self, node_id_from, param_id_from, node_id_to, param_id_to, link_id=None):
        # Check source and target nodes availability
        if node_id_from not in self.nodes or node_id_to not in self.nodes:
            ALogger.print_error("The node ID does not exist!")
            return
        # Check source and target ports availability
        if param_id_from not in self.nodes[node_id_from].params_out or \
                        param_id_to not in self.nodes[node_id_to].params_in:
            ALogger.print_error("The param ID does not exist!")
            return

        # If user does not give the link ID parameter, it will be generated
        if link_id is None:
            i = 0
            while True:
                link_id = 'link_' + str(self.__num_links_created + i)
                if link_id not in self.links:
                    break
                i += 1

        # Instantiate new link object
        link = AGraphLink(link_id=link_id, start=self.nodes[node_id_from].params_out[param_id_from],
                          end=self.nodes[node_id_to].params_in[param_id_to])
        link.gui.link_type = ALinkType.PARAM
        self.links[link_id] = link
        self.nodes[node_id_from].params_out[param_id_from].links[link_id] = link
        self.nodes[node_id_to].params_in[param_id_to].links[link_id] = link
        self.__num_links_created += 1
        self.nodes[node_id_from].edit_run()
        return link

    # Remove Input Port
    def remove_port_in(self, node_id, port_id):
        del self.nodes[node_id].ports_in[port_id]
