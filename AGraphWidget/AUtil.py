from PyQt5 import QtCore, QtGui, QtWidgets
import math


class APortType:
    INPUT = 0
    OUTPUT = 1


class AParamType:
    INPUT = 0
    OUTPUT = 1

class APropertyType:
    BOOL = 0
    TEXT = 1
    COLOR = 2
    VECTOR3 = 3
    VECTOR2 = 4
    INT = 5
    COMBO = 6
    SLIDER = 7
    FILE = 8
    IMAGE = 9
class APropertyLocation:
    NODE = 0
    TOOLBAR = 1

class ALinkType:
    PARAM = 0
    PORT = 1


class ACache:
    input_ports_gui = {}
    output_ports_gui = {}
    input_params_gui = {}
    output_params_gui = {}
    # copied nodes cache
    agraphnode_list = {}


class ASharedItems:
    awidget = None
    aPluginManager = None


class AMath:
    @staticmethod
    def distance(p1: QtCore.QPointF, p2: QtCore.QPointF):
        dist = math.hypot(p2.x() - p1.x(), p2.y() - p1.y())
        return dist
