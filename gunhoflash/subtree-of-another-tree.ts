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

function isSameTree(a: TreeNode | null, b: TreeNode | null): boolean {
  if (a === null || b === null) {
    return a === b;
  }

  if (a.val !== b.val) {
    return false;
  }

  return isSameTree(a.left, b.left) && isSameTree(a.right, b.right);
}

function isSubtree(root: TreeNode | null, subRoot: TreeNode | null): boolean {
  if (root === null) {
    return subRoot === null;
  }
  return isSameTree(root, subRoot) || isSubtree(root.left || null, subRoot) || isSubtree(root.right || null, subRoot);
}

