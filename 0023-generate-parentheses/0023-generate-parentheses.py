class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        luutru = []
        def quaylui(chuoi_hien_tai, so_ngoac_mo, so_ngoac_dong):
            if len(chuoi_hien_tai) == n*2:
                luutru.append(chuoi_hien_tai)
                return
            
            if so_ngoac_mo < n:
                quaylui(chuoi_hien_tai + '(',so_ngoac_mo + 1, so_ngoac_dong)
            
            if so_ngoac_mo > so_ngoac_dong:
                quaylui(chuoi_hien_tai + ')',so_ngoac_mo , so_ngoac_dong+1)
            
        quaylui('',0,0)
        return luutru

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna