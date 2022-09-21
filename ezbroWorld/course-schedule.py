import collections

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:   
        
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)

        traced, visited = set(), set()
        
        def dfs(i):
            
            if i in visited :
                return True
            
            if i in traced : 
                return False
            
            traced.add(i)
            
            for j in graph[i]:
                if not dfs(j):
                    return False
                
            traced.remove(i)
            visited.add(i)
            return True
            
            
        for x in list(graph):
            if not dfs(x):
                return False
        return True
