# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: None Do not return anything, modify head in-place instead.
        """
        arr = []
        temp = head
        while temp:
            arr.append(temp)
            temp = temp.next
        left = 0
        right = len(arr) - 1
        while left < right:
            arr[left].next = arr[right]
            left += 1
            if left == right:
                break
            arr[right].next = arr[left]
            right -= 1
        arr[left].next = None