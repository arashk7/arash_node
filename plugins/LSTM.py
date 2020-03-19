from AGraphWidget.APlugin import APlugin
from yapsy.IPlugin import IPlugin


class LSTM(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        self.node_id = ''
        self.node_type = 'LSTM'
        APlugin.__init__(self, node_id=self.node_id, node_type=self.node_type, x=x, y=y)

    def init_plugin(self):
        print("Init plugin " + self.node_type)

    def init_node(self):
        print('Added node: ', self.node_id)
