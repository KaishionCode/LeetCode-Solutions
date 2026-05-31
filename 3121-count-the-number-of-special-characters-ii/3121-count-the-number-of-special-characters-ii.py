class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chu_thuong_cuoi = {}
        chu_hoa_dau = {}
        for i,chu in enumerate(word):
            if chu.islower():
                chu_thuong_cuoi[chu] = i
            if chu.isupper() and chu not in chu_hoa_dau:
                chu_hoa_dau[chu] = i
        dem = 0
        for chu,j in chu_thuong_cuoi.items():
            chu_hoa = chu.upper() 
            if chu_hoa in chu_hoa_dau and j < chu_hoa_dau[chu_hoa]:
                dem += 1
        return dem  



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna