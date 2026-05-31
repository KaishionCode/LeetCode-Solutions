class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s
        luutru = [""] * numRows
        vi_tri_tro = 0
        xu_huong = 1
        for char in s:
            luutru[vi_tri_tro] += char
            if vi_tri_tro == numRows - 1:
                xu_huong = -1
            elif vi_tri_tro == 0:
                xu_huong = 1
            vi_tri_tro += xu_huong
        return "".join(luutru)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna