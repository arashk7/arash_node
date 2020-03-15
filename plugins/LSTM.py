from AGraphWidget.APlugin import APlugin
from yapsy.IPlugin import IPlugin

class didi_plugin(APlugin,IPlugin):
    def __init__(self):
        self.node_id = ''
        self.node_type= 'LSTM'
        self.x = 100
        self.y = 100
        APlugin.__init__(self, node_id=self.node_id,node_type=self.node_type, x=self.x, y=self.y)
    def init_plugin(self):
        print("Init plugin " + self.node_type)

    def init_node(self):
        print('Added node: ', self.node_id)
