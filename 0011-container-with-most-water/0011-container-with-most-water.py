class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_rs = 0
        while (i <= j):
            min_high = min(height[i],height[j])
            ket_qua = min_high * (j-i)
            if ket_qua > max_rs:  max_rs = ket_qua
            if height[i] == height[j]:
                i+=1
                j-=1
            elif height[i] == min_high:
                i+=1
            elif height[j] == min_high:
                j-=1
        return max_rs

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna