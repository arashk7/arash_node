from PyQt5 import QtCore, QtGui, QtWidgets
from ASkin import *

class ARubberBand:
    def __init__(self, widget_parent, color):
        self.__rubber_band = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, widget_parent)
        rubber_band_palette = QtGui.QPalette()
        rubber_band_brush = QtGui.QBrush(color)
        rubber_band_palette.setBrush(QtGui.QPalette.Highlight, rubber_band_brush)
        self.__rubber_band.setPalette(rubber_band_palette)
        self.__origin = None

    def mouse_press_event(self,event:QtGui.QMouseEvent):
        print('rubberband')
        # self.origin = event.pos()
        # self.rubberBand.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
        # self.rubberBand.show()
        # self.rectChanged.emit(self.rubberBand.geometry())



