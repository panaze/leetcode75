#Given the root of a binary tree, return the length of the diameter of the tree.

#The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

#The length of a path between two nodes is represented by the number of edges between them.

#Example 1:
#Input: root = [1,2,3,4,5]
#Output: 3

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
        diameter = 0

        def maxDepth(root: Optional[TreeNode]) -> int:
            if root is None:
                return 0

            nonlocal diameter

            # recursively find the longest path in
            # both left child and right child
            left = maxDepth(root.left)
            right = maxDepth(root.right)

            # update the diameter if left_path plus right_path is larger
            diameter = max(diameter, left + right)
            
            return max(left,right) + 1

        maxDepth(root)
        return diameter
