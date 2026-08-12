# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev_group = dummy

        while True:
            kth = self.find_kth_node(prev_group, k)

            if not kth:
                break
            next_group = kth.next

            prev, curr = kth.next, prev_group.next

            while curr != next_group:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = prev_group.next
            prev_group.next = kth
            prev_group = tmp

        return dummy.next
    


    def find_kth_node(self, curr, k):
        
        while curr and k > 0:
            curr = curr.next
            k -= 1
        
        return curr
