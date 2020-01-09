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
# remember that .search_nodes() returns a list! hence the [0] to get the first item on the list
D = t.search_nodes(name="D")[0]
print(D)

# search for all nodes with branch length 0.5
nodes = t.search_nodes(dist=0.5)
print(len(nodes), "nodes have distance=0.5")

# instead of searching all nodes, search only leaves (this is faster)
# also .get_leaves_by_name returns a list!
D = t.get_leaves_by_name(name="D")[0]
print(D)

## you can also create your own search function
# for when .search_nodes method is not complex search conditions enough
def search_by_size(node,size):
    "Finds nodes with a given number of leaves"
    
    # create an empty list
    matches = []

    # fill list with nodes that fullfill the criteria of having <size> number of leaves
    for n in node.traverse():
        if len(n) == size:
            print("Found one!")
            matches.append(n)
    return matches

# apply function on random tree
t = Tree()
# names_library only names leaves?
t.populate(40, names_library=["A","B","C","D"], reuse_names=True)
print(t)
print( t.write(format=1) )
# search_by_size() thus returns a list of TreeNode objects that fullfill the set criteria
matches = search_by_size(t, size=4)
# view the nodes by printing their corresponding subtrees
for node in matches:
    print(node)

## Find the last common ancestor of a set of nodes
t = Tree( "((H:0.3,I:0.1):0.5, A:1, (B:0.4,(C:0.5,(J:1.3, (F:1.2, D:0.1):0.5):0.5):0.5):0.5);" )
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
lca = t.get_common_ancestor("C","J","B")
# remember that lca is a TreeNode object, so printing it returns the entire subtree
print(lca)

## another way to search for particular nodes is to combine the python filter() function with the .traverse method:
t = Tree("((H:0.3,I:0.1):0.5, A:1, (B:0.4,(C:1,D:1):0.5):0.5);")

# print branch lengths
for node in t.traverse():
    print(node.name, node.dist)
print("====\n")
#  0.0
#  0.5
# A 1.0
#  0.5
# H 0.3
# I 0.1
# B 0.4
#  0.5
# C 1.0
# D 1.0
# ====

def is_long_branch(node):
    if node.dist > 0.6:
        return True
    else:
        return False

# filter() applies a True/False function to all elements in a specified iterable object,
# and returns only the True items in a 'filter object', which is an iterator
matches = filter(is_long_branch, t.traverse())

# to find the length you need to iterate over the filter object
# you can do this apparently with the list() function
print(len(list(matches)), "nodes have branches with length > 0.3")

## Finding TreeNode objects by their name is so common that ETE3 implements a shortcut: TreeNODE&NodeName
t = Tree("((H:0.3,I:0.1):0.5, A:1, (B:0.4,(C:1,(J:1, (F:1, D:1):0.5):0.5):0.5):0.5);")
# returns the first TreeNode whose name is "D"
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

D = t&"D"
print(D)

# store parent nodes of D in 'paths'
node = D
path = []
while node.up:
    path.append(node)
    node = node.up
print(path)

# Substract D node from the total number of visited nodes
# .up method goes all the way until the root node
print("There are", len(path)-1, "nodes between D and the root")

# Find specific nodes relative to a node of interest
Dsparent = (t&"D").up
Bsparent = (t&"B").up
Jsparent = (t&"J").up
print(Dsparent)
#    /-F
# --|
#    \-D
print(Bsparent)
#    /-B
# --|
#   |   /-C
#    \-|
#      |   /-J
#       \-|
#         |   /-F
#          \-|
#             \-D
print(Jsparent)
#    /-J
# --|
#   |   /-F
#    \-|
#       \-D
# Remember that any TreeNode represents itself and all of its children
# or in ETE3 terms, any tree can be represented by its root node

# You can check whether one node is inside a tree of another node
# nodeA in nodeB returns True or False
print("It is", Dsparent in Bsparent, "that D's parent is under B's parent")
print("It is", Dsparent in Jsparent, "that D's parent is under J's parent")
