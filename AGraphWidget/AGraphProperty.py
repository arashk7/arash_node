from AGraphWidget.APropertyGUI import APropertyGUI
from AGraphWidget.AUtil import APropertyType



class AGraphProperty:
    def __init__(self, property_id, property_type, property_location, node):
        self.property_id = property_id
        self.caption = property_id
        self.property_type = property_type
        self.property_location = property_location
        self.node = node

        self.data_type = None
        self.__value = None

        self.shape = None
        self.gui = APropertyGUI(property=self, property_id=property_id, property_type=property_type, property_location= property_location)
        self.gui.setParentItem(node.gui)
        self.gui.node_id = node.node_id




    # property value
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value

    # # param ID
    # @property
    # def id(self):
    #     return self.__id
    #
    # @id.setter
    # def id(self, property_id):
    #     self.__id = property_id
