from AGraphWidget.APlugin import APlugin
from yapsy.IPlugin import IPlugin
from AGraphWidget import AGraphPort


class PluginOne(APlugin, IPlugin):
    def __init__(self):
        # APlugin.__init__(self)
        self.node_id = ''
        self.node_type = 'Conv2D'
        self.x = 100
        self.y = 100
        APlugin.__init__(self, node_id=self.node_id,node_type=self.node_type, x=self.x, y=self.y)

        self.add_in_port('port_1')
        self.add_in_port('port_2')
        self.add_out_port('port_1')
        self.ports_in['port_1'].value = 5

    def init_plugin(self):
        print("Init plugin " + self.node_type)


    def init_node(self):
        print('Added node: ', self.node_id)

