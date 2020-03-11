from PyQt5 import QtCore
from random import randint

from AGraphWidget.AGraphNode import AGraphNode

from AGraphWidget.AGraphPort import AGraphPort
from AGraphWidget.ALogger import ALogger
from AGraphWidget.AGraphLink import AGraphLink
from AGraphWidget.AUtil import APortType, ACache


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
        self.__num_nodes_active = 0

    def copy_node(self, node: AGraphNode):
        node_id = node.node_id
        if node.node_id in self.nodes:
            i = 0
            while True:
                node_id = 'node_' + str(self.__num_nodes_created + i)
                if node_id not in self.nodes:
                    break
                i += 1

        new_node = AGraphNode(node_id, node.gui.pos.x(), node.gui.pos.y())
        self.nodes[node_id] = new_node

        for p in node.ports_in.values():
            self.add_port_in(node_id=node_id, port_id=p.port_id)
        for p in node.ports_out.values():
            self.add_port_out(node_id=node_id, port_id=p.port_id)

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
        node = AGraphNode(node_id, x, y)
        self.nodes[node_id] = node
        self.__num_nodes_created += 1
        return node

    # Add Node to the Graph
    def add_full_node(self, node):
        # Node ID has to be exclusive
        # Check dict to make sure there is no other node with ID
        node_id = node.node_id
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
        # Set node name
        node.node_id = node_id

        self.nodes[node_id] = node
        self.__num_nodes_created += 1

        for _port in node.ports_in.values():
            ACache.input_ports_gui[_port.port_id + '_' + node_id] = _port.gui
            self.__num_ports_in_created += 1
            print('port '+ _port.port_id +' added to '+ node.node_id)
        for _port in node.ports_out.values():
            ACache.output_ports_gui[_port.port_id + '_' + node_id] = _port.gui
            self.__num_ports_out_created += 1
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
        self.nodes[node_id].gui.init_ports_locations()
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
        self.nodes[node_id].gui.init_ports_locations()
        self.__num_ports_out_created += 1
        return p_out

    # Add Link
    def add_link(self, node_id_from, port_id_from, node_id_to, port_id_to, link_id=None):
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
        self.links[link_id] = link
        self.nodes[node_id_from].ports_out[port_id_from].link = link
        self.nodes[node_id_to].ports_in[port_id_to].link = link
        self.__num_links_created += 1
        return link

    # Remove Input Port
    def remove_port_in(self, node_id, port_id):
        del self.nodes[node_id].ports_in[port_id]