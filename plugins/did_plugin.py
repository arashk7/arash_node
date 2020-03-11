from AGraphWidget.APlugin import APlugin
from yapsy.IPlugin import IPlugin

class didi_plugin(APlugin,IPlugin):
    def __init__(self):
        self.node_id= 'LSTM'
        self.x = 100
        self.y = 100
        APlugin.__init__(self, node_id=self.node_id, x=self.x, y=self.y)
    def print_name(self):
        print("This is plugin " + self.node_id)
