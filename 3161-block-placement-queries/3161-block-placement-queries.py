from sortedcontainers import SortedList
from typing import List
class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (2 * n)
    def update(self, pos, value):
        pos += self.n
        self.tree[pos] = value
        pos //= 2
        while pos > 0:
            self.tree[pos] = max(self.tree[2 * pos], self.tree[2 * pos + 1])
            pos //= 2    
    def query(self, left, right):
        res = 0
        left += self.n
        right += self.n
        while left < right:
            if left % 2 == 1:
                res = max(res, self.tree[left])
                left += 1
            if right % 2 == 1:
                right -= 1
                res = max(res, self.tree[right])
            left //= 2
            right //= 2
        return res
class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = max(q[1] for q in queries) + 1
        st = SegmentTree(max_x)
        sl = SortedList([0])
        ket_qua = []
        for q in queries:
            if q[0] == 1:
                x = q[1]
                idx = sl.bisect_right(x)
                prev = sl[idx - 1]
                nxt = sl[idx] if idx < len(sl) else None
                sl.add(x)
                st.update(x, x - prev)
                if nxt is not None:
                    st.update(nxt, nxt - x)
            else:
                x, sz = q[1], q[2]
                idx = sl.bisect_right(x)
                prev = sl[idx - 1]
                max_gap = st.query(0, prev + 1)
                if max(max_gap, x - prev) >= sz:
                    ket_qua.append(True)
                else:
                    ket_qua.append(False)
        return ket_qua

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna