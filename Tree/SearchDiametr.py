class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def __init__(self):
    self.diametr = 0
    
def diametrOfBinaryTree(self, root):
    self.height(root)
    return self.diametr

def height(self, node):
    if not node:
        return 0
    left_height = self.height(node.left)
    right_height = self.height(node.right)
    self.diametr = max(self.diametr, left_height+right_height)
    return 1 + max(left_height, right_height)