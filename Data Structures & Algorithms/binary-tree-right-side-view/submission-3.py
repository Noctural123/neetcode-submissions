# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        bfs = deque([root])
        res = []

        while bfs:
            qLen = len(bfs)
            rightNode = None

            for i in range(qLen):
                node = bfs.popleft()

                if node:
                    rightNode = node
                    bfs.append(node.left)
                    bfs.append(node.right)
            
            if rightNode:
                res.append(rightNode.val)
            
        return res

