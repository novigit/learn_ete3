#!/usr/bin/env python
from ete3 import Tree
import pdb
# Create a random tree object with random topology t
# the t tree object is represented by its root node
# t is an object of the Tree or TreeNode class
t = Tree()
t.populate(15)
# print tree t in ascii characters
# print only prints the topology, not the branch lengths
print(t)
#         /-aaaaaaaaak
#       /-|
#      |  |   /-aaaaaaaaal
#      |   \-|
#      |     |   /-aaaaaaaaam
#    /-|      \-|
#   |  |        |   /-aaaaaaaaan
#   |  |         \-|
#   |  |            \-aaaaaaaaao
#   |  |
#   |   \-aaaaaaaaaa
# --|
#   |      /-aaaaaaaaab
#   |   /-|
#   |  |  |   /-aaaaaaaaac
#   |  |   \-|
#   |  |     |   /-aaaaaaaaad
#   |  |      \-|
#    \-|        |   /-aaaaaaaaae
#      |         \-|
#      |            \-aaaaaaaaaf
#      |
#      |   /-aaaaaaaaag
#       \-|
#         |   /-aaaaaaaaah
#          \-|
#            |   /-aaaaaaaaai
#             \-|
#                \-aaaaaaaaaj

# print list of children nodes (2 children of the root node)
# ? actually a list of hash references?
print(t.children)
pdb.set_trace()
# prints subtree associated with the first child node
print(t.children[0])
# prints subtree associated with the second child node
print(t.children[1])

# returns the same as t.children
print(t.get_children())

# .up returns a pointer to the parents node.
# since the root node doesn't have a parent node, it returns None
print(t.up)

# .name returns a custom node's name, including leaves names
# in this case no custom node name was specified so it doesnt return anything
print(t.name)

# .dist returns the branch length from the node to its parent
# since its the root node it doesnt have a parent,
# so it returns the default value (1.0)
print(t.dist)

# .is_leaf() returns True when TreeNode object t is a leaf,
# False when it is an internal node
print(t.is_leaf())

# .get_tree_root returns the root of tree that the TreeNode object is in
# in this case it returns the same node,
# since the considered TreeNode object is already the root
# the print statement then prints the tree again in ascii characters
print(t.get_tree_root())

# .get_tree_root() applied on the TreeNode
# t.children[0] returns the root of entire tree t
print(t.children[0].get_tree_root())

# also this returns the root of the entire tree t
print(t.children[0].children[0].get_tree_root())

# iterate over tree leaves
for leaf in t:
    print(leaf.name)
