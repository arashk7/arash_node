from pluginmanager import PluginInterface


class AToolManager:
    def __init__(self):
        self.plugin_interface = PluginInterface()

    def load_dir(self, directory='plugins'):
        self.plugin_interface.set_plugin_directories(directory)
        self.plugin_interface.collect_plugins()

        plugins = self.plugin_interface.get_instances()
        print(len(plugins))
