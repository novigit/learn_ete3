#!/usr/bin/env python
from ete3 import Tree

# specify unrooted_tree, a Tree object
unrooted_tree = Tree( "(A,B,(C,D));" )
print(unrooted_tree)
#    /-A
#   |
# --|--B
#   |
#   |   /-C
#    \-|
#       \-D

# Even though this is an unrooted tree, in this context it still as a root node, as in the top-most node
# The root node represents the whole tree structure
# The root node of an unrooted tree has more than two children nodes

rooted_tree = Tree( "((A,B),(C,D));" )
print(rooted_tree)
#       /-A
#    /-|
#   |   \-B
# --|
#   |   /-C
#    \-|
#       \-D

# Here the root node has two children
