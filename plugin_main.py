from pluginmanager import PluginInterface

plugin_interface = PluginInterface()
plugin_interface.set_plugin_directories('plugins')
plugin_interface.collect_plugins() # doctest: +SKIP

plugins = plugin_interface.get_instances()
print(plugins)