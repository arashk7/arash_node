class ANodePlayer:
    def __init__(self):
        self.start_nodes = {}

    def run_all(self):

        print('Run')
        for node in self.start_nodes:
            self.exec_node(node=node)


    def exec_node(self, node):
        node.run()
        print(node.node_id)
