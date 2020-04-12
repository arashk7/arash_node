from AGraphWidget.APlugin import *

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


        # self.change_event()
        self.image = self.add_property_image('image1')
        self.image.gui.property_height = 150
        self.add_property_combobox('combo1', self.items)
        self.add_property_file('file', 'open')
        self.add_property_change_event('file', "change_event1")

    def init_node(self):
        super(Conv2D, self).init_node()
        self.gui.update()
        # self.change_event('file')
        # print(self.get_property('prop'))
        print('Added node: ', self.node_id)

    def change_event1(self):
        # pix = QtGui.QPixmap(self.get_property_value('file'))
        print(self.get_property_value('file'))
        # pix = pix.scaledToHeight(90)
        self.image.gui.set_image_file(self.get_property_value('file'))


    def run(self):
        print('run Conv2D')
        # while True:
        #     print('.')

        pass


