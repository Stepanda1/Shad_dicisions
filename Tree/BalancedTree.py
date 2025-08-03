class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def height(root):
    if not root:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)
    return max(left_height, right_height) + 1
    
def isBalanced(root):
    if not root:
        return True
    left_height = height(root.left)
    right_height = height(root.right)
    if abs(left_height - right_height) > 1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
root.left.left = TreeNode(5)
root.left.left.left = TreeNode(100)
print(isBalanced(root))