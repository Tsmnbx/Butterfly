from taxonomy import*

class Phylogenetic_Tree:
    """A phylogenetic tree for the class Lepidoptera where nodes are either a taxonmic group or a species"""
    def __init__(self, node, left = None, right = None):
        """Initialize the phylogentic tree"""
        self.node = node
        self.left = left
        self.right = right
        
    