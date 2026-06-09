class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        min_len = float ('inf')
        max_len = float ('-inf')
        for i in nums:
            if i < min_len: min_len = i
            if i > max_len: max_len = i
        return (max_len - min_len) * k

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna