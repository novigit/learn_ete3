#!/usr/bin/env python
from ete3 import Tree

# load a tree
t = Tree('((((H,K)D,(F,I)G)B,E)A,((L,(N,Q)O)J,(P,S)M)C);', format=1)
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

# .traverse returns an 'iterator' (a list? an iterable object?) of the tree nodes in postorder
# 'postorder': traverse left subtree from leave to top, traverse right subtree from leave to top, visit the root
for node in t.traverse("postorder"):
    print(node.name)
# H
# K
# D
# F
# I
# G
# B
# E
# A
# L
# N
# Q
# O
# J
# P
# S
# M
# C
# 

# other traversal options:
# 'preorder' - visit the root, then left tree nodes, then right tree nodes
# 'levelorder' - default. every node is visited on a given level before dropping down one level

# traverse over the tree in postorder, but skip the root node
# the difference in output is one less empty line (this line represents the root node that did not have a name)
for node in t.iter_descendants("postorder"):
    print(node.name)
# H
# K
# D
# F
# I
# G
# B
# E
# A
# L
# N
# Q
# O
# J
# P
# S
# M
# C

t = Tree( "(A:1,(B:1,(C:1,D:1):0.5):0.5);" )
print(t)
# .search_nodes() returns a list of nodes that match a certain set of conditions (name, branch length etc)
# printing a specific leave node returns
# --C
print( t.search_nodes(name="C")[0] )

# traverse the tree node by node upwards from a desired specific node
node = t.search_nodes(name="C")[0]
while node:
    print(node)
    # node.up returns a pointer to the parent node
    node = node.up

