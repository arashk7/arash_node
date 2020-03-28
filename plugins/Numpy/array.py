from AGraphWidget.APlugin import APlugin
from yapsy.IPlugin import IPlugin
import numpy as np


class Array(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        APlugin.__init__(self, x=x, y=y)

        self.add_out_param('out')

        arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        arr = arr.reshape((3, 4))

        self.set_out_param('out', arr)

    def init_plugin(self):
        print("Init plugin " + self.node_type)

    def init_node(self):
        self.edit_run()
        pass

    def update_output_shape(self):
        self.params_out['out'].shape = (3,4)

    def run(self):
        pass


        # self.params_in['in'].va
