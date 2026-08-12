# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next
        
        prev = head
        index_to_remove = length - n
        for i in range(index_to_remove-1):
            prev = prev.next
        
        if prev == head and n == length:
            return head.next

        remove = prev.next 

        prev.next = remove.next
        return head


        # index_to_remove = 4
        # input = [1, 2, 3, 4, 5] 
        # n = 2

        # output = [1, 2, 3, 5]

        
        # length = 5
        # 5 - 2 = 3 + 1

        # 2 - 2 = 0 + 1