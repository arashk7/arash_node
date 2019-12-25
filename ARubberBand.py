from PyQt5 import QtCore, QtGui, QtWidgets
from ASkin import *


# Customized RobberBand
# it is implemented to use skin. In future it is going to have more functionality
class ARubberBand:
    def __init__(self, widget_parent, color):
        self.__rubber_band = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, widget_parent)
        self.parent = widget_parent
        # Initialize palette
        rubber_band_palette = QtGui.QPalette()
        rubber_band_brush = QtGui.QBrush(color)
        rubber_band_palette.setBrush(QtGui.QPalette.Highlight, rubber_band_brush)
        self.__rubber_band.setPalette(rubber_band_palette)
        # Store the drag position
        self.origin = QtCore.QPoint()
        # It will be True if we drag the mouse
        self.changeRubberBand = False

    def mouse_press_event(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            # Record the drag position
            self.origin = event.pos()
            self.__rubber_band.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
            self.__rubber_band.show()

            # Emit the rectangle in AWidget
            self.parent.rectChanged.emit(self.__rubber_band.geometry())

            self.changeRubberBand = True

    def mouse_release_event(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            self.__rubber_band.hide()

    def mouse_move_event(self, event: QtGui.QMouseEvent):
        if self.changeRubberBand:
            self.__rubber_band.setGeometry(QtCore.QRect(self.origin, event.pos()).normalized())

            # Emit the new rubber rectangle to AWidget
            self.parent.rectChanged.emit(self.__rubber_band.geometry())
            QtWidgets.QGraphicsView.mouseMoveEvent(self.parent, event)
