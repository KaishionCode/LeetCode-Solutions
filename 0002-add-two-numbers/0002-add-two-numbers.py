# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        luutru = ListNode(0)
        hien_tai = luutru
        nho = 0
        while l1 is not None or l2 is not None: 
            so1 = l1.val if l1 is not None else 0
            so2 = l2.val if l2 is not None else 0
            tong = so1 + so2 + nho
            ketqua = tong % 10
            nho = tong // 10
            hien_tai.next = ListNode(ketqua)
            hien_tai = hien_tai.next
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        if nho > 0:
            hien_tai.next = ListNode(nho)
        return luutru.next

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna