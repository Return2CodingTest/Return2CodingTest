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

function levelOrder(root: TreeNode | null): number[][] {
  const answer: number[][] = [];

  function pushByLevelOrder(node: TreeNode | null, level: number) {
    if (node === null) return;
    answer[level] = answer[level] || [];
    answer[level].push(node.val);
    pushByLevelOrder(node.left, level + 1);
    pushByLevelOrder(node.right, level + 1);
  }

  pushByLevelOrder(root, 0);

  return answer;
}
