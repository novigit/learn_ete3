#!/usr/bin/env python
from ete3 import Tree

# Loads a tree structure from a newick string. The returned variable ’t’ is the root node for the tree.
t = Tree("(A:1,(B:1,(E:1,D:1):0.5):0.5);" )

# Load a tree structure from a newick file.
t = Tree("rp56.nw")

# You can also specify the newick format. For instance, for named internal nodes we will use format 1.
t = Tree("(A:1,(B:1,(E:1,D:1)Internal_1:0.5)Internal_2:0.5)Root;", format=1)
## ETE3 toolkit specificies several types of newick format types, see their documentation
