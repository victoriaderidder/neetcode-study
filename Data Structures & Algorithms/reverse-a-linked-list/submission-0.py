# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        if vals == []:
            return head
        vals.reverse()
        new_head = ListNode(vals[0])
        curr = new_head
        for i in range(1, len(vals)):
            curr.next = ListNode(vals[i])
            curr = curr.next
        return new_head
        