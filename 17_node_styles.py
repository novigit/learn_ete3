#!/usr/bin/env python

from ete3 import Tree, NodeStyle, TreeStyle

t = Tree( "((a,b),c);" )

# basic tree style
ts = TreeStyle()
ts.show_leaf_name = True

# draw nodes as small red spheres, diameter 10 px
## create NodeStyle() dictionary
nstyle = NodeStyle()
## define nodestyle
nstyle["shape"] = "sphere"
nstyle["size"] = 10
nstyle["fgcolor"] = "darkred"
## nodestyle also controls branch style
## define branch style
nstyle["hz_line_type"] = 1
nstyle["hz_line_color"] = "#cccccc"

# apply style to all nodes in tree
for n in t.traverse():
    n.set_style(nstyle)

t.render("17a_my_redsphere_nodes_tree.png", tree_style=ts)


# create independent node styles for each node,
# which is initialized with red foreground color
t = Tree( "((a,b),c);" )

# basic tree style
ts = TreeStyle()
ts.show_leaf_name = True

# first set all nodes to red flat circle
for n in t.traverse():
    nstyle = NodeStyle()
    nstyle["fgcolor"] = "red"
    nstyle["size"] = 15
    n.set_style(nstyle)
# then modify the root node only
t.img_style["size"] = 30 # t is the tree, but by definition also the root node
t.img_style["fgcolor"] = "blue"
# so, you can adjust the style of a particular node by
# 1. defining a style in a NodeStyle oject and then apply it via n.set_style(nstyle)
# 2. define a style property directoy via n.img_style["property"] = "value"

t.render("17b_my_independent_nodes_tree.png", tree_style=ts)

