# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.sortedList = []

        def dfs(node):
            if not node:
                return None
            
            left,right = node.left, node.right
            
            if left:
                dfs(left)

            self.sortedList.append(node.val)

            if right:
                dfs(right)


        dfs(root)
        print(self.sortedList)
        return self.sortedList[k-1]