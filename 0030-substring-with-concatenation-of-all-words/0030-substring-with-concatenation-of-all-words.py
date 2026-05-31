from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        word_len = len(words)
        char_len = len(words[0])
        luu_tru = Counter(words)
        ketqua = []
        for i in range (char_len):
            l = i
            r = i
            dem = Counter()
            da_dem = 0
            while r + char_len <= len(s):
                word = s[r:r+char_len]
                r += char_len
                if word in luu_tru:
                    dem[word] += 1
                    da_dem += 1
                    while dem[word] > luu_tru[word]:
                        tam = s[l:l+char_len]
                        dem[tam] -= 1
                        da_dem -= 1
                        l += char_len
                    if da_dem == word_len:
                        ketqua.append(l)     
                else:
                    dem.clear()
                    da_dem = 0
                    l=r
        return ketqua

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna