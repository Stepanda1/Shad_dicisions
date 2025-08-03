class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def reverse(self, root):
    if root is None:
        return None
    root.left, root.right = root.right, root.left
    self.reverse(root.left)
    self.reverse(root.right)
    return root