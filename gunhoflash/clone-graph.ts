class GraphNode {
  val: number;
  neighbors: GraphNode[];

  constructor(val: number = 0, neighbors: GraphNode[] = []) {
    this.val = val;
    this.neighbors = neighbors;
  }
}

function cloneGraph(node: GraphNode | null): GraphNode | null {
  const clones = Array(101).fill(null).map((_, i) => new GraphNode(i))
  const isVisited = Array(101).fill(false);

  if (node === null) {
    return null;
  }

  const visitingStack = [node];
  while (visitingStack.length) {
    const now = visitingStack.pop()!;

    if (isVisited[now.val]) continue;
    isVisited[now.val] = true;

    now.neighbors
    .filter(neighbor => !isVisited[neighbor.val])
    .forEach(neighbor => {
      clones[now.val].neighbors.push(clones[neighbor.val]);
      clones[neighbor.val].neighbors.push(clones[now.val]);
      visitingStack.push(neighbor);
    });
  }

  return clones[node.val];
}
