class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        luu_tru = {}
        def check(i,j):
            if (i,j) in luu_tru:
                return luu_tru[(i,j)]
            if j == len(p):
                return i == len(s)
            
            dung = i < len(s) and p[j] in {s[i],'.'}

            if j+1 < len(p) and p[j+1] == '*':
                ket_qua = check(i,j+2) or (dung and check(i+1,j))
            else: ket_qua = dung and check(i+1,j+1)

            luu_tru[(i,j)] = ket_qua
            return ket_qua
        return check(0,0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna