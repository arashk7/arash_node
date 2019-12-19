from ABasePort import ABasePort


class ABaseNode:
    def __init__(self, node_id):
        self.__id = node_id
        self.__title = node_id
        self.__category = 'none'
        self.__params_in = {}
        self.__params_out = {}
        self._ports_in = {}
        self._ports_out = {}
        self.__num_params_in = 0
        self.__num_params_out = 0
        self.__num_ports_in = 0
        self.__num_ports_out = 0

    # Node ID
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, node_id):
        if len(node_id) < 3:
            print('The length of id must be more than 3!')
            return
        else:
            self.__id = node_id

    # Add Input Port
    # def add_port_in(self, port_id):
    #     self.__num_ports_in = self.__num_ports_in + 1
    #     new_port = ABasePort(anc_id)
    #     self.__ports_in[port_id] = new_port
