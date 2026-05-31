class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        ket_qua = []
        n = len(nums)
        for i in range (n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range (i+1,n-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                
                l = j + 1
                r = n - 1

                while (l<r):
                    tong = nums[i] + nums[j] + nums[l] + nums[r]
                    if tong - target < 0:
                        l += 1
                    elif tong - target > 0:
                        r -= 1
                    else:
                        ket_qua.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l+= 1
                        while l < r and nums[r] == nums[r-1]:
                            r-= 1
                        l += 1
                        r -= 1
        return ket_qua


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna