# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
    
        def dfs(node, currMax):
            if not node:
                return None
            if node.val - currMax >= 0:
                self.res += 1
                print(str(node.val) + "-" + str(currMax) +'\n')
                currMax = max(currMax, node.val)
            
            dfs(node.left,currMax)
            dfs(node.right,currMax)
    
        dfs(root, float('-inf'))
        return self.res

    # - DFS
    # - Go down tree holding running max (pass max into recursive call)
    # - compare by doing currNode.val - root.val
    # - If the difference is > 0 then it is a good node

                #     2
                #     /\
                #    1  1
                #   /\  /\
                #  3 x 1  5

                #      3
                #     / \
                #    3   null
                #   /\   
                #  4  2

                #      -1
                #     / \
                #    5   -2
                #   /\   /\
                #  4  4 2  -2
                # /\  /\ /\ /\
                #x  x-4x-23x-2
        