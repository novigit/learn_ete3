#!/usr/bin/env python

from ete3 import Tree

# Loads a tree with branch lenght information. Note that if no
# distance info is provided in the newick, it will be initialized with
# the default dist value = 1.0
nw = """(((A:0.1, B:0.01):0.001, C:0.0001):1.0,
(((((D:0.00001,I:0):0,F:0):0,G:0):0,H:0):0,
E:0.000001):0.0000001):2.0;"""
t = Tree(nw)
print(t)
#          /-A
#       /-|
#    /-|   \-B
#   |  |
#   |   \-C
#   |
#   |               /-D
#   |            /-|
# --|         /-|   \-I
#   |        |  |
#   |      /-|   \-F
#   |     |  |
#   |   /-|   \-G
#   |  |  |
#    \-|   \-H
#      |
#       \-E
# for some reason print(t) does not print branch lengths

# Locate some nodes
A = t&"A"
C = t&"C"
# Calculate distance from current node
print("The distance between A and C is",  A.get_distance("C"))
# Calculate distance between two descendants of current node
print("The distance between A and C is",  t.get_distance("A","C"))
# Calculate the toplogical distance (number of nodes in between)
print("The number of nodes between A and D is ",  \
    t.get_distance("A","D", topology_only=True))

# Calculate the farthest node from E within the whole structure
# farthest in terms of cumulative branch lengths
farthest, dist = (t&"E").get_farthest_node()
print("The farthest node from E is", farthest.name, "with dist =", dist)

# Calculate the farthest node from E within the whole structure,
# farthest in terms of number of nodes away
# Note that the result is different.
farthest, dist = (t&"E").get_farthest_node(topology_only=True)
print("The farthest (topologically) node from E is", \
    farthest.name, "with", dist, "nodes in between")

# Calculate farthest node from the root node
farthest, dist = t.get_farthest_node()
print("The farthest node from root is", farthest.name, "with dist=", dist)