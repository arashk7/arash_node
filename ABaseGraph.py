from ABaseNode import ABaseNode
from ABasePort import ABasePort


class ABaseGraph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, node_id):
        node = ABaseNode(node_id)
        self.nodes[node_id] = node

    def add_port_in(self, node_id, port_id):
        p_in = ABasePort(port_id)
        self.nodes[node_id]._ports_in[port_id] = p_in
