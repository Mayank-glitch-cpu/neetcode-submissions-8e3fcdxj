# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0)
        out = dummy
        head1= list1
        head2= list2

        while head1!=None and head2!=None:
        
            if head1.val > head2.val:
                out.next= head2
                head2= head2.next

            else:
                out.next=head1
                head1= head1.next
            out= out.next
        out.next= head1 if head1 else head2
        return dummy.next
