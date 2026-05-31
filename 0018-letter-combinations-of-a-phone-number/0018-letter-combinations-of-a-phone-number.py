class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        luu_tru = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wzxy'}
        ket_qua = []

        def quaylui(vi_tri,chuoi_hien_tai):
            if vi_tri == len(digits):
                ket_qua.append(chuoi_hien_tai)
                return
            
            cac_chu_cai = luu_tru[digits[vi_tri]]

            for chu in cac_chu_cai:
                quaylui(vi_tri + 1, chuoi_hien_tai + chu)
        
        quaylui(0,'')
        return ket_qua
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna