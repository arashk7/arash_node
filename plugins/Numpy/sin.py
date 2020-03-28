from AGraphWidget.APlugin import APlugin
from yapsy.IPlugin import IPlugin
from AGraphWidget import AGraphPort


class Sin(APlugin, IPlugin):
    def __init__(self, x=0, y=0):

        APlugin.__init__(self, x=x, y=y)

        self.add_in_param('in')
        self.add_out_param('out')

    def init_plugin(self):
        print("Init plugin " + self.node_type)

    def init_node(self):
        print('Added node: ', self.node_id)

    def update_output_shape(self):
        if self.params_in['in'].is_connected():
            self.params_out['out'].shape = (4, 3, 5)
        else:
            self.params_out['out'].shape = None

    def run(self):
        pass


        # self.params_in['in'].va
