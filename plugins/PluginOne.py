from AGraphWidget.APlugin import APlugin
from yapsy.IPlugin import IPlugin
from AGraphWidget import AGraphPort


class PluginOne(APlugin, IPlugin):
    def __init__(self):
        # APlugin.__init__(self)
        self.node_id = 'Conv_11'
        self.x = 100
        self.y = 100
        APlugin.__init__(self, node_id=self.node_id, x=self.x, y=self.y)
        self.add_port_in(AGraphPort.AGraphPort('port_1', AGraphPort.APortType.INPUT, self))
        self.add_port_in(AGraphPort.AGraphPort('port_2', AGraphPort.APortType.INPUT, self))
        self.add_port_out(AGraphPort.AGraphPort('port_1', AGraphPort.APortType.OUTPUT, self))

    def print_name(self):
        print("This is plugin " + self.node_id)

    def init_ports(self):
        pass
