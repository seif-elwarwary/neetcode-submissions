class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for i, eq in enumerate(equations):
            a, b = eq
            adj[a].append((b, values[i]))
            adj[b].append((a, 1 / values[i]))
        def bfs(src, dst):
            if src not in adj or dst not in adj:
                return -1
            q, visit = deque([(src, 1)]), set()
            visit.add(src)
            while q:
                n, w = q.popleft()
                if n == dst: return w

                for node, wight in adj[n]:
                    if node not in visit:
                        visit.add(node)
                        q.append((node, w*wight))
                    
            return -1

        return [bfs(q[0],q[1]) for q in queries]