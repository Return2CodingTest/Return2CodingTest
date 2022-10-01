function eraseOverlapIntervals(intervals: number[][]): number {
  const sortedIntervalList = (JSON.parse(JSON.stringify(intervals)) as number[][]).sort((a, b) => a[0] - b[0]);
  let nowEnd = -50000;
  let nDeleted = 0;

  for (const [start, end] of sortedIntervalList) {
    if (nowEnd <= start) {
      // not overlapped
      nowEnd = end;
      continue;
    }

    // overlapped
    nDeleted++;
    if (end < nowEnd) {
      nowEnd = end;
    }
  }

  return nDeleted;
}
