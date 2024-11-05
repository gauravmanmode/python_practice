class UnionFind:
    def __init__(self,n):
        self.parent = list(range(n))
        self.rank = [0] *n
    
    def find(self, x):
        if self.parent[x]!= x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]


    def union(self, x,y):
        rootx, rooty = self.find(x), self.find(y)
        if rootx != rooty:
                if self.rank[rootx] > self.rank[rooty]:
                    self.parent[rooty] = rootx
                elif self.rank[rootx] < self.rank[rooty]:
                    self.parent[rootx] = rooty
                else:
                    self.parent[rooty] = rootx
                    self.rank[root_x] += 1
                return True
        return False

def minimumcost(A,B):
    B.sort(key = lambda x: x[2])
    uf = UnionFind(A+1)

    total_cost = 0
    edges_used = 0

    for u, v, cost in B:
        if uf.union(u, v):
            total_cost+=cost
            edges_used+=1
            if edges_used == A - 1:
                break

    return total_cost
        