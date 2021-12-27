from typing import List


class Graph:
    def __init__(self, nodes: int = 100):
        self.graph: List[List[int]] = []
        self.nodes = nodes
        for _ in range(nodes):
            self.graph.append([])

    def addEdge(self, a, b, w=None, directed=False):
        self.graph[a].append(b if not w else (b, w))
        if not directed:
            self.graph[b].append(a if not w else (a, w))

    def printGraph(self):
        for idx, item in enumerate(self.graph):
            if len(item) > 0:
                print(f"{idx}-->{[x for x in item]}")

    def _dfs(self, starting: int, res: List, visited: List[bool]) -> List:
        res.append(starting)
        visited[starting] = True
        for i in self.graph[starting]:
            if not visited[i]:
                self._dfs(i, res, visited)
        return res

    def dfs(self, starting: int = 0) -> List:
        return self._dfs(starting, [], [False] * self.nodes)

    def contains_cycle(self):
        visited = [False] * self.nodes
        visited[0] = True
        _arr = [0]
        while len(_arr) > 0:
            popped = _arr.pop(0)
            if visited[popped]:
                return True
            if not visited[popped]:
                visited[popped] = True
            for i in self.graph[popped]:
                if not visited[i]:
                    _arr.append(i)

        return False

    def _contains_cycle_directed(
        self, res: bool, cur: List[bool], visited: List[bool], root: int = 0
    ):
        cur[root] = True
        visited[root] = True
        for i in self.graph[root]:
            if cur[i]:
                return True
            res = self._contains_cycle_directed(res, cur, visited, i)
            if res:
                break
            cur[i] = False
        return res

    def contains_cycle_directed(self):
        return self._contains_cycle_directed(
            False, [False] * self.nodes, [False] * self.nodes
        )

    def bfs(self, starting=0) -> List:
        visited = [False] * self.nodes
        _arr = [starting]
        res = []
        while len(_arr) > 0:
            popped = _arr.pop(0)
            if not visited[popped]:
                visited[popped] = True
                res.append(popped)
            for i in self.graph[popped]:
                if not visited[i]:
                    _arr.append(i)

        return res

    def bfs_dist(self, starting=0):
        visited = [False] * self.nodes
        _arr = [starting]
        dist = [0] * self.nodes
        while len(_arr) > 0:
            popped = _arr.pop(0)
            if not visited[popped]:
                visited[popped] = True
            for i in self.graph[popped]:
                if not visited[i]:
                    _arr.append(i)
                    if dist[i] == 0:
                        dist[i] = dist[popped] + 1

        return dist

    def dijkstra(self, start: int = 0):
        final = [False] * self.nodes
        dist = [1000000 for _ in range(self.nodes)]
        dist[start] = 0
        dist_set = [(start, 0)]
        prev = [start for _ in range(self.nodes)]
        while not all(final):
            min_dist = 10000000
            min_idx = -1
            for idx, item in enumerate(dist_set):
                if item[1] < min_dist:
                    min_idx = idx
                    min_dist = item[1]
            selected_idx, selected_dist = dist_set.pop(min_idx)
            for node, weight in self.graph[selected_idx]:
                if not final[node]:
                    new_dist = selected_dist + weight
                    if new_dist < dist[node]:
                        dist_set = [x for x in dist_set if x[0] != node]
                        dist_set.append((node, new_dist))
                        dist[node] = new_dist
                        prev[node] = selected_idx
            final[selected_idx] = True
        return dist, prev
