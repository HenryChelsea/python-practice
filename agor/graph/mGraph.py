# coding: utf-8

"""
    grapys.mGraphs
    ~~~~~~~~~~~~~~

    Use for graph standard api

    V(): return node count
    E(): return edges
    add_edge(v, w): add edge
    adj(v): releated to node
    int degree(v): node degree

    int max_degree(G): graph max degree
    int avg_degree(G): graph average degree
    int numberOfSelfLoops(G): graph self loops counts
    to_string(self): self to to_string

    Paths: return all path to start
    hasPathTo(v): return is s > v path
    pathTo(v): return s > v path

"""
import Queue


class Graph(object):
    def __init__(self, graph_list):
        self._V = 0
        self._E = 0
        self._exist_v = set()
        self._bag = {}
        for node in graph_txt:
            v, w = node
            self.add_edge(v, w) 

    def add_edge(self, v, w):
        self._bag.setdefault(v, []).append(w)
        self._bag.setdefault(w, []).append(v)
        self._exist_v.add(v)
        self._exist_v.add(w)
        self._V = len(self._exist_v)
        self._E += 1

    def V(self):
        return self._V

    def E(self):
        return self._E

    def exist_v(self):
        return list(self._exist_v)

    def adj(self, v):
        return self._bag.get(v, [])


class DFS(object):
    def __init__(self, G, S):
        self._G = G
        self._S = S
        self.count = 0
        self._marked = {}
        self.edgeTo = {}
        self.dfs(G, S)

    def dfs(self, G, v):
        self._marked[v] = True
        self.count += 1

        for w in reversed(G.adj(v)):
            if not self._marked.get(w):
                self.edgeTo[w] = v
                self.dfs(G, w)

    def marked(self, v):
        return bool(self._marked.get(v)) | False

    def count():
        return self.count

    def has_path_to(self, v):
        return self.marked(v)

    def path_to(self, v):
        if not self.has_path_to(v):
            return None

        paths = Queue.deque()
        cur_node = v
        paths.append(v)
        while cur_node != self._S:
            _node = self.edgeTo.get(cur_node)
            paths.append(_node)
            cur_node =  _node
        return [p for p in paths]

    def paths(self):
        _paths = {}

        for w in self._G.exist_v():
            w_paths = self.path_to(w)
            _paths[w] = w_paths
        return _paths


class Test(object):
    pass

if __name__ == '__main__':
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
    print ">>> ", graph.exist_v()
    search = DFS(graph, 0)
    print search._marked
    print search.edgeTo
    print search.path_to(5)
    print search.paths()

