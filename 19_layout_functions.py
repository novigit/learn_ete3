#!/usr/bin/env python

from ete3 import Tree, TreeStyle, TextFace


t = Tree("((((a,b), c), d), e);")

def abc_layout(node):
    """
    Examply layout function
    If node is a vowel, draw it red with size 15
    The layout function is called when rendering or showing the tree
    """
    vowels = set(["a", "e", "i", "o", "u"])
    if node.name in vowels:
        node.img_style["size"] = 15
        node.img_style["fgcolor"] = "red"

ts = TreeStyle()
ts.show_leaf_name = True

t.add_face(TextFace("hola "), column=0, position="branch-right")
t.add_face(TextFace("mundo!"), column=1, position="branch-right")

t.render("19a_layout_function.png", tree_style=ts, layout=abc_layout)
# t.show(tree_style=ts, layout=abc_layout)