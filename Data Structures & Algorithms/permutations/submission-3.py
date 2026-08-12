class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms = [[]]
    
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    copy = perm.copy()
                    copy.insert(i, n)
                    new_perms.append(copy)
            perms = new_perms
        
        return perms


        # [2, 3]
        # [3, 2]

        # insert 1

        # 1 2 3
