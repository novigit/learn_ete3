#!/usr/bin/env python

from ete3 import Tree


# Let's create simple tree
t = Tree('((((H,K),(F,I)G),E),((L,(N,Q)O),(P,S)));', format=1)
print("Original tree looks like this:")
print(t)
#             /-H
#          /-|
#         |   \-K
#       /-|
#      |  |   /-F
#    /-|   \-|
#   |  |      \-I
#   |  |
#   |   \-E
# --|
#   |      /-L
#   |   /-|
#   |  |  |   /-N
#   |  |   \-|
#    \-|      \-Q
#      |
#      |   /-P
#       \-|
#          \-S

# Prune the tree in order to keep only some leaf nodes.
# Pruning means to discard all nodes and associated branches except those
# that are requested
t.prune(["H","F","E","Q", "P"])
print("Pruned tree")
print(t)
#          /-H
#       /-|
#    /-|   \-F
#   |  |
# --|   \-E
#   |
#   |   /-Q
#    \-|
#       \-P