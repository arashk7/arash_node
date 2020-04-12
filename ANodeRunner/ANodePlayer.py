from AGraphWidget import AGraphNode, AGraphParam


class ANodePlayer:
    def __init__(self, graph):
        self.graph = graph

    def exec_recursive(self):
        print('exec recursive')
        for node in self.graph.nodes.values():
            if node.is_starter:
                self.exec_node(node=node)
    def check_node_inputs(self,node:AGraphNode.AGraphNode):
        for param in node.params_in.values():
            if not param.value:
                return False
        return True

    def exec_node(self, node: AGraphNode.AGraphNode):
        if not self.check_node_inputs(node=node):
            print('null input')
            return
        node.run_main()
        for param in node.params_out.values():
            for link in param.links.values():
                link.end.value = param.value
                print(link.end.node.node_id)
                self.exec_node(link.end.node)

        print('ok')
        return
