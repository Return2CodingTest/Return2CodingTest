function insert(intervals: number[][], newInterval: number[]): number[][] {
  const minNum = intervals.length ? Math.min(intervals.at(0)![0], newInterval[0]) : newInterval[0];
  const maxNum = intervals.length ? Math.max(intervals.at(-1)![1], newInterval[1]) : newInterval[1];

  // init up-down counts
  const upCounts = Array(maxNum + 1).fill(0);
  const downCounts = Array(maxNum + 1).fill(0);
  upCounts[newInterval[0]] = 1;
  downCounts[newInterval[1]] = 1;
  for (const [start, end] of intervals) {
    upCounts[start]++;
    downCounts[end]++;
  }

  const answer: number[][] = [];
  let start = 0, end = 0, upDownCount = 0;
  for (let i = minNum; i <= maxNum; i++) {
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
