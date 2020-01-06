#!/usr/bin/env python
from ete3 import Tree

t = Tree( "((H:3,I:1):0.5, A:1, (B:1,(C:1,D:1):0.5):0.5);", format=0)
print(t) # remember that print() does not print branch lengths, only topology
#       /-H
#    /-|
#   |   \-I
#   |
# --|--A
#   |
#   |   /-B
#    \-|
#      |   /-C
#       \-|
#          \-D

# search for node 'D'
# remember that .search_nodes returns a list! hence the [0] to get the first item on the list
D = t.search_nodes(name="D")[0]
print(D)

# search for all nodes with branch length 0.5
nodes = t.search_nodes(dist=0.5)
print(len(nodes), "nodes have distance=0.5")

# instead of searching all nodes, search only leaves (this is faster)
# also .get_leaves_by_name returns a list!
D = t.get_leaves_by_name(name="D")[0]
print(D)