# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxLen = 0

        def getHeight(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            leftHeight = getHeight(node.left)
            rightHeight = getHeight(node.right)

            self.maxLen = max(self.maxLen, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)


        getHeight(root)
        return self.maxLen
        
        