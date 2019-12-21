from ABaseGraph import ABaseGraph

g = ABaseGraph()
g.add_node('node_0')
g.add_node('node_1')
g.add_port_in('node_2')
g.add_port_in('node_0', 'p2')

# g.remove_node('node2')

print("")
