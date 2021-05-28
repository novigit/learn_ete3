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

# face properties

t = Tree( "(a,b);" )
ts = TreeStyle()
ts.show_leaf_name = True

# create two face objects
hola = TextFace("hola")
mundo = TextFace("mundo")
# set hola face attributes
# margin is distance in px between text and edge of the border
hola.margin_top = 10
hola.margin_right = 10
hola.margin_left = 10
hola.margin_bottom = 10
hola.opacity = 0.5 # range is from 0 to 1
hola.inner_border.width = 1 # pixel border
hola.inner_border.type = 1 # dashed line
hola.border.width = 1
hola.background.color = "LightGreen"

t.add_face(hola, column=0, position="branch-top")
t.add_face(mundo, column=1, position="branch-bottom")

t.render("18c_my_face_attributes.png", tree_style=ts)