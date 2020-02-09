from PyQt5 import QtCore, QtGui, QtWidgets
from ArashWidget.ASkin import *


# Customized RobberBand
# it is implemented to use skin. In future it is going to have more functionality
class ARubberBand:
    def __init__(self, widget_parent):
        self.__rubber_band = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle, widget_parent)
        self.__parent = widget_parent
        # Initialize palette
        rubber_band_palette = QtGui.QPalette()
        rubber_band_brush = QtGui.QBrush(ASkin.color(ARole.RUBBER_BAND))
        rubber_band_palette.setBrush(QtGui.QPalette.Highlight, rubber_band_brush)
        self.__rubber_band.setPalette(rubber_band_palette)
        # Store the drag position
        self.__origin = QtCore.QPoint()
        # It will be True if we drag the mouse
        self.__change_rubber_band = False

    def get_rect(self):
        return self.__rubber_band.geometry()

    def mouse_press_event(self, widget: QtWidgets.QGraphicsView, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            node = widget.itemAt(event.pos())
            if not node or node.data(0) == 'grid' or node.data(0) == 'link':

                # Record the drag position
                self.__origin = event.pos()
                self.__rubber_band.setGeometry(QtCore.QRect(self.__origin, QtCore.QSize()))
                self.__rubber_band.show()

                # Emit the rectangle in AWidget
                self.__parent.rectChanged.emit(self.__rubber_band.geometry())

                self.__change_rubber_band = True
            else:
                self.__change_rubber_band = False



    def mouse_release_event(self, event: QtGui.QMouseEvent):
        if event.button() == QtCore.Qt.LeftButton:
            self.__rubber_band.hide()

    def mouse_move_event(self, event: QtGui.QMouseEvent):
        if self.__change_rubber_band:
            self.__rubber_band.setGeometry(QtCore.QRect(self.__origin, event.pos()).normalized())

            # Emit the new rubber rectangle to AWidget
            self.__parent.rectChanged.emit(self.__rubber_band.geometry())
