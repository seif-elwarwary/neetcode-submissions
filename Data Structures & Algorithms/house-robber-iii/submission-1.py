# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache ={None:0}
        def dfs(node):
            if node in cache: return cache[node]
            cache[node] = node.val
            if node.left:
                cache[node] += dfs(node.left.left)
                cache[node] += dfs(node.left.right)
            if node.right:
                cache[node] += dfs(node.right.left)
                cache[node] += dfs(node.right.right)
            cache[node] = max(cache[node],dfs(node.left)+dfs(node.right))
            return cache[node]
        return dfs(root)