# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head):
        prev=None
        curr=head
        while curr:
            temp= curr.next
            curr.next= prev
            prev=curr
            curr=temp
        return prev
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r_head=self.reverseList(head)
        remove_spot= n
        count=0
        dummy=ListNode(0)
        dummy.next=r_head
        prev=dummy
        curr=r_head
        while curr:
            if count==n-1:
                prev.next=curr.next
                break
            prev=curr
            curr=curr.next
            count+=1
        return (self.reverseList(dummy.next))

