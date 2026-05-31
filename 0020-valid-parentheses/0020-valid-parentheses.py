class Solution:
    def isValid(self, s: str) -> bool:
        luutru = []
        mapping = {')':'(','}':'{',']':'['}
        for char in s:
            if char in mapping:
                ki_tu_cuoi = luutru.pop() if luutru else '#'
                if mapping[char] != ki_tu_cuoi: return False
            else:
                luutru.append(char)
        return not luutru

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna