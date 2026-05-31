# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        luutru = ListNode(0)
        capnhat = luutru
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                capnhat.next = list1
                list1 = list1.next
            else:
                capnhat.next = list2
                list2 = list2.next
            capnhat = capnhat.next
        if list1 is not None:
            capnhat.next = list1
        elif list2 is not None:
            capnhat.next = list2
        return luutru.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna