# coding: utf-8

"""
    agor.graph.Digraph
    ~~~~~~~~~~~~~~~~~~

    V(): return count of vertex.
    E(): return count of edge.
    adj(): direct to other vertex.
    exist_v(): return graph current vertex.
    add_edge(v, x): return edge of two vertex.
    reverse(): graph inverse directed graph.

"""


class Dgraph(object):
    def __init__(self, v):
        self._V = v
        self._E = 0
        self._bag = 0
        for i in xrange(v):
            self._bag.setdefult(i, set())


    def add_edge(self, v, w):
        self._bag.setdefault(v, set()).add(w)

        self._E += 1
        self._V = len(self._exist_vertex)

    def adj(self, v):
        return self._bag.get(v)

    def V(self):
        return self._V

    def E(self):
        return self._E

    def reverse(self):
        r = Dgraph(self._V)
        for v in r.V():
            d_v = r.adj(v)
            for vv in d_v:
                r.add_edge(vv, v)
        return r



class DirectedDFS(object):
    def __init__(self, G, S):
        self._G = G
        self._S = S
        self._marked = {}
        self.dfs(S)

    def dfs(self, v):
        self._marked[v] = True
        for w in self._G.adj(v):
            if not self.marked.get(w):
                self.dfs(w)



if __name__ == '__main__':
    with open('tinDG.txt', 'wb') as f:
        while f


