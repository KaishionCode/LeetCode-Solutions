class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        vetrai = []
        vegiua = []
        vephai = []
        for i in nums:
            if i < pivot: vetrai.append(i)
            if i == pivot: vegiua.append(i)
            if i > pivot: vephai.append(i)
        ketqua = vetrai+vegiua+vephai
        return ketqua

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna