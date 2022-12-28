class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    def getLowestCommonAncestor(root: TreeNode, p: int, q: int) -> TreeNode:
      if p <= root.val <= q:
        return root
      if q < root.val:
        return getLowestCommonAncestor(root.left, p, q)
      return getLowestCommonAncestor(root.right, p, q)

    return getLowestCommonAncestor(root, min(p.val, q.val), max(p.val, q.val))
