#!/usr/bin/env python
from ete3 import Tree

# every node contains 3 basic attributes:
## TreeNode.name - name
## TreeNode.dist - branch length
## TreeNode.support - branch support
# these are the three forms of information typically encoded in Newick format

# it is possible to add additional data to the node
# this is called tree or node annotation

# example
t = Tree( '((H:0.3,I:0.1):0.5, A:1, (B:0.4,(C:0.5,(J:1.3, (F:1.2, D:0.1):0.5):0.5):0.5):0.5);' )
print(t)
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
#         |   /-J
#          \-|
#            |   /-F
#             \-|
#                \-D

## Find a node using the .get_common_ancestor() method
ancestor=t.get_common_ancestor("J","F","C")
print(ancestor)
#    /-C
# --|
#   |   /-J
#    \-|
#      |   /-F
#       \-|
#          \-D
## Find a node using the .search_nodes() method
### Remember that search_nodes() returns a list
A = t.search_nodes(name="A")[0]
# print(A)
## Find some other nodes using the t&"C" shortcut
C = t&"C"
H = t&"H"
I = t&"I"

# Add custom features to the nodes. It can be whatever feature you wish
C.add_features(vowel=False, confidence=1.0, blergh="Wut")
A.add_features(vowel=True, confidence=0.5)
ancestor.add_features(nodetype="internal")
# print(C.vowel)
# print(C.confidence)
# print(C.blergh)
# Automate adding custom features to nodes
import random
for leaf in t.traverse():
    if leaf.name in "AEIOU": # apparently this returns True also for inner nodes with empty names
        leaf.add_features(vowel=True, confidence=random.random())
        print(leaf.name, "hahaha")
    else:
        leaf.add_features(vowel=False, confidence=random.random())
print(t.get_ascii(attributes=["name", "vowel", "confidence"], show_internal=False))
#       /-H, 0.20091802319217555
#    /-|
#   |   \-I, 0.2996038602077522
#   |
# --|--A, 0.7414957503097014
#   |
#   |   /-B, 0.11029596725406932
#    \-|
#      |   /-C, 0.8783581327234126
#       \-|
#         |   /-J, 0.22179947167849268
#          \-|
#            |   /-F, 0.725635503319019
#             \-|
#                \-D, 0.6518668962404354
print("This tree has", len(t.search_nodes(vowel=True)), "vowel nodes")
# print(t.search_nodes(vowel=True))
# the next line of code uses a 'list comprehension', which is a sort of easy to read syntax one liner that replaces a list statement and subsequent for loop
print("Which are", [leaf.name for leaf in t.iter_leaves() if leaf.vowel==True])

# detect leaf nodes under 'ancestor' with distance higher than 1
# note that .traverse() is used on 'ancestor', not on 't'.
# this means that only all nodes under ancestor are visited
matches = [leaf for leaf in ancestor.traverse() if leaf.dist>1.0]
# note that this again is a list comprehension

print(matches)
# confirming by looking at the tree
#ancestor.show()

# add matched nodes as information to ancestor node as a new attribute feature ("long_branch_nodes")
# make sure to use .add_feature(), not .add_features()!!
ancestor.add_feature("long_branch_nodes", matches)

# now check em
print("These are nodes under ancestor with long branches", [n.name for n in ancestor.long_branch_nodes])
# note that ancestor.long_branch_nodes returns a list of nodes

# we can also use the add_feature() method to dynamically add new features
label = input("custom_label:")
value = input("custom label value:")
ancestor.add_feature(label, value)
print("Ancestor has now the [", label, "] attribute with value [", value, "]")