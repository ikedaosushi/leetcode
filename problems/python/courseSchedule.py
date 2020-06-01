from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        visited = [0] * numCourses

        for x, y in prerequisites:
            graph[x].append(y)

        for i in range(numCourses):
            if not self.dfs(graph, visited, i):
                return False
        return True

    def dfs(self, graph, visited, i):
        if visited[i] == 1:
            return True
        if visited[i] == -1:
            return False

        visited[i] = -1

        for y in graph[i]:
            if not self.dfs(graph, visited, y):
                return False

        visited[i] = 1
        return True
