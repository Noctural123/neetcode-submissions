# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        prev = None
        curr = head
        length = 0

        while curr:
            length += 1
            new_node = ListNode(curr.val)
            new_node.next = prev
            prev = new_node
            curr = curr.next
        reversed_list = prev

        new_length = 0
        curr = head
        while new_length != length:
            temp_next = curr.next
            curr.next = reversed_list
            reversed_list_next = reversed_list.next
            reversed_list.next = temp_next
            
            reversed_list = reversed_list_next
            curr = temp_next
            new_length += 1
        
        curr = head
        res_length = 0
        while res_length != length-1:
            print(curr.val)
            curr = curr.next
            res_length += 1
        curr.next = None

    # 2 -> 4 -> 6 -> 8
    # 8 -> 6 -> 4 -> 2

    # 2 -> 6 -> 6 -> 8
    # 8 -> 6 -> 6 -> 2
    
    # 2 8 6 6

    # 2 -> 4 -> 6 -> 8 -> 10
    # 10 -> 8 -> 6 -> 4 -> 2

    # 2 10 4 8 6
