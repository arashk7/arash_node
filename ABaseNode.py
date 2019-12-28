from ALogger import ALogger

class ABaseNode:
    def __init__(self, node_id):
        self._id = node_id
        self.__title = node_id
        self.__category = 'none'
        self.__params_in = {}
        self.__params_out = {}
        self.ports_in = {}
        self.ports_out = {}
        self.__num_params_in_created = 0
        self.__num_params_out_created = 0
        self.num_ports_in_created = 0
        self.num_ports_out_created = 0

    # Node ID
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, node_id):
        if len(node_id) < 3:
            ALogger.print_error('The length of id must be more than 3!')
            return
        else:
            self.__id = node_id
