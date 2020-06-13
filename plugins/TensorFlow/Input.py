from AGraphWidget.APlugin import APlugin, APropertyLocation, APropertyType
from yapsy.IPlugin import IPlugin
from AGraphWidget.AUtil import ATools
from keras import layers


class Input(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        APlugin.__init__(self, x=x, y=y)

        # self.add_in_port('port_1')
        self.add_out_port('port_1')

        self.add_property_text(property_name='Shape', value='(50,50,50)',
                               property_location=APropertyLocation.PROPERTYBAR)

    def init_node(self):
        print('Added node: ', self.node_id)

    def run(self):
        str = self.get_property_pm_value('Shape')
        print(str)
        tup= ATools.str2tuple(str)
        print(tup)


        in_1 = layers.Input(shape=tup,name=self.node_id)
        print(in_1)
