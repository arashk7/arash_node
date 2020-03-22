from yapsy.PluginManager import PluginManager
import os


class APluginManager:
    def __init__(self, awidget):
        # Load the plugins from the plugin directory.
        self.manager = PluginManager()
        self.awidget = awidget
        self.items = list()

    def load_dir(self, directory='plugins'):
        # make a list of plugin categories
        plg_cats = []
        dir_items = os.listdir(directory)
        for item in dir_items:
            path = directory + '/'+item
            if os.path.isdir(path) == True:
                if item[0] != '_':
                    plg_cats.append(path)

        self.manager.setPluginPlaces(plg_cats)
        self.manager.collectPlugins()

        # Loop round the plugins and print their names.
        for plugin in self.manager.getAllPlugins():
            plugin.plugin_object.init_plugin()
            # print(plugin.path)
            # print(plugin.cat)
            self.items.append(plugin.plugin_object)

            # print(len(self.items))

    def inset_to_widget(self, item, x, y):

        new_item = (type(item))(x, y)

        node = self.awidget.add_full_node(new_item)
        node.init_node()
        self.awidget.scene().addItem(node.gui)

        # node= APlugin(self.awidget,'ttttt',1000,1000)

        # AConfig.awidget.add_node('nnnnnnnnn',1000,1000)
