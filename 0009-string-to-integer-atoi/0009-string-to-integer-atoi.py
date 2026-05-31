class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        s= s.lstrip()
        if s == '': return 0
        sign = 1
        limit_min = -2**31
        limit_max = 2**31-1
        if s[i] == '-': 
            sign = -1
            i = 1
        elif s[i] == '+': i = 1
        ketqua = 0
        while i < len(s) and '0' <= s[i] <= '9':
            ketqua = ketqua * 10 + int(s[i])
            if ketqua*sign < limit_min: return limit_min
            elif ketqua*sign > limit_max: return limit_max
            i+=1
        return ketqua * sign

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna