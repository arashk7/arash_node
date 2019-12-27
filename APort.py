from PyQt5 import QtCore, QtGui, QtWidgets
from ABasePort import ABasePort
# from ABaseNode import ABaseNode
from ASkin import *


class APort(QtWidgets.QGraphicsItem, ABasePort):
    def __init__(self, port_id):
        APort.__init__(self, port_id)
        self.__id = port_id



