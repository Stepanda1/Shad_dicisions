class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def isSame(self, node1, node2):
        if not node1 or not node2:
            return True
        if not node1 and not node2:
            return False
        if node1.val != node2.val:
            return False
        return isSame(node1.left, node2.left) and isSame(node1.right, node2.right)