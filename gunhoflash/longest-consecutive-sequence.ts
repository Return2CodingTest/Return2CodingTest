class Element {
  value: number;
  left: Element;
  right: Element;

  constructor(value: number, left: Element | undefined, right: Element | undefined) {
    this.value = value;
    this.left = left || this;
    this.right = right || this;
  }
}

function longestConsecutive(nums: number[]): number {
  let answer = 0;
  const map = new Map<number, Element>();

  for (const num of nums) {
    // skip if already exists
    if (map.has(num)) continue;

    // find left and right elements
    const left = map.get(num - 1)?.left;
    const right = map.get(num + 1)?.right;

    // create new element with value num
    const element = new Element(num, left, right);
    map.set(num, element);

    // update left and right elements
    element.left.right = element.right;
    element.right.left = element.left;

    // update answer
    answer = Math.max(answer, element.right.value - element.left.value + 1);
  }

  return answer;
}
