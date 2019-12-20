from random import randint

from ABaseNode import ABaseNode
from ABasePort import ABasePort
from ALogger import ALogger,MsgColors

class ABaseGraph:
    def __init__(self):
        self.nodes = {}
        self.__num_nodes_created = 0

    # Add Node to the Graph
    def add_node(self, node_id=None):
        # Node ID has to be exclusive
        # Check dict to make sure there is no other node with ID
        if node_id in self.nodes:
            ALogger.print_error("The node ID is already taken!")
            return
        # If user does not give the ID parameter, it will be generated by random number
        if node_id is None:
            while True:
                node_id = 'node_' + str(randint(1, 10000))
                if node_id not in self.nodes:
                    break
        # Instantiate new Node object
        node = ABaseNode(node_id)
        self.nodes[node_id] = node
        self.__num_nodes_created += 1

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
        if port_id in self.nodes[node_id].ports_in:
            ALogger.print_error("The node ID is already taken!")
            return
        # If user does not give the ID parameter, it will be generated ny random number
        if port_id is None:
            while True:
                port_id = 'port_' + str(randint(1, 10000))
                if port_id not in self.nodes[node_id].ports_in:
                    break
        # Instantiate new Port object
        p_in = ABasePort(port_id)
        self.nodes[node_id].ports_in[port_id] = p_in

    # Remove Input Port
    def remove_port_in(self, node_id, port_id):
        del self.nodes[node_id].ports_in[port_id]
        self.__num_nodes_active -= 1