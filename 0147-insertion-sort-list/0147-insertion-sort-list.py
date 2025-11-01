# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr = head
        while curr:
            pre = dummy
            while pre.next and pre.next.val < curr.val:
                pre = pre.next
            nxt_temp = curr.next
            curr.next = pre.next
            pre.next = curr
            curr = nxt_temp
        return dummy.next
