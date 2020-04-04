from AGraphWidget.APlugin import APlugin, IPlugin


class Conv2D(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        APlugin.__init__(self, x=x, y=y)

        self.add_in_port('port_1')
        self.add_in_port('port_2')
        self.add_in_param('param_1')
        self.add_out_port('port_1')
        self.ports_in['port_1'].value = 5

        self.items = {'item_1', 'item_2', 'item_3'}

        self.add_property_bool('checkbox', False)
        self.add_property_text('edit1', 'type here')
        self.add_property_slider('slider1', 40)
        self.add_property_file('load file','open')
        self.add_property_image('image1')
        self.add_property_combobox('combo1', self.items)

    def init_node(self):
        super(Conv2D, self).init_node()
        # print(self.get_property('prop'))
        print('Added node: ', self.node_id)
