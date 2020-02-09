from PyQt5 import QtCore, QtGui, QtWidgets
import xml.etree.cElementTree as ET
from enum import Enum
from AGraphWidget.ALogger import ALogger


# Group Enumerator that demonstrate all the states of the different roles
class AGroup(Enum):
    DISABLED = 'Disabled'
    ACTIVE = 'Active'
    INACTIVE = 'Inactive'
    NORMAL = 'Normal'


# Role Enumerator
class ARole(Enum):
    BACKGROUND = 'Background'
    NODE_WND = 'NodeWindow'
    NODE_WND_CAP_BAR = 'NodeWindowCaptionBar'
    NODE_WND_CAP_TEXT = 'NodeWindowCaptionText'

    GRID = 'Grid'
    RUBBER_BAND = 'RubberBand'
    SELECT_HIGHLIGHT = 'SelectHighlight'


# This class gives us ability to define colors for different roles in different states.
# You will be able to save and load your custom skins.
class ASkin:
    # Palette is a dict which records color value for each tuple of (role, group)
    palette = dict()

    # Initialize all the colors in different states and save them as the default skin
    @staticmethod
    def init_default():
        ASkin.set_role_color(ARole.BACKGROUND, AGroup.NORMAL, QtGui.QColor(100, 100, 100))
        ASkin.set_role_color(ARole.GRID, AGroup.NORMAL, QtGui.QColor(70, 70, 70))
        ASkin.set_role_color(ARole.RUBBER_BAND, AGroup.NORMAL, QtGui.QColor(200, 200, 200, 80))
        ASkin.set_role_color(ARole.SELECT_HIGHLIGHT, AGroup.NORMAL, QtGui.QColor(160, 220, 255, 100))
        ASkin.set_role_color(ARole.NODE_WND, AGroup.NORMAL, QtGui.QColor(150, 150, 150, 150))
        ASkin.set_role_color(ARole.NODE_WND_CAP_BAR, AGroup.NORMAL, QtGui.QColor(20, 20, 20, 250))
        ASkin.set_role_color(ARole.NODE_WND_CAP_TEXT, AGroup.NORMAL, QtGui.QColor(200, 200, 200, 200))

        ASkin.save_skin()

    # Load default skin. generally this function would be called at the first stage of application.
    @staticmethod
    def load_default():
        ASkin.load_skin()

    # Save the skin file in /skins
    # It records all the roles and groups color
    @staticmethod
    def save_skin(skin_file_name='default.askin'):
        skin = ET.Element("skin")
        palette = ET.SubElement(skin, "palette")

        for r in ARole:
            role = ET.SubElement(palette, "role", name=r.value)
            for g in AGroup:

                if (r, g) in ASkin.palette:
                    c = ASkin.color(r, g)
                    ET.SubElement(role, "group", name=g.value).text = str(c.red()) + ',' + str(c.green()) + ',' + str(
                        c.blue()) + ',' + str(c.alpha())

        tree = ET.ElementTree(skin)
        tree.write('skins/' + skin_file_name)

    # Load a skin from the '/skins' directory.
    # If you call the function without parameter, it will import the 'default.askin'
    @staticmethod
    def load_skin(skin_file_name='default.askin'):
        skin = ET.parse('skins/' + skin_file_name).getroot()
        palette = skin[0]

        for role in palette:
            for group in role:
                rgbd_str = group.text.split(',')
                rgbd_int = list(map(int, rgbd_str))

                ASkin.set_role_color(ARole(role.attrib['name']), AGroup(group.attrib['name']),
                                     QtGui.QColor(rgbd_int[0], rgbd_int[1], rgbd_int[2], rgbd_int[3]))

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
        if (role, group) in ASkin.palette:
            color = ASkin.palette[(role, group)]
        else:
            ALogger.print_error('Skin Role or group not found! role=' + role + ' group=' + group)
            color = QtGui.QColor(0, 0, 0)
        return color
