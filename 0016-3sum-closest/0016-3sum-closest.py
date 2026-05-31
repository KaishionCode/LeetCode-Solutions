class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        ket_qua = float('inf')
        ketqua = 0
        n = len(nums)
        for i in range (n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i+1
            r = n-1
            while (l<r):
                tong = nums[i] + nums[l] + nums[r]
                hieu = tong - target
                check = abs(hieu)
                if check < ket_qua:
                    ket_qua = check
                    ketqua = tong
                if hieu > 0:
                    r -= 1
                elif hieu < 0:
                    l += 1
                else: break
        return ketqua

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna