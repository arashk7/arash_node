from AGraphWidget import APropertyCombo, APropertyText, APropertyBool, APropertySlider, APropertyFile, APropertyImage
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
        self.gui = None
        if property_type == APropertyType.COMBO:
            self.gui = APropertyCombo.APropertyCombo(property=self, property_id=property_id,
                                                     property_location=property_location)
        elif property_type == APropertyType.TEXT:
            self.gui = APropertyText.APropertyText(property=self, property_id=property_id,
                                                   property_location=property_location)
        elif property_type == APropertyType.BOOL:
            self.gui = APropertyBool.APropertyBool(property=self, property_id=property_id,
                                                   property_location=property_location)
        elif property_type == APropertyType.SLIDER:
            self.gui = APropertySlider.APropertySlider(property=self, property_id=property_id,
                                                       property_location=property_location)
        elif property_type == APropertyType.FILE:
            self.gui = APropertyFile.APropertyFile(property=self, property_id=property_id,
                                                   property_location=property_location)
        elif property_type == APropertyType.IMAGE:
            self.gui = APropertyImage.APropertyImage(property=self, property_id=property_id,
                                                     property_location=property_location)
        self.gui.setParentItem(node.gui)
        self.gui.node_id = node.node_id

    # def add_combo_items(self, items):
    #     if self.gui:
    #         if self.property_type == APropertyType.COMBO:
    #             for item in items:
    #                 self.gui.add_item(item)
    #         else:
    #             print('AGraphProperty --> add item is just for combo property')

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
