from AGraphWidget import AGraphNode, AUtil, AGraph
from AGraphWidget import AGraphPort, AGraphParam, AWidget, AGraphProperty, APropertyCombo
from AGraphWidget.AUtil import APropertyType, APropertyLocation
from yapsy.IPlugin import IPlugin
import threading



class APlugin(AGraphNode.AGraphNode):
    def __init__(self, x=0, y=0):
        AGraphNode.AGraphNode.__init__(self, node_id='', node_type=self.__class__.__name__, x=x, y=y)
        self.default_text = ''
        self.events = dict()
        self.is_starter = False
        self.run_in_thread = False
        self.thread = None

    def add_property_change_event(self, prop_id, func_name):
        self.events[prop_id] = func_name

    def change_event(self, prop_id):
        func = getattr(self, self.events[prop_id])
        func()

        pass

    def add_property_combobox(self, property_name, items):
        prop = AGraphProperty.AGraphProperty(property_id=property_name, property_type=APropertyType.COMBO,
                                             property_location=APropertyLocation.NODE, node=self)
        prop.gui.add_items(items)
        self.add_prop(prop)
        return prop

    def add_property_text(self, property_name, default_text):
        prop = AGraphProperty.AGraphProperty(property_name, APropertyType.TEXT, APropertyLocation.NODE, self)
        prop.gui.set_text(default_text)
        self.add_prop(prop)
        return prop

    def add_property_bool(self, property_name, default_state):
        prop = AGraphProperty.AGraphProperty(property_name, APropertyType.BOOL, APropertyLocation.NODE, self)
        prop.gui.set_state(default_state)
        self.add_prop(prop)

    def add_property_slider(self, property_name, default_value):
        prop = AGraphProperty.AGraphProperty(property_name, APropertyType.SLIDER, APropertyLocation.NODE, self)
        prop.gui.set_value(default_value)
        self.add_prop(prop)
        return prop

    def add_property_file(self, property_name, default_value):
        prop = AGraphProperty.AGraphProperty(property_name, APropertyType.FILE, APropertyLocation.NODE, self)
        prop.gui.set_file_path(default_value)
        self.add_prop(prop)
        return prop

    def add_property_image(self, property_name):
        prop = AGraphProperty.AGraphProperty(property_name, APropertyType.IMAGE, APropertyLocation.NODE, self)
        self.add_prop(prop)
        return prop

    def get_property_value(self, property_name):
        return self.props[property_name].value

    def set_in_param(self, param_name, val):
        self.params_in[param_name].value = val

    def get_in_param(self, param_name):
        return self.params_in[param_name].value

    def set_out_param(self, param_name, val):
        self.params_out[param_name].value = val

    def get_out_param(self, param_name):
        return self.params_out[param_name].value

    def add_in_port(self, port_name):
        self.add_port_in(port=AGraphPort.AGraphPort(port_name, AGraphPort.APortType.INPUT, self))

    def add_out_port(self, port_name):
        self.add_port_out(port=AGraphPort.AGraphPort(port_name, AGraphPort.APortType.OUTPUT, self))

    def add_in_param(self, param_name):
        self.add_param_in(param=AGraphParam.AGraphParam(param_name, AGraphParam.AParamType.INPUT, self))

    def add_out_param(self, param_name):
        self.add_param_out(param=AGraphParam.AGraphParam(param_name, AGraphParam.AParamType.OUTPUT, self))

    def set_position(self, x, y):
        self.gui.rect.setX(x)
        self.gui.rect.setY(y)
        self.gui.setX(x)
        self.gui.setY(y)

    def edit_run(self):
        self.update_output_shape()
        self.gui.node_info = ''
        for out in self.params_out.values():
            sh = out.shape
            if sh:
                self.gui.node_info += '('
                for i in range(len(sh)):
                    if i != 0:
                        self.gui.node_info += ','
                    self.gui.node_info += str(sh[i])
                self.gui.node_info += ')'

            for link in out.links.values():
                # link.end.value =
                link.end.node.edit_run()

    def run_main(self):
        print('run')
        if self.run_in_thread:
            self.thread = threading.Thread(target=self.exec)
            self.thread.start()
        else:
            self.exec()

        if self.thread:
            while self.thread.isAlive():
                pass




    def run(self):
        pass

    def init(self):
        print('init run')

    def exec(self):
        self.init()
        self.run()
        self.end()

    def end(self):
        print('end')

    def init_node(self):
        print('init_node: ' + self.node_id)
        # if self.prop

    def get_output_shape(self):
        if self.params_out['out']:
            return self.params_out['out'].value.shape
        return None

    def update_output_shape(self):
        pass

    def init_plugin(self):
        print("Init plugin " + self.node_type)
        # def print_name(self):
        #     print('parent')
        # self.awidget = awidget
        # node = self.awidget.add_node('teeeeest', 1000, 1000)
        # self.awidget.scene().addItem(self.gui)
        # self.category = 'pytorch'
        # port = AGraphPort('port_1', AUtil.APortType.INPUT, self)
        # self.add_port_in

        # def add_to_graph(self):
        #     self.awidget.add_full_node(self)
        #     self.awidget.scene().addItem(self.gui)
