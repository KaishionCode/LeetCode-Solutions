class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        luutru = {}
        for j,so_hien_tai in enumerate(nums):
            so_can_tim = target - so_hien_tai
            if so_can_tim in luutru:
                i = luutru[so_can_tim]
                return [i,j]
            luutru[so_hien_tai] = j 
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna