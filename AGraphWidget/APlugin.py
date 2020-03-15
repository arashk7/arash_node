from AGraphWidget import AGraphNode, AUtil, AGraph
from AGraphWidget import AGraphPort, AWidget
from AGraphWidget.AUtil import ASharedItems


class APlugin(AGraphNode.AGraphNode):
    def __init__(self, node_id, node_type='', x=0, y=0):
        AGraphNode.AGraphNode.__init__(self, node_id=node_id, node_type=node_type, x=x, y=y)

    def add_in_port(self, port_name):
        self.add_port_in(port=AGraphPort.AGraphPort(port_name, AGraphPort.APortType.INPUT, self))

    def add_out_port(self, port_name):
        self.add_port_out(port=AGraphPort.AGraphPort(port_name, AGraphPort.APortType.OUTPUT, self))


    def edit_run(self):
        print('edit run')
        pass

    def run(self):
        print('run')
        pass

    def init_node(self):
        print('init_node: ' + self.node_id)
        pass

        # def print_name(self):
        #     print('parent')
        # self.awidget = awidget
        # node = self.awidget.add_node('teeeeest', 1000, 1000)
        # self.awidget.scene().addItem(self.gui)
        # self.category = 'pytorch'
        # port = AGraphPort('port_1', AUtil.APortType.INPUT, self)
        # self.add_port_in

        # def add_to_graph(self):
        #     self.awidget.add_full_node(self)
        #     self.awidget.scene().addItem(self.gui)
