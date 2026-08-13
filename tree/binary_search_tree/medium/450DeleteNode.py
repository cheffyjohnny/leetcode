# 📖 Problem

# Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

# Basically, the deletion can be divided into two stages:

# Search for a node to remove.
# If the node is found, delete the node.

# 💻
# Example 1:
# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
# Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
# One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
# Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

# Example 2:
# Input: root = [5,3,6,2,4,null,7], key = 0
# Output: [5,3,6,2,4,null,7]
# Explanation: The tree does not contain a node with value = 0.

# Example 3:
# Input: root = [], key = 0
# Output: []
# Definition for a binary tree node.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root, key):

        # Node doesn't exist
        if root is None:
            return None

        # Search left
        if key < root.val:
            root.left = self.deleteNode(root.left, key)

        # Search right
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)

        # Found the node
        else:

            # No left child
            if root.left is None:
                return root.right

            # No right child
            if root.right is None:
                return root.left

            # Two children
            successor = root.right

            while successor.left:
                successor = successor.left

            root.val = successor.val

            root.right = self.deleteNode(root.right, successor.val)

        return root
    
    #     36
    #    /  \
    #  30    40
    #       /  \
    #     38    48
    #          /  \
    #         45   50


    #     36
    #    /  \
    #  30    45
    #       /  \
    #     38    48
    #          /  \
    #         45   50

    #     36
    #    /  \
    #  30    45
    #       /  \
    #     38    48
    #             \
    #              50