# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        q = deque([root])
        res = []

        while q:
            temp = []
            lenQ = len(q)

            for i in range(lenQ):
                temp.append(q[0].val)
                currNode = q.popleft()

                if currNode.left:
                    q.append(currNode.left)
                if currNode.right:
                    q.append(currNode.right)

            res.append(temp)
        
        return res

