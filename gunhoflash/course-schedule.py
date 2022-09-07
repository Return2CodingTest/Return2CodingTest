from typing import List

class Solution:
  def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    nPrerequisitesList = [0] * numCourses
    nextList = [[] for i in range(numCourses)]
    nVisited = numCourses

    for [nextCourse, prevCourse] in prerequisites:
      nextList[prevCourse].append(nextCourse)
      nPrerequisitesList[nextCourse] += 1

    visitingStack = []
    for i, n in enumerate(nPrerequisitesList):
      if n == 0:
        visitingStack.append(i)

    while len(visitingStack):
      nVisited -= 1
      i = visitingStack.pop()

      for nextCourse in nextList[i]:
        nPrerequisitesList[nextCourse] -= 1
        if nPrerequisitesList[nextCourse] == 0:
          visitingStack.append(nextCourse)

    return nVisited == 0
