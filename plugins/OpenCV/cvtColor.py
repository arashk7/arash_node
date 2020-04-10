from AGraphWidget.APlugin import APlugin, APropertyLocation, APropertyType
from yapsy.IPlugin import IPlugin
import numpy as np
import cv2 as cv

class cvtColor(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        APlugin.__init__(self, x=x, y=y)

        self.add_in_param('in')
        self.add_out_param('out')

        self.img = self.add_property_image('viewer')


    def init_plugin(self):
        print("Init plugin " + self.node_type)

    def init_node(self):
        print('Added node: ', self.node_id)

    def update_output_shape(self):
        img = self.params_out['out'].value
        if img:
            self.params_out['out'].shape = img.shape

    def run(self):
        source = self.get_in_param('in')
        if source:
            dest = cv.cvtColor(source, cv.COLOR_BGR2GRAY)
            print('ok gray')

    def change_event1(self):
        self.img.gui.set_image_file(self.get_property_value('image_file'))


        # self.params_in['in'].va
