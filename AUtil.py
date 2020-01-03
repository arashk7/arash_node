from PyQt5 import QtCore, QtGui, QtWidgets
import math


class APortType:
    INPUT = 0
    OUTPUT = 1


class ACache:
    input_ports_gui = {}
    output_ports_gui = {}


class AMath:
    @staticmethod
    def distance(p1: QtCore.QPointF, p2: QtCore.QPointF):
        dist = math.hypot(p2.x() - p1.x(), p2.y() - p1.y())
        return dist
