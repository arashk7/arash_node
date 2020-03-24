from AGraphWidget.APlugin import APlugin
from yapsy.IPlugin import IPlugin
from AGraphWidget import AGraphPort


class Sin(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        # APlugin.__init__(self)
        self.node_id = ''
        self.node_type = __class__.__name__

        APlugin.__init__(self, node_id=self.node_id, node_type=self.node_type, x=x, y=y)


        self.add_in_param('in')
        self.add_out_param('out')


    def init_plugin(self):
        print("Init plugin " + self.node_type)

    def init_node(self):
        print('Added node: ', self.node_id)

    def run(self):
        pass
        # self.params_in['in'].va

