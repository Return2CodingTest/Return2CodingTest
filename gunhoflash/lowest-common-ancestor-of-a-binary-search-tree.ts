class TreeNode {
  val: number;
  left: TreeNode | null;
  right: TreeNode | null;
  constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function lowestCommonAncestor(
  root: TreeNode,
  p: TreeNode,
  q: TreeNode
): TreeNode {
  function getLowestCommonAncestor(
    root: TreeNode,
    p: number,
    q: number
  ): TreeNode {
    if (p <= root.val && root.val <= q) return root;
    return q < root.val
      ? getLowestCommonAncestor(root.left!, p, q)
      : getLowestCommonAncestor(root.right!, p, q);
  }

  return getLowestCommonAncestor(
    root,
    Math.min(p.val, q.val),
    Math.max(p.val, q.val)
  );
}
