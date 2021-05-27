#!/usr/bin/env python

from ete3 import Tree, TreeStyle, TextFace

t = Tree("((a,b),c);")

ts = TreeStyle()
ts.show_leaf_name = True

# the plain tree
t.render("18a_my_default_nodes.png", tree_style=ts)
# add text to
# the right of the root node
t.add_face(TextFace("hola "), column=0, position= "branch-right")
# the right of the root node, right next to the first annotation
t.add_face(TextFace("mundo! "), column=1, position= "branch-right")
t.render("18b_my_annotated_nodes.png", tree_style=ts)


