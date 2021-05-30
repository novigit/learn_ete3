#!/usr/bin/env python

from ete3 import Tree


t = Tree("((A, B)Internal_1:0.7, (C, D)Internal_2:0.5)root:1.3;", format=1)
print(t.get_ascii(show_internal=True))
#               /-A
#     /Internal_1
#    |          \-B
# -root
#    |          /-C
#     \Internal_2
#               \-D

# we add a custom annotation to the node named A
(t&"A").add_features(label="custom Value")
print(t.get_ascii(show_internal=True, attributes=["name", "label"]))

#               /-A, custom Value
#     /Internal_1
#    |          \-B
# -root
#    |          /-C
#     \Internal_2
#               \-D

# we add a complex feature to the A node, consisting of a list of lists
(t&"A").add_features(complex=[[0,1], [2,3], [1,11], [1,0]])
print(t.get_ascii(show_internal=True, attributes=["name", "dist", "label", "complex"]))
#                         /-A, 1.0, custom Value, [[0, 1], [2, 3], [1, 11], [1, 0]]
#          /Internal_1, 0.7
#         |               \-B, 1.0
# -root, 1.3
#         |               /-C, 1.0
#          \Internal_2, 0.5
#                         \-D, 1.0

# Newick copy will lose custom node annotations, complex features,
# ond will only keep node names, branch lengths and branch support values (not included in this example)
print(t.copy("newick").get_ascii(attributes=["name", "dist", "label", "complex"]))
#                         /-A, 1.0
#          /Internal_1, 0.7
#         |               \-B, 1.0
# -root, 1.3
#         |               /-C, 1.0
#          \Internal_2, 0.5
#                         \-D, 1.0

# Extended Newick copy will transfer custom annotations as text strings,
# so complex features are lost (or get misinterpreted ?)
# keeps node names, branch lengths, branch supports and simple custom annotations
print(t.copy("newick-extended").get_ascii(attributes=["name", "dist", "label", "complex"]))
#                     /-A, 1.0, custom Value, _0_ 1_|_2_ 3_|_1_ 11_|_1_ 0_
#      /Internal_1, 0.7
#     |               \-B, 1.0
# -, 0.0
#     |               /-C, 1.0
#      \Internal_2, 0.5
#                     \-D, 1.0

# The default pickle method will produce a exact clone of the
# original tree, where features are duplicated keeping their
# python data type.
print(t.copy("cpickle").get_ascii(attributes=["name", "dist", "label", "complex"]))
#                         /-A, 1.0, custom Value, [[0, 1], [2, 3], [1, 11], [1, 0]]
#          /Internal_1, 0.7
#         |               \-B, 1.0
# -root, 1.3
#         |               /-C, 1.0
#          \Internal_2, 0.5
#                         \-D, 1.0
print("first element in complex feature:", (t&"A").complex[0])
# first element in complex feature: [0, 1]