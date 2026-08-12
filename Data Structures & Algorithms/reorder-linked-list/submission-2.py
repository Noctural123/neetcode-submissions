# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
                
        second = slow.next
        slow.next = prev = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        first, second = head, prev

        while second:
            tmp_first, tmp_second = first.next, second.next
            first.next = second
            second.next = tmp_first
            first, second = tmp_first, tmp_second



        # Test case 1
        # Input = [2, 4, 6, 8]

        # first = [2, 4]
        # second = [8, 6]

        # 2 8 4 6

        # Test case 2
        # Input: [2, 4, 6, 8, 10]

        # first = [2, 4, 6]
        # second= [8, 10]