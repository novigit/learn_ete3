#!/usr/bin/env python

from ete3 import Tree, TreeStyle, TextFace, NodeStyle, AttrFace, faces
import csv

# load tree
t = Tree("rp56.nw")

# set TreeStyle
ts = TreeStyle()
ts.show_leaf_name = False
ts.show_branch_support = True
ts.title.add_face(TextFace("Tree Title", fsize=20), column=0)


# Suppress nodes
# and increase line width
ns = NodeStyle()
ns["size"] = 0
ns["hz_line_width"] = 1
ns["vt_line_width"] = 1
for node in t.traverse():
    node.set_style(node_style=ns)


# Load mapping file
## taxon - clade - color
with open("scratch.map", "r") as m:
    map = {}
    for taxon, clade, color in csv.reader(m, delimiter='\t'):
        map[taxon] = [clade, color]


# Root tree
outgroup_taxa = [ taxon for taxon in map.keys() if map[taxon][0] == 'Outgroup' ]
outgroup_lca = t.get_common_ancestor(outgroup_taxa)
t.set_outgroup(outgroup_lca)


# Order tree
t.ladderize(direction=1)


# Set leaf font
def leaf_font(node):
    """
    Set font for leaf names
    and replace underscores with spaces
    """
    if node.is_leaf():
        if node.name in outgroup_taxa:
            node.name = node.name.replace("_", " ")
            leaf_face = AttrFace(attr="name", ftype="Arial", fgcolor="grey")
        else:
            node.name = node.name.replace("_", " ")
            leaf_face = AttrFace(attr="name", ftype="Arial", fgcolor="black")

        faces.add_face_to_node(
            face=leaf_face, node=node, column=0, position="branch-right"
        )


t.show(tree_style=ts, layout=leaf_font)