import heapq
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap =[]
        for i in range (len(lists)):
            if lists[i] is not None:
                heapq.heappush(heap,(lists[i].val,i,lists[i]))

        luutru = ListNode(0)
        capnhat = luutru

        while heap:
            val,i,node = heapq.heappop(heap) 

            capnhat.next = node
            capnhat = capnhat.next

            if node.next is not None:
                heapq.heappush(heap,(node.next.val,i,node.next))
        return luutru.next


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna