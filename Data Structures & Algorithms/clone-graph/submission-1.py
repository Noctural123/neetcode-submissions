"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copy = Node(node.val)
            old_to_new[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        return dfs(node) if node else None

        # 1: [2]
        # 2: [1,3]
        # 3: [2]

        # # original : copy
        # old_to_new = {1 : 1, 2 : 2, 3 : 3}

        # dfs(1):
        # copy = 1 #copy
        # copy_1_neighbors = [2 #copy] At the very end

        # dfs(2):
        # copy = 2 #copy

        # copy_2_neighbors = [1 #copy, 3 #copy]

        # dfs(3):
        # copy = 3 #copy

        # copy_3_neightbors = [2 #copy]





