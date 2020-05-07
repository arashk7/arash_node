from AGraphWidget.APlugin import APlugin, APropertyLocation, APropertyType
from yapsy.IPlugin import IPlugin

class Merge(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        APlugin.__init__(self, x=x, y=y)

        self.add_in_port('port_1')
        self.add_in_port('port_2')
        self.add_out_port('port_1')



    def init_node(self):
        # APlugin.init_node()

        # self.change_event('file')
        # print(self.get_property('prop'))
        print('Added node: ', self.node_id)


    def run(self):
        print('run Conv2D')
        # while True:
        #     print('.')

        pass


