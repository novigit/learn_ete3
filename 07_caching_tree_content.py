#!/usr/bin/env python
from ete3 import Tree

t = Tree()
t.populate(50)
print(t)

#       /-aaaaaaaaan
#      /-|
#     |   \-aaaaaaaaao
#   /-|
#  |  |   /-aaaaaaaaap
#  |   \-|
#  |      \-aaaaaaaaaq
#  |
#  |         /-aaaaaaaaar
#  |      /-|
#  |     |   \-aaaaaaaaas
# .... etc .... etc ....

# .get_cached_content() returns a dictionary
# keys: nodes (the TreeNode object)
# values: contents of those nodes
# by default a list of leave nodes associated with the key node
# if you want to 'cache' another attribute, you can set a custom 'store_attr' value
node2leaves = t.get_cached_content()
# particularly useful if you need to access node content multiple times independently
# create one dictionary once, which is easily accessible
# instead of traversing the tree multiple times which slows down the script

# we can now traverse the tree only once and print for each node its corresponding leaves
for node in t.traverse():
    # print() can also take in printf -like syntax
    print("node %s contains %s tips" %(node.name, len(node2leaves[node])) ) 

# node  contains 50 tips
# node  contains 41 tips
# node  contains 9 tips
# node  contains 11 tips
# node  contains 30 tips
# node  contains 4 tips
# node  contains 5 tips
# node  contains 3 tips
# node  contains 8 tips
# node  contains 17 tips
# node  contains 13 tips
# node aaaaaaaaaa contains 1 tips
# node  contains 3 tips
# node  contains 2 tips
# node  contains 3 tips
# node aaaaaaaaaj contains 1 tips
# node  contains 2 tips
# node  contains 3 tips
# node  contains 5 tips
# node  contains 2 tips
# node  contains 15 tips
# ....  etc .... etc ...