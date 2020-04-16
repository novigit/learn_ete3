#!/usr/bin/env python
from ete3 import Tree

# Loads a tree structure from a newick string.
# The returned variable ’t’ is the root node for the tree.
# 't' is a TreeNode object
# Tree() is an alias for TreeNode()
# which create TreeNode objects
t = Tree("(A:1,(B:1,(E:1,D:1):0.5):0.5);")
# This newick format includes leaf names and branch lengths
#    /-A
# --|
#   |   /-B
#    \-|
#      |   /-E
#       \-|
#          \-D


# Load a tree structure from a newick file.
t = Tree("rp56.nw")

# You can also specify the newick format.
# For instance, for named internal nodes we will use format 1.
# The default format is 0
# format 0 and 1 are 'flexible',
# meaning they will load even if they miss e.g., support values
# other formats are strict and will raise exceptions if the
# provided tree does not strictly adhere to the requested format
t = Tree("(A:1,(B:1,(E:1,D:1)Internal_1:0.5)Internal_2:0.5)Root;", format=1)
#    /-A
# --|
#   |   /-B
#    \-|
#      |   /-E
#       \-|
#          \-D
# Apparently does not print internal node names though..

# ETE3 toolkit specificies several types of newick format types,
# see their documentation
