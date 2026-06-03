import bisect
from typing import List

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def get_min_time(start_A, dur_A, start_B, dur_B):
            B = sorted(zip(start_B, dur_B))
            m = len(B)
            b_starts = [x[0] for x in B]
            b_durs = [x[1] for x in B]
            prefix_min_dur = [float('inf')] * m
            curr_min = float('inf')
            for i in range(m):
                curr_min = min(curr_min, b_durs[i])
                prefix_min_dur[i] = curr_min
            suffix_min_finish = [float('inf')] * m
            curr_min = float('inf')
            for i in range(m - 1, -1, -1):
                curr_min = min(curr_min, b_starts[i] + b_durs[i])
                suffix_min_finish[i] = curr_min
            min_total_time = float('inf')
            for i in range(len(start_A)):
                finish_A = start_A[i] + dur_A[i]
                idx = bisect.bisect_right(b_starts, finish_A)
                best_if_B_open = float('inf')
                best_if_B_wait = float('inf')
                if idx > 0:
                    best_if_B_open = finish_A + prefix_min_dur[idx - 1]
                if idx < m:
                    best_if_B_wait = suffix_min_finish[idx]
                min_total_time = min(min_total_time, best_if_B_open, best_if_B_wait)
                
            return min_total_time
        ans1 = get_min_time(landStartTime, landDuration, waterStartTime, waterDuration)
        ans2 = get_min_time(waterStartTime, waterDuration, landStartTime, landDuration)
        return min(ans1, ans2)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna