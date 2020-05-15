from AGraphWidget.APlugin import APlugin, APropertyLocation, APropertyType
from yapsy.IPlugin import IPlugin
from keras.layers import Input, Dense

class Dense(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        APlugin.__init__(self, x=x, y=y)

        self.add_in_port('port_1')
        self.add_out_port('port_1')



    def init_node(self):

        print('Added node: ', self.node_id)


    def run(self):
        Dense_3 = Dense(name='Output', output_dim=40, activation='softmax')
        print(Dense_3)



