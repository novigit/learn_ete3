#!/usr/bin/env python

from ete3 import Tree, TreeStyle, TextFace, NodeStyle, AttrFace, faces
import csv
import argparse

# make command line interface
parser = argparse.ArgumentParser(
    description="Root, color and render a tree in PNG, SVG or PDF"
)
parser.add_argument(
    "-t", 
    dest="tree_file",
    metavar="TREE_FILE",
    required=True, 
    help="Tree in Newick format"
)
parser.add_argument(
    "-m", 
    dest="mapping_file", 
    metavar="MAPPING_FILE",
    required=True, 
    help="Tab separated mapping file"
         "taxon <tab> clade <tab> color"
)
parser.add_argument(
    "-o",
    dest="outfile",
    metavar="OUTFILE",
    required=True,
    help="Name of the outfile"
         "Extension determines format"
         "Ex. file.pdf is in PDF format"
)
args = parser.parse_args()

# load tree
t = Tree(args.tree_file)

# load mapping file
## taxon - clade - color
with open(args.mapping_file, "r") as m:
    map = {}
    for taxon, clade, color in csv.reader(m, delimiter="\t"):
        map[taxon] = [clade, color]


# root tree
outgroup_taxa = [taxon for taxon in map.keys() if map[taxon][0] == "Outgroup"]
outgroup_lca = t.get_common_ancestor(outgroup_taxa)
t.set_outgroup(outgroup_lca)


# set TreeStyle
ts = TreeStyle()
ts.show_leaf_name = False
ts.show_branch_support = True
ts.scale_length = 0.3
# ts.title.add_face(TextFace("Tree Title", fsize=20), column=0)


# Suppress nodes
# and increase line width
ns = NodeStyle()
ns["size"] = 0
ns["hz_line_width"] = 1
ns["vt_line_width"] = 1
for node in t.traverse():
    node.set_style(node_style=ns)


# Order tree
t.ladderize(direction=1)


# Set leaf font
def leaf_font(node):
    """
    Set font for leaf names
    and replace underscores with spaces
    """
    if node.is_leaf():

        # extract color from loaded mapping file
        color = map[node.name][1]

        # remove underscores from leaf name
        node.name = node.name.replace("_", " ")

        # color leaf name
        leaf_face = AttrFace(attr="name", fgcolor=color)
        faces.add_face_to_node(
            face=leaf_face, node=node, column=1, position="branch-right"
        )

    # else:
    #     support_face = AttrFace(attr="support", ftype="Arial", fsize=8, fgcolor="crimson")
    #     faces.add_face_to_node(face=support_face, node=node, column=0, position="branch-top")


# t.render("scratch.pdf", tree_style=ts, layout=leaf_font, w=210, units="mm")
t.render(args.outfile, tree_style=ts, layout=leaf_font)