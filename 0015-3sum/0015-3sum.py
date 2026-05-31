class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ket_qua = []
        for i in range (n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = n - 1

            while l < r:
                tong = nums[l] + nums[r] + nums[i]
                if tong > 0:
                    r -=1
                elif tong < 0:
                    l += 1
                else:
                    ket_qua.append([nums[l],nums[r],nums[i]])
                    while l < r and nums[l] == nums[l+1]:
                        l+= 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l+=1
                    r-=1
        return ket_qua
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna