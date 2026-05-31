class Solution:
    def romanToInt(self, s: str) -> int:
        luu_tru = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        ket_qua = 0
        do_dai_chuoi = len(s)
        for i in range (do_dai_chuoi):
            if i+1 < do_dai_chuoi and luu_tru[s[i]] < luu_tru[s[i+1]]:
                ket_qua -= luu_tru[s[i]]
            else:
                ket_qua += luu_tru[s[i]]
        return ket_qua


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna