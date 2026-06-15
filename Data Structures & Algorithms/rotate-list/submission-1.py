# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        curr = tail = head
        length= 0
        while curr:
            length +=1
            tail = curr
            curr= curr.next

        k = k % length

        if k ==0:
            return head

        dummy = ListNode(0)
        curr= head

        idx =0

        while curr:
            if idx == (length -k -1):
                next_part= curr.next
                curr.next= None
                tail.next = head
                dummy.next= next_part
                return dummy.next
            idx+=1
            curr= curr.next