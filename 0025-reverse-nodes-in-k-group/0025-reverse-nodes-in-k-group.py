# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        luutru = ListNode(0)
        luutru.next = head
        fast = luutru
        slow = head
        while fast.next is not None:
            luu2 = slow
            luu = slow
            truoc_do = fast
            for i in range(k):
                fast = fast.next
                if fast is None: break
            if fast is None: break
            truoc_do.next = fast
            slow = slow.next
            luu.next = fast.next
            for i in range(k-1):
                luu1 = slow
                slow = slow.next
                luu1.next = luu
                luu = luu1
            fast = luu2
            slow = fast.next
        return luutru.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna