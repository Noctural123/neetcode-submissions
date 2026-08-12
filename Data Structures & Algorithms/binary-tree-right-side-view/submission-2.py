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

            for i in range (qLen-1):
                node = bfs.popleft()
                if node:
                    left,right = node.left, node.right
                    if left:
                        bfs.append(node.left)
                    if right:
                        bfs.append(node.right)

            rightNode = bfs.popleft()
            if rightNode:
                left, right = rightNode.left, rightNode.right
                if left:
                    bfs.append(left)
                if right:
                    bfs.append(right)

                res.append(rightNode.val)
            
        return res

