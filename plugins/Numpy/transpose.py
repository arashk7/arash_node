from AGraphWidget.APlugin import APlugin
from yapsy.IPlugin import IPlugin
from AGraphWidget import AGraphPort


class Transpose(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        # APlugin.__init__(self)
        self.node_id = ''
        self.node_type = 'Transpose'

        APlugin.__init__(self, node_id=self.node_id, node_type=self.node_type, x=x, y=y)


        self.add_in_param('param1')
        self.add_out_param('param1')


    def init_plugin(self):
        print("Init plugin " + self.node_type)

    def init_node(self):
        print('Added node: ', self.node_id)
