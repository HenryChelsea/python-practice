# coding: utf-8

"""
    agor.graph.connected_component
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Graph:
        V(): count of vertex
        E(): count edge of Graph
        adj: related to vertex
        add_edge(v, w): add edge in graph
        exist_v(): current vertex index

"""


class Graph(object):
    

    def __init__(self, container):
        self._V = 0
        self._E = 0
        self._exist_v = set()
        self._bag = {}
        for node in container:
            v, w = node
            self.add_edge(v, w)

    def add_edge(self, v, w):
        self._bag.setdefault(v, set()).add(w)
        self._bag.setdefault(w, set()).add(v)
        self._exist_v.add(v)
        self._exist_v.add(w)
        self._E += 1
        self._V = len(self._exist_v)

    def V(self):
        return self._V

    def E(self):
        return self._E

    def exist_v(self):
        return list(self._exist_v)

    def adj(self, v):
        return self._bag.get(v)

class CC(object):
    def __init__(self, G):
        self._G = G
        self.count = 0
        self._id = {}
        self.marked = {}

        for s in G.exist_v():
            if not self.marked.get(s):
                self.count += 1
                self.dfs(s)


    def dfs(self, s):
        for v in self._G.adj(s):
            if not self.marked.get(v):
                self.marked[v] = True
                self._id.setdefault(self.count, set()).add(v)
                self.dfs(v)

    def back_id(self):
        return self._id

    def count(self):
        return self.count

if __name__ == "__main__":
    graph_txt = [
        [0, 5],
        [2, 4],
        [2, 3],
        [1, 2],
        [0, 1],
        [3, 4],
        [3, 5],
        [0, 2]
    ]


    graph = Graph(graph_txt)

    cc = CC(graph)
    print cc.back_id()


