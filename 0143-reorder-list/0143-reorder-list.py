# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_LL(self,head):
        prev=None
        temp=head
        while temp:
            curr=temp.next
            temp.next=prev
            prev=temp
            temp=curr
        return prev
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        slow=head
        fast=head
        while fast and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        second=self.reverse_LL(slow.next)
        slow.next=None
        first=head
        while second:
            temp=first.next
            first.next=second
            first=second
            second=second.next
            first.next=temp
            first=temp