#https://github.com/prd-xxx/gorichan_kyopro_library/tree/main/bipartite
class Bipartite:
    def __init__(self, es):
        self.es = es
        self.N = len(es)
    def analize(self):
        self.isolated_vertices = []
        self.bipartite_ccs = []
        self.not_bipartite_ccs = []
        self.cols = [0] * self.N
        for s in range(self.N):
            if self.cols[s] != 0: continue
            if len(self.es[s])==0:
                self.isolated_vertices.append(s)
                continue
            stack = [(s,1)]
            self.cols[s] = 1
            is_bipartite = True
            ccs = {s}
            while stack:
                v,col = stack.pop()
                for to in self.es[v]:
                    ccs.add(to)
                    if self.cols[to] == col:
                        is_bipartite = False
                    if self.cols[to] == 0:
                        stack.append((to, -col))
                        self.cols[to] = -col
            if is_bipartite:
                self.bipartite_ccs.append(ccs)
            else:
                self.not_bipartite_ccs.append(ccs)
    def is_bipartite(self):
        return len(self.not_bipartite_ccs) == 0
    def bipartite_distribution(self, i):
        assert 0 <= i < len(self.bipartite_ccs)
        b = w = 0
        for v in self.bipartite_ccs[i]:
            if self.cols[v]==1:
                b += 1
            else:
                w += 1
        return (b,w)
