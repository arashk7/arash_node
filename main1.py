from ABaseGraph import ABaseGraph
from ABaseNode import ABaseNode

# print('\x1b[6;30;42m' + 'Success!' + '\x1b[0m')

g = ABaseGraph()
g.add_node('node_0')
g.add_node('node_1')
g.add_port_in('node_2')
g.add_port_in('node_0','p2')


# g.remove_node('node2')

print("")
