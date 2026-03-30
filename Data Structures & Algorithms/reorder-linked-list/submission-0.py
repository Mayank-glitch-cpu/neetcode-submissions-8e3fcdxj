# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self,head):
        prev= None
        curr = head
        while curr:
            temp= curr.next
            curr.next= prev
            prev=curr
            curr=temp
        return prev

    def merge(self,l1,l2):
        while l2:
            temp1=l1.next
            temp2=l2.next

            l1.next=l2
            l2.next= temp1

            l1=temp1
            l2=temp2

    def reorderList(self, head: Optional[ListNode]) -> None:
        l1=slow=head
        fast= head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        l2= slow.next
        slow.next=None
        rl2=self.reverseList(l2)
        self.merge(l1,rl2)


        