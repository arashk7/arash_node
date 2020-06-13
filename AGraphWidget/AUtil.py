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
    FLOAT = 6
    COMBO = 7
    SLIDER = 8
    FILE = 9
    IMAGE = 10


class APropertyLocation:
    NODE = 0
    PROPERTYBAR = 1


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
    aPropertyManager = None


class AMath:
    @staticmethod
    def distance(p1: QtCore.QPointF, p2: QtCore.QPointF):
        dist = math.hypot(p2.x() - p1.x(), p2.y() - p1.y())
        return dist


class ATools:
    @staticmethod
    def str2tuple(str_shape):
        str_shape = ATools.remove_brackets(str_shape)
        tup = tuple(map(int, str_shape.split(',')))
        return tup

    @staticmethod
    def remove_brackets(str_tuple):
        return str_tuple.replace('(', '').replace(')', '')