from PyQt5 import QtCore, QtGui, QtWidgets


# Group Enumerator that demonstrate all the states of the different roles
class AGroup:
    DISABLED = 'Disabled'
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    NORMAL = 'Normal'


# Role Enumerator
class ARole:
    BACKGROUND = 'Background'
    NODE_WND = 'NodeWindow'
    NODE_WND_CAP = 'NodeWindowCaption'
    GRID = 'Grid'


class ASkin:
    # Palette is a dict which records color value for each tuple of (role, group)
    palette = dict()

    @staticmethod
    def init_default():
        ASkin.set_role_color(ARole.BACKGROUND, AGroup.NORMAL, QtGui.QColor(100, 100, 100))
        ASkin.set_role_color(ARole.GRID, AGroup.NORMAL, QtGui.QColor(70, 100, 100))

    # Set color for each role in normal state(group)
    @staticmethod
    def set_role_color(role, color=QtGui.QColor(0, 0, 0)):
        ASkin.palette[(role, AGroup.NORMAL)] = color

    # Set color for each role in their different states(groups)
    @staticmethod
    def set_role_color(role, group, color=QtGui.QColor(0, 0, 0)):
        ASkin.palette[(role, group)] = color

    # Get color from the static palette
    @staticmethod
    def color(role, group=AGroup.NORMAL):
        return ASkin.palette[(role, group)]
