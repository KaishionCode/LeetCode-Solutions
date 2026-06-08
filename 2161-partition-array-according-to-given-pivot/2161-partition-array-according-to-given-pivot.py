class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        return [x for x in nums if x < pivot] + \
               [x for x in nums if x == pivot] + \
               [x for x in nums if x > pivot]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna