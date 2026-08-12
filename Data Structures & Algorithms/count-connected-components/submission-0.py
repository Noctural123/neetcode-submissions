class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        visit = [False] * n

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        
        def dfs(node):
            for nei in adj[node]:
                if not visit[nei]:
                    visit[nei] = True
                    dfs(nei)
    
        components = 0
        
        for i in range(n):
            if not visit[i]:
                visit[i] = True
                dfs(i)
                components += 1
        
        return components

    




    # 0-1-2-3 4-5
    # 6 nodes
    # 4 edges
