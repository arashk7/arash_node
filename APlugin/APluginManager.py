from yapsy.PluginManager import PluginManager
# from APlugin import APlugin
from AGraphWidget.APlugin import APlugin


class APluginManager:
    def __init__(self, awidget):
        # Load the plugins from the plugin directory.
        self.manager = PluginManager()
        self.awidget = awidget
        self.items = list()

    def load_dir(self, directory='plugins'):
        self.manager.setPluginPlaces(["plugins"])
        self.manager.collectPlugins()

        # Loop round the plugins and print their names.
        for plugin in self.manager.getAllPlugins():
            plugin.plugin_object.init_plugin()
            self.items.append(plugin.plugin_object)
            # print(len(self.items))

    def inset_to_widget(self, item):
        new_item = (type(item))()
        node = self.awidget.add_full_node(new_item)
        node.init_node()
        self.awidget.scene().addItem(node.gui)

        # node= APlugin(self.awidget,'ttttt',1000,1000)

        # AConfig.awidget.add_node('nnnnnnnnn',1000,1000)
