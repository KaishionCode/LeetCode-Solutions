class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        luutru = set()
        j = 0
        max = 0
        for i in range (len(s)):
            while s[i] in luutru:
                luutru.remove (s[j])
                j+=1
            luutru.add(s[i])
            soluong = i - j + 1
            if soluong > max: max = soluong
        return max


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna