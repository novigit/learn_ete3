#!/usr/bin/env python
from ete3 import Tree

t = Tree()
t.populate(50)
print(t)

# .get_cached_content() returns a dictionary
# keys: nodes
# values: list of leave nodes associated with key node
node2leaves = t.get_cached_content()

# we can now traverse the tree only once and print for each node its corresponding leaves
for node in t.traverse():
    print("node %s contains %s tips" %(node.name, len(node2leaves[node])) ) 