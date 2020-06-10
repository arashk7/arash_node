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

        for pl in plg_cats:
            self.manager = PluginManager()
            self.manager.setPluginPlaces([pl])
            self.manager.collectPlugins()
            cat = pl.split('/')[1]
            print(cat)
            # Loop round the plugins and add them to item list
            for plugin in self.manager.getAllPlugins():
                # print(plugin.plugin_object.node_id)
                plugin.plugin_object.init_plugin()
                plugin.plugin_object.category = cat
                self.items.append(plugin.plugin_object)


        # # Loop round the plugins and print their names.
        # for plugin in self.manager.getAllPlugins():
        #     plugin.plugin_object.init_plugin()
        #     # print(plugin.path)
        #     plugin.category='test'
        #     print(plugin.category)
        #     self.items.append(plugin.plugin_object)

            # print(len(self.items))

    def inset_to_widget(self, item, x, y):

        new_item = (type(item))(x, y)

        node = self.awidget.add_full_node(new_item)
        node.init_node()
        if node.is_starter:
            print('starter')
        if node.gui:
            self.awidget.scene().addItem(node.gui)

        # node= APlugin(self.awidget,'ttttt',1000,1000)

        # AConfig.awidget.add_node('nnnnnnnnn',1000,1000)
