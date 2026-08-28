class UF:
    def __init__(self) -> None:
        self.parent ={}
        self.weight ={}
    def add(self,x):
        if x not in self.parent:
            self.parent[x]=x
            self.weight[x]=1.
    def find(self,x):
        if x!=self.parent[x]:
            org_par = self.parent[x]
            self.parent[x]=self.find(self.parent[x])
            self.weight[x]*=self.weight[org_par]
        return self.parent[x]
    def union(self,x,y,val):
        self.add(x)
        self.add(y)
        r_x = self.find(x)
        r_y = self.find(y)
        if r_x!=r_y:
            self.parent[r_x]=r_y
            self.weight[r_x]=val*self.weight[y]/self.weight[x]
    def get_ratio(self,x,y):
        if x not in self.parent or y not in self.parent or self.find(x)!=self.find(y): return -1.
        return self.weight[x]/self.weight[y]


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf =UF()
        for (a,b), value in zip(equations,values):
            uf.union(a,b,value)
        return [uf.get_ratio(a,b) for a,b in queries]

