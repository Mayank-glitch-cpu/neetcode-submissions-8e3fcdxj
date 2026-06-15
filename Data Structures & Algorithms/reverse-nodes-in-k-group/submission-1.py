# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr= head
        count=0

        while curr and count<k:
            curr= curr.next
            count +=1

        if count<k:
            return head

        prev= None
        curr= head
        nextnode= None

        for _ in range(k):
            nextnode= curr.next
            curr.next= prev
            prev= curr
            curr= nextnode

        head.next = self.reverseKGroup(nextnode, k)

        return prev
