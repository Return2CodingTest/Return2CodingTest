#207. Course Schedule

from typing import List

def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    visited = [0 for _ in range(numCourses)]
    courses = dict.fromkeys(range(numCourses), [])
    for a, b in prerequisites:
        courses[b].append(a)

    def dfs(n):
        if visited[n] == 1:
            return False
        visited[n] = 1

        for i in courses[n]:
            ret = dfs(i)
            if not ret:
                return False
        
        visited[n] = 0
        return True
            
    
    for i in range(visited):
        if visited[i] != 1:
            res  = dfs(i)
            if not res:
                return False
    
    return True
    
    #unsolved



