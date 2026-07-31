# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def traverse(node : Optional[TreeNode]):
            if node is None: return TreeNode(val)
            if node.val < val:
                fin_node = traverse(node.right)
                if node.right is None:
                    node.right = fin_node
            else: 
                fin_node = traverse(node.left)
                if node.left is None:
                    node.left = fin_node
            return node
        return traverse(root)
