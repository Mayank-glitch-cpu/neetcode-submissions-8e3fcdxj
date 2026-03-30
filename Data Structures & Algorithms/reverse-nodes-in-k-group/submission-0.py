# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check if there are k nodes ahead
        curr=head
        count=0
        while curr and count<k:
            curr=curr.next
            count+=1
        
        if count<k:
            return head

        prev= None
        curr=head
        nextNode= None 

        for _ in range(k):
            nextNode= curr.next
            curr.next=prev
            prev=curr
            curr=nextNode
        
        head.next= self.reverseKGroup(nextNode,k)

        return prev