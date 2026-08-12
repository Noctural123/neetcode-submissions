class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)

        def dfs(curr, parent):
            if curr in seen:
                return True
            
            seen.add(curr)
            for nei in adj[curr]:
                if nei == parent:
                    continue
                if dfs(nei, curr):
                    return True

            return False


        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
            seen = set()

            if dfs(n1, -1):
                return [n1, n2]
        
        return []

    # seen = 1, 2

    # dfs(1, -1)

    # adj
    # 1: 2, 3
    # 2: 1
    # 3: 1
    # 4:
