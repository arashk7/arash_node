

class AGraphPort:
    def __init__(self, port_id):
        self.__id = port_id

    # Port ID
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, port_id):
        self.__id = port_id



