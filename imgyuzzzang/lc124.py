#124. Binary Tree Maximum Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxNum = -1000
    def getPathSum(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        leftSum = self.getPathSum(root.left)
        rightSum = self.getPathSum(root.right)
        print(root.val, leftSum, rightSum)
        res = root.val + max(leftSum, rightSum, 0)

        self.maxNum = max(self.maxNum, res, root.val + leftSum + rightSum)

        return res

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxNum = -1000
        self.getPathSum(root)
        return self.maxNum
