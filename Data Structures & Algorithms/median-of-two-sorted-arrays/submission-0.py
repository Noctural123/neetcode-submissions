class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half - i - 2

            A_left = A[i] if i >= 0 else float('-inf')
            A_right = A[i+1] if (i+1) < len(A) else float('inf')
            B_left = B[j] if j >= 0 else float('-inf')
            B_right = B[j+1] if (j+1) < len(B) else float('inf')

            if (A_left <= B_right) and (B_left <= A_right):
                
                if total % 2:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1

    # # A = [3]
    #        l
    #        r
    # # B = [1, 2]
    # l = 0
    # r = -1
    # total = 3
    # half = 1
    # i = -1
    # j = 0

    # A_left = -inf
    # A_right = 3
    # B_left = 1
    # B_right = 2

    # return min(A_right, B_right) since it's an odd total_length 





        

    # B = [1 | 2 5 6]
    # A = [3 4 | 7]
    #      l m   r

    # total_length = 7
    # half = 3
    # # mid of shorter array
    # m = 0