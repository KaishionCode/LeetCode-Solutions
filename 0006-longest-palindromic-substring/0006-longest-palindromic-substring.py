class Solution:
      def longestPalindrome(self, s: str) -> str:
        max_len = luui= luuj = 0
        def check (i,j):
            nonlocal max_len,luui,luuj
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i-=1
                j+=1
            temp_max = j - i - 1
            if temp_max > max_len: 
                max_len = temp_max
                luui = i + 1
                luuj = j
        for i in range (len(s)):
            check (i,i)
            check (i,i+1)
        return s[luui:luuj]
            
                
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna