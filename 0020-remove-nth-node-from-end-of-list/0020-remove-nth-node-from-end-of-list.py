# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        goc = ListNode(0)
        goc.next = head
        slow = goc
        fast = goc
        for i in range (n+1):
            fast = fast.next
        while (fast is not None):
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next

        return goc.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna