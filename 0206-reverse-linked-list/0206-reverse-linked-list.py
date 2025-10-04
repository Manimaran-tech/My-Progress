#class ListNode:
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverse=None
        while head is not None:
            new=ListNode(head.val)
            new.next=reverse
            reverse=new
            head=head.next
        return reverse