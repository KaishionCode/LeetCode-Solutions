class Solution:
    def leftRightDifference(self, nums: list[int]) -> list[int]:
        rightsum = sum(nums)
        leftsum = 0
        ketqua = []
        for num in nums:
            rightsum -= num
            ketqua.append(abs(rightsum-leftsum))
            leftsum += num
        return ketqua

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna