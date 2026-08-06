# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]):
            if not node: return None
            l= dfs(node.left)
            r= dfs(node.right)
            if not l: node.left=None 
            if not r:node.right=None 
            if node.val == target and not l and not r:
                return None
            return root
        return dfs(root)