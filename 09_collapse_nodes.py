#!/usr/bin/env python

from ete3 import Tree

# custom function that takes a node as a first argument and returns True/False
# when is_leaf_fn=collapsed_leaf,
# the collapsed_leaf function is used to determine whether
# a node should be a leaf or not
# so, if you want to collapse a subtree at a certain node,
# you can set the criteria for determining which nodes should be 
# collapsed in the custom function
def collapsed_leaf(node):
    # node2labels[node] returns a set (?) of 
    # unique leaf names that are descendants of node
    # e.g. {'a', 'b'} for node 'ab'
    # so if ancestral node only has 1 unique leaf label
    # we want to collapse it (i.e. make it a leaf node)
    if len(node2labels[node]) == 1:
       return True
    # else if it has multiple unique leaf labels
    # we do not want to collapse it
    else:
       return False

# define toy tree with internal labels (internal nodes have names)
t = Tree("((((a,a,a)a,a)aa, (b,b)b)ab, (c, (d,d)d)cd);", format=1)
print(t)
#             /-a
#            |
#          /-|--a
#         |  |
#       /-|   \-a
#      |  |
#    /-|   \-a
#   |  |
#   |  |   /-b
# --|   \-|
#   |      \-b
#   |
#   |   /-c
#    \-|
#      |   /-d
#       \-|
#          \-d

# print tree showing internal labels
print(t.get_ascii(show_internal=True))
#             /-a
#            |
#          /a|--a
#         |  |
#       /aa   \-a
#      |  |
#    /ab   \-a
#   |  |
#   |  |   /-b
# --|   \b|
#   |      \-b
#   |
#   |   /-c
#    \cd
#      |   /-d
#       \d|
#          \-d

# create dictionary (a 'cache')
## keys   = node objects
## values = node names (node.name is a basic attribute)
##          of all unique leaf nodes descendant of node
node2labels = t.get_cached_content(store_attr="name")

# collapse tree via is_leaf_fn function
# all nodes that only have one unique descendant leaf label are collapsed
c = Tree( t.write(is_leaf_fn=collapsed_leaf) )
print(c.get_ascii(show_internal=True))
#       /-aa
#    /-|
#   |   \-b
# --|
#   |   /-c
#    \-|
#       \-d

# overview of node2labels dictionary
for node in node2labels:
    print(node, " ", node.name, " ", node2labels[node], " ", len(node2labels[node]))
# --a   a   {'a'}   1

# --a   a   {'a'}   1

# --a   a   {'a'}   1

#    /-a
#   |
# --|--a
#   |
#    \-a   a   {'a'}   1

# --a   a   {'a'}   1

#       /-a
#      |
#    /-|--a
#   |  |
# --|   \-a
#   |
#    \-a   aa   {'a'}   1

# --b   b   {'b'}   1

# --b   b   {'b'}   1

#    /-b
# --|
#    \-b   b   {'b'}   1
# etc etc