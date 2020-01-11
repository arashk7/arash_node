from PyQt5 import QtCore, QtGui, QtWidgets


class AKeyboardEvent:
    def __init__(self):
        print('init keyboard')

    def key_press_event(self, event):
        # if event == QtGui.QKeyEvent.KeyPress:
        # if event.modifiers() & QtCore.Qt.ControlModifier:
        #     if event.key() == QtCore.Qt.Key_C:
        #         print('sss')

        # if QtGui.QKeySequence(event.key() + int(event.modifiers())) == QtGui.QKeySequence("Ctrl+C"):
        #     print('ok')

        # if QtCore.Qt.QKeySequence(event.key()+int(event.modifiers())) == QtCore.Qt.QKeySequence("Ctrl+C"):
        #     print('The control + C is pressed')
        # if type(event) == QtCore.Qt.QKeyEvent.KeyPress:
        #     print('sss')
        # if event.key() == QtCore.Qt.QKeySequence.Copy:
        #     print('The control + V is pressed')

        # print('key_pressed')
        pass
