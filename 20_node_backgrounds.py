#!/usr/bin/env python

from ete3 import Tree, TreeStyle, NodeStyle, AttrFace, faces

t = Tree("((((a1,a2),a3), ((b1,b2),(b3,b4))), ((c1,c2),c3));")
# print(t)
#             /-a1
#          /-|
#       /-|   \-a2
#      |  |
#      |   \-a3
#    /-|
#   |  |      /-b1
#   |  |   /-|
#   |  |  |   \-b2
#   |   \-|
# --|     |   /-b3
#   |      \-|
#   |         \-b4
#   |
#   |      /-c1
#   |   /-|
#    \-|   \-c2
#      |
#       \-c3

# set circular treestyle
ts = TreeStyle()
# suppress leaf names
## leaf names are replaced by TextFaces (see below)
ts.show_leaf_name = False
ts.mode = "c"
# how much the center of the tree should be 'opened up'
ts.root_opening_factor = 0.25
# if leaf names are aligned, draw dotted guide lines 
ts.draw_guiding_lines = True


# set background colors in NodeStyle objects
stblue = NodeStyle()
stblue["bgcolor"] = "LightSteelBlue"
stmocc = NodeStyle()
stmocc["bgcolor"] = "Moccasin"
stkhaki = NodeStyle()
stkhaki["bgcolor"] = "Khaki"
stgreen = NodeStyle()
stgreen["bgcolor"] = "DarkSeaGreen"

# assign background colors to ancestral nodes
a  = t.get_common_ancestor("a1","a2","a3")
b  = t.get_common_ancestor("b1","b2","b3","b4")
bs = t.get_common_ancestor("b3","b4")
c  = t.get_common_ancestor("c1","c2","c3")
a.set_style(stblue)
b.set_style(stmocc)
bs.set_style(stkhaki)
c.set_style(stgreen)

# define layout function that
def layout_fn(node):
    """
    Leaf nodes will show TextFaces instead of leaf names
    These TextFaces will get their text from the node.name attribute
    and will have large font size
    """
    if node.is_leaf():
        # AttrFace() creates a TextFace instance from which the value
        # of the text is extracted from the .name attribute
        leaf_face = AttrFace(attr="name", fsize=30)
        # I have no idea what the faces object means
        faces.add_face_to_node(face=leaf_face, node=node, column=0, position="aligned")

t.render("20a_background_colors.png",tree_style=ts, layout=layout_fn)