# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootList: list[Optional[int]] = []
        subList: list[Optional[int]] = []

        def dfs(node: Optional[TreeNode], output: list[Optional[int]]) -> None:
            if not node:
                output.append(None)
                return
            
            output.append(node.val)
            dfs(node.left, output)
            dfs(node.right, output)

        dfs(root, rootList)
        dfs(subRoot, subList)

        m = len(subList)
        for i in range(len(rootList) - m + 1):
            if rootList[i : i + m] == subList:
                return True

        return False


    
        