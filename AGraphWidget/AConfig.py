from PyQt5 import QtCore, QtGui, QtWidgets

class AConfig:


    font = QtGui.QFont()

    def init_font(self):
        font = QtGui.QFont()
        font.setFamily(QtCore.fromUtf8._fromUtf8("FreeMono"))
        font.setBold(True)
