import pluginmanager


class MyCustomPlugin(pluginmanager.IPlugin):
    def __init__(self):
        self.name = 'custom_name'
        super().__init__()
        self.category = 'PyTorch'
        self.subcategory = 'Convolution'
    def print(self):
        print('salam')
