from AGraphWidget.APlugin import APlugin
from yapsy.IPlugin import IPlugin
from AGraphWidget import AGraphPort


class MaxPool2D(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        # APlugin.__init__(self)
        self.node_id = ''
        self.node_type = 'MaxPool2D'
        APlugin.__init__(self, node_id=self.node_id, node_type=self.node_type, x=x, y=y)

        # self.add_port_in(AGraphPort.AGraphPort('port_1', AGraphPort.APortType.INPUT, self))
        # self.add_port_out(AGraphPort.AGraphPort('port_1', AGraphPort.APortType.OUTPUT, self))

    def init_plugin(self):
        print("Init plugin " + self.node_type)

    def init_node(self):
        print('Added node: ', self.node_id)
