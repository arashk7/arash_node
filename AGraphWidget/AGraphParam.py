from AGraphWidget.AParamGUI import AParamGUI
from AGraphWidget.AUtil import AParamType


class AGraphParam:
    def __init__(self, param_id, param_type, node):
        self.param_id = param_id
        self.caption = param_id
        self.node = node
        self.links = dict()
        self.data_type = None
        self.__value = None
        self.param_type = param_type
        self.shape = None
        self.gui = AParamGUI(param=self, param_id=param_id, param_type=param_type)
        self.gui.setParentItem(node.gui)
        self.gui.node_id = node.node_id


    def is_connected(self):
        if len(self.links.items()) > 0:
            return True
        return False

    # param value
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = new_value


