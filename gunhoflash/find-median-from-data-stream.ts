enum HeapType {
  minHeap,
  maxHeap,
}

class Heap {
  list: number[];
  type: HeapType;

  constructor(type: HeapType) {
    this.list = [];
    this.type = type;
  }

  get size() {
    return this.list.length;
  }

  push(num: number) {
    this.list.push(num);
    this.#bubbleUp();
  }

  pop() {
    const num = this.list[0];
    const last = this.list.pop()!;
    if (this.list.length) {
      this.list[0] = last;
      this.#bubbleDown();
    }
    return num;
  }

  get top() {
    return this.list[0];
  }

  #bubbleUp() {
    let index = this.list.length - 1;
    while (index > 0) {
      const current = this.list[index];
      const parentIndex = Math.floor((index - 1) / 2);
      const parent = this.list[parentIndex];
      if (this.type === HeapType.maxHeap && parent >= current) {
        break;
      }
      if (this.type === HeapType.minHeap && parent <= current) {
        break;
      }
      this.list[parentIndex] = current;
      this.list[index] = parent;
      index = parentIndex;
    }
  }

  #bubbleDown() {
    let index = 0;
    while (index < this.list.length) {
      const leftIndex = index * 2 + 1;
      const rightIndex = leftIndex + 1;
      const left = this.list[leftIndex];
      const right = this.list[rightIndex];
      const parent = this.list[index];
      let targetIndex = index;
      if (this.type === HeapType.maxHeap) {
        if (left !== undefined && left > parent) {
          targetIndex = leftIndex;
        }
        if (right !== undefined && right > parent && right > left) {
          targetIndex = rightIndex;
        }
      }
      if (this.type === HeapType.minHeap) {
        if (left !== undefined && left < parent) {
          targetIndex = leftIndex;
        }
        if (right !== undefined && right < parent && right < left) {
          targetIndex = rightIndex;
        }
      }
      if (targetIndex === index) {
        break;
      }
      this.list[index] = this.list[targetIndex];
      this.list[targetIndex] = parent;
      index = targetIndex;
    }
  }
}

class MedianFinder {
  maxHeap: Heap;
  minHeap: Heap;

  constructor() {
    this.maxHeap = new Heap(HeapType.maxHeap);
    this.minHeap = new Heap(HeapType.minHeap);
  }

  addNum(num: number): void {
    if (num <= this.maxHeap.top) {
      this.maxHeap.push(num);
      if (this.maxHeap.size > this.minHeap.size + 1) {
        this.minHeap.push(this.maxHeap.pop());
      }
    } else {
      this.minHeap.push(num);
      if (this.minHeap.size > this.maxHeap.size + 1) {
        this.maxHeap.push(this.minHeap.pop());
      }
    }
  }

  findMedian(): number {
    if (this.maxHeap.size === this.minHeap.size) {
      return (this.maxHeap.top + this.minHeap.top) / 2;
    }
    return this.maxHeap.size > this.minHeap.size
      ? this.maxHeap.top
      : this.minHeap.top;
  }
}
