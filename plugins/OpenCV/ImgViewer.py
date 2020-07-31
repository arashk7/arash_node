from AGraphWidget.APlugin import APlugin, APropertyLocation, APropertyType
from yapsy.IPlugin import IPlugin
import numpy as np
import cv2 as cv


class ImgViewer(APlugin, IPlugin):
    def __init__(self, x=0, y=0):
        APlugin.__init__(self, x=x, y=y)

        # self.is_starter = True
        self.add_in_port('in')

        self.img = self.add_property_image('viewer')
        self.add_property_file('image_file', '')
        self.add_property_change_event('image_file', "change_event1")

    def init_plugin(self):
        print("Init plugin " + self.node_type)

    def init_node(self):
        print('Added node: ', self.node_id)


    def run(self):
        print('input run')
        # file_path = self.get_property_node_value('image_file')
        # if file_path:
        #     img = cv.imread(filename=file_path)
        #     if img:
        #         self.set_out_param('out', img)

    def change_event1(self):
        self.img.gui.set_image_file(self.get_property_node_value('image_file'))

        # self.params_in['in'].va
