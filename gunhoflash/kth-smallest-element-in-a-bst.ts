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

function kthSmallest(root: TreeNode | null, k: number): number {
  const inorderList: number[] = [];
  function setInorderList(root: TreeNode | null) {
    if (root === null) return;
    setInorderList(root.left);
    inorderList.push(root.val);
    setInorderList(root.right);
  }
  setInorderList(root);
  return inorderList[k - 1];
}
