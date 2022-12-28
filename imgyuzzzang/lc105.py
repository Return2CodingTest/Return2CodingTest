#105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None

        now = preorder[0]

        index = inorder.index(now)

        leftPreorder = preorder[1 : 1 + index]
        rightPreorder = preorder[1 + index:]

        leftInorder = inorder[0 : index]
        rightInorder = inorder[index + 1:]


        leftTree = self.buildTree(leftPreorder, leftInorder)
        rightTree = self.buildTree(rightPreorder, rightInorder)

        tree = TreeNode(now, leftTree, rightTree)
        
        return  tree