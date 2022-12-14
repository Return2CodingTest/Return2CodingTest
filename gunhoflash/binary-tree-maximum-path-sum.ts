class MyTreeNode {
  val: number;
  left: MyTreeNode | null;
  right: MyTreeNode | null;
  maxSum: number = 0;
  constructor(val?: number, left?: MyTreeNode | null, right?: MyTreeNode | null) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
  }
}

function maxChildrenSum(root: MyTreeNode | null): number {
  if (root === null) return 0;
  const maxSum = root.val + Math.max(
    0,
    maxChildrenSum(root.right),
    maxChildrenSum(root.left)
  );

  root.maxSum = maxSum;
  return maxSum;
}

function getMaxPathSum(root: MyTreeNode | null): number {
  if (root === null) return 0;

  return Math.max(
    Math.max(root.left?.maxSum || 0, 0) + Math.max(root.right?.maxSum || 0, 0) + root.val,
    root.left ? getMaxPathSum(root.left) : root.val,
    root.right ? getMaxPathSum(root.right) : root.val
  );
}

function maxPathSum(root: MyTreeNode): number {
  maxChildrenSum(root);
  return getMaxPathSum(root);
}
