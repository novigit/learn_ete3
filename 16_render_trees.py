#!/usr/bin/env python

from ete3 import Tree, TreeStyle

t = Tree("((a,b),c);")
# if you do not specify width, height and units, it will default to A4
t.render("16a_my_rendered_tree.png", w=183, units="mm")

# render tree in circular style
## create TreeStyle object
circular_style = TreeStyle()
## specify style parameters
circular_style.mode = "c"
circular_style.scale = 20
## pass on style to render()
t.render("16b_my_circular_tree.png", w=183, units="mm", tree_style=circular_style)

# render tree with
## Leaf names
## Branch length
## Branch support
t = Tree()
t.populate(10, random_branches=True)
## create TreeStyle object
ts = TreeStyle()
## specify style parameters
ts.show_leaf_name = True
ts.show_branch_length = True
ts.show_branch_support = True
t.render("16c_my_annotated_tree.png", h=200, units="mm", tree_style=ts)
## branch lengths on top of the branch
## branch supports on the bottom of the branch

# change the scale of the branch lengths
# scale defined in number of pixels per branch length unit
ts.scale = 600
t.render("16d_my_x_scaled_tree.png", h=200, units="mm", tree_style=ts)

# more vertical space between nodes 
# space defined in number of pixels
ts.branch_vertical_margin = 100
t.render("16e_my_y_scaled_tree.png", tree_style=ts)

# circular tree in 180 degrees
t = Tree()
t.populate(38)
# create TreeStyle object
ts = TreeStyle()
# define tree style parameters
ts.show_leaf_name = True
ts.mode = "c" # circular mode
ts.arc_start = -180 # 0 degrees starts at 3 oclock
ts.arc_span = 180
t.render("16f_my_arced_tree.png", tree_style=ts)

# add title to tree
from ete3 import Tree, TreeStyle, TextFace
t = Tree("((a,b),c);")
ts = TreeStyle()
ts.show_leaf_name = True
ts.title.add_face(TextFace("Hello ETE", fsize=20), column=0)
t.render("16g_my_titled_tree.png", tree_style=ts)
