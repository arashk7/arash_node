from AGraphWidget import AGraphNode, AUtil, AGraph
from AGraphWidget import AGraphPort, AGraphParam, AWidget
from AGraphWidget.AUtil import ASharedItems


class APlugin(AGraphNode.AGraphNode):
    def __init__(self, x=0, y=0):
        AGraphNode.AGraphNode.__init__(self, node_id='', node_type=self.__class__.__name__, x=x, y=y)

    def set_in_param(self, param_name, val):
        self.params_in[param_name].value = val

    def set_out_param(self, param_name, val):
        self.params_out[param_name].value = val

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

    def run(self):
        print('run')
        pass

    def init_node(self):
        print('init_node: ' + self.node_id)
        pass

    def get_output_shape(self):
        if self.params_out['out']:
            return self.params_out['out'].value.shape
        return None

    def update_output_shape(self):
        pass


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
