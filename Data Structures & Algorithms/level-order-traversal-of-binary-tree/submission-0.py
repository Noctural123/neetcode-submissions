# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        bfs = deque([root])
        res = []

        while bfs:
            level = []
            qLen = len(bfs)

            for i in range (qLen):
                currNode = bfs.popleft()
                if currNode:
                    bfs.append(currNode.left)
                    bfs.append(currNode.right)
                    level.append(currNode.val)

            if level:
                res.append(level)
        
        return res
    
        root = [1]
        level = [1]
        qlen = 1
        currNode = 1

        res = [[1]]

        bfs = []



