#https://github.com/prd-xxx/gorichan_kyopro_library/tree/main/lowlink
class LowLink:
    def __init__(self,n,es):
        self.n = n
        self.es = es
        self.visited = [0] * n
        self.order = [0] * n
        self.low = [0] * n
        self.count = 0
        self.articulation_points = set()
        self.bridges = []
        self.dfs_parent = [-1] * n
        self.dfs_child = [[] for _ in range(n)]
        self.is_dfs_root = [0] * n
    def _dfs(self,rt):
        self.is_dfs_root[rt] = 1
        stack = [(-1,rt,0)]
        while stack:
            p,c,dir = stack.pop()
            if dir==0:
                if self.visited[c]: continue
                self.visited[c] = 1
                self.low[c] = self.order[c] = self.count
                self.count += 1
                if c != rt:
                    self.dfs_parent[c] = p
                    self.dfs_child[p].append(c)
                for to in self.es[c][::-1]:
                    if self.visited[to]:
                        if to != p:
                            self.low[c] = min(self.low[c], self.order[to])
                        continue
                    stack.append((c,to,1))
                    stack.append((c,to,0))
            else:
                if self.dfs_parent[c] != p: continue
                if c != self.dfs_parent[p]:
                    self.low[p] = min(self.low[p], self.low[c])
                if p != rt and self.order[p] <= self.low[c]:
                    self.articulation_points.add(p)
                if self.order[p] < self.low[c]:
                    self.bridges.append((p,c)) 
        if len(self.dfs_child[rt]) >= 2:
            self.articulation_points.add(rt)
    def build(self):
        self.component_num = 0
        for i in range(self.n):
            if self.visited[i]: continue
            self._dfs(i)
            self.component_num += 1