# 📖 Problem

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# 💻
# Example 1:
# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Example 2:
# Input: root = [1,null,2]
# Output: 2
 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case
        if root is None:
            return 0

        # Get information from children
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        # Current node adds 1
        return max(left, right) + 1