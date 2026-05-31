class Solution:
    def reverse(self, x: int) -> int:
        y = str(x)
        if x < 0:
            kq = int ('-' + y[:0:-1])
        else:  
            kq= int(y[::-1])
        if kq < -2 ** 31 or kq > 2**31-1:
            return 0
        return kq

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna