const MAX_VALUE = 10000;

function merge(intervals: number[][]): number[][] {
  // init up-down counts
  const upCounts = Array(MAX_VALUE + 1).fill(0);
  const downCounts = Array(MAX_VALUE + 1).fill(0);
  for (const [start, end] of intervals) {
    upCounts[start]++;
    downCounts[end]++;
  }

  const answer: number[][] = [];
  let start = 0, end = 0, upDownCount = 0;
  for (let i = 0; i <= MAX_VALUE; i++) {
    const up = upCounts[i];
    const down = downCounts[i];

    if (up !== 0 && upDownCount === 0) {
      start = i;
    }

    upDownCount += up - down;

    if (down !== 0 && upDownCount === 0) {
      end = i;
      answer.push([start, end]);
    }
  }

  return answer;
}
