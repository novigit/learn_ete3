#!/usr/bin/env python

from ete3 import Tree

# all trees in ete3, whether conceptually rooted or unrooted, have a root node
# a tree is considered rooted if the root node has two daughter branches
# a tree is considered unrooted if the root node has more than two daughter branches

t = Tree('(A,(H,F),(B,(E,D)));')
print("Unrooted tree")
print(t)
#    /-A
#   |
#   |   /-H
# --|--|
#   |   \-F
#   |
#   |   /-B
#    \-|
#      |   /-E
#       \-|
#          \-D

# Let's define that the ancestor of E and D as the tree outgroup.  Of
# course, the definition of an outgroup will depend on user criteria.
outgroup_node = t.get_common_ancestor("E","D")
t.set_outgroup(outgroup_node)
print("Tree rooted at E and D's ancestor is more basal that the others.")
print(t)
#       /-E
#    /-|
#   |   \-D
# --|
#   |   /-B
#    \-|
#      |   /-A
#       \-|
#         |   /-H
#          \-|
#             \-F

# Set node A as the outgroup
t.set_outgroup( t&"A" )
print("Tree rooted at a terminal node")
print(t)
#    /-A
#   |
# --|      /-H
#   |   /-|
#   |  |   \-F
#    \-|
#      |   /-B
#       \-|
#         |   /-E
#          \-|
#             \-D

# MIDPOINT ROOTING

t = Tree()
t.populate(15)
print(t)
#          /-aaaaaaaaaj
#       /-|
#      |   \-aaaaaaaaak
#      |
#    /-|      /-aaaaaaaaal
#   |  |   /-|
#   |  |  |   \-aaaaaaaaam
#   |   \-|
#   |     |   /-aaaaaaaaan
#   |      \-|
# --|         \-aaaaaaaaao
#   |
#   |      /-aaaaaaaaaa
#   |   /-|
#   |  |   \-aaaaaaaaab
#   |  |
#   |  |      /-aaaaaaaaac
#    \-|   /-|
#      |  |  |   /-aaaaaaaaad
#      |  |   \-|
#      |  |     |   /-aaaaaaaaae
#      |  |      \-|
#       \-|        |   /-aaaaaaaaaf
#         |         \-|
#         |            \-aaaaaaaaag
#         |
#         |   /-aaaaaaaaah
#          \-|
#             \-aaaaaaaaai

# calculate the midpoint node
midpoint_node = t.get_midpoint_outgroup()
# set it as outgroup
t.set_outgroup(midpoint_node)
print(t)
#          /-aaaaaaaaac
#       /-|
#      |  |   /-aaaaaaaaad
#      |   \-|
#      |     |   /-aaaaaaaaae
#      |      \-|
#    /-|        |   /-aaaaaaaaaf
#   |  |         \-|
#   |  |            \-aaaaaaaaag
#   |  |
#   |  |   /-aaaaaaaaah
#   |   \-|
# --|      \-aaaaaaaaai
#   |
#   |      /-aaaaaaaaaa
#   |   /-|
#   |  |   \-aaaaaaaaab
#   |  |
#    \-|      /-aaaaaaaaaj
#      |   /-|
#      |  |   \-aaaaaaaaak
#      |  |
#       \-|      /-aaaaaaaaal
#         |   /-|
#         |  |   \-aaaaaaaaam
#          \-|
#            |   /-aaaaaaaaan
#             \-|
#                \-aaaaaaaaao

