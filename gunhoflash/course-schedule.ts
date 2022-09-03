function canFinish(numCourses: number, prerequisites: number[][]): boolean {
  const nPrerequisitesList: number[] = Array(numCourses).fill(0);
  const nextList: number[][] = Array(numCourses).fill(null).map(() => []);
  let nVisited = 0;

  for (const [nextCourse, prevCourse] of prerequisites) {
    nextList[prevCourse].push(nextCourse);
    ++nPrerequisitesList[nextCourse];
  }

  const visitingStack: number[] = [];
  for (let i = 0; i < numCourses; ++i) {
    if (nPrerequisitesList[i] === 0) {
      visitingStack.push(i);
    }
  }

  while (visitingStack.length) {
    ++nVisited;
    const i = visitingStack.pop()!;

    for (const nextCourse of nextList[i]) {
      if (--nPrerequisitesList[nextCourse] === 0) {
        visitingStack.push(nextCourse);
      }
    }
  }

  return nVisited === numCourses;
}
