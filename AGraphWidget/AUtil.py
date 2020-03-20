from PyQt5 import QtCore, QtGui, QtWidgets
import math


class APortType:
    INPUT = 0
    OUTPUT = 1


class AParamType:
    INPUT = 0
    OUTPUT = 1


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
