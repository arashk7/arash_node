from PyQt5 import QtCore, QtGui, QtWidgets
from ABasePort import ABasePort
# from ABaseNode import ABaseNode
from ASkin import *


class APortGUI(QtWidgets.QGraphicsItem):
    def __init__(self, port_id):
        super(APortGUI, self).__init__()
        self.__id = port_id
        




