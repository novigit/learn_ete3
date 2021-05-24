#!/usr/bin/env python
from ete3 import Tree

t =  Tree("((((((a, e), i), o),h), u), ((f, g), j));")
print(t)
#                   /-a
#                /-|
#             /-|   \-e
#            |  |
#          /-|   \-i
#         |  |
#       /-|   \-o
#      |  |
#    /-|   \-h
#   |  |
#   |   \-u
# --|
#   |      /-f
#   |   /-|
#    \-|   \-g
#      |
#       \-j

# check if all vowels are monophyletic, and if not, what their phyly is
print(t.check_monophyly(values=["a","e","i","o","u"], target_attr="name"))
## (False, 'polyphyletic', {Tree node 'h' (-0x7fffffffee25ea2a)})

# check if subset of vowels are monophyletic
print(t.check_monophyly(values=["a","e","i","o"], target_attr="name"))
## (True, 'monophyletic', set())

# these vowels are paraphyletic (a specific case of polyphyly)
print(t.check_monophyly(values=["i", "o"], target_attr="name"))
# (False, 'paraphyletic', {Tree node 'e' (0x117646a2), Tree node 'a' (0x1176469b)})


## .get_monophyletic
## returns a list of nodes that are monophyletic in a certain trait
## trait is usually defined as an attribute of the tree node
t =  Tree("((((((4, e), i), o),h), u), ((3, 4), (i, june)));")
print(t)
#                   /-4
#                /-|
#             /-|   \-e
#            |  |
#          /-|   \-i
#         |  |
#       /-|   \-o
#      |  |
#    /-|   \-h
#   |  |
#   |   \-u
# --|
#   |      /-3
#   |   /-|
#   |  |   \-4
#    \-|
#      |   /-i
#       \-|
#          \-june
# annotate the tree
# colors is a dictionary
colors = {
    "a":"red", 
    "e":"green", 
    "i":"yellow",
    "o":"black",
    "u":"purple",
    "4":"green",
    "3":"yellow", 
    "1":"white", "5":"red",
    "june":"yellow"
}
# .get() is a dictionary method that returns the value (the color) of the requested key (the leaf)
# the second argument of .get() states the value that should be returned ("None"), if the requested key (the leaf) is not found
# the for loop below adds a color to a leaf, leaf by leaf
for leaf in t:
    leaf.add_features(color=colors.get(leaf.name, "none"))
# just printing t doesnt show the features
print(t)
# requires the .get_ascii() method
print(t.get_ascii(attributes=["name", "color"], show_internal=False))
#                   /-4, green
#                /-|
#             /-|   \-e, green
#            |  |
#          /-|   \-i, yellow
#         |  |
#       /-|   \-o, black
#      |  |
#    /-|   \-h, none
#   |  |
#   |   \-u, purple
# --|
#   |      /-3, yellow
#   |   /-|
#   |  |   \-4, green
#    \-|
#      |   /-i, yellow
#       \-|
#          \-june, yellow

# find nodes that are monophyletic for containing either green or yellow
print("Green-yellow clusters:")
for node in t.get_monophyletic(values=["green","yellow"], target_attr="color"): 
    print(node.get_ascii(attributes=["color","name"], show_internal=False))
# Green-yellow clusters:

#       /-green, 4
#    /-|
# --|   \-green, e
#   |
#    \-yellow, i

#       /-yellow, 3
#    /-|
#   |   \-green, 4
# --|
#   |   /-yellow, i
#    \-|
#       \-yellow, june
