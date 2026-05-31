class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        i = 31
        ketqua = 0
        checked = (dividend < 0) != (divisor < 0)
        divisor = abs(divisor)
        dividend = abs (dividend)
        while i >= 0:
            luu = divisor << i
            if dividend >= luu :
                dividend -= luu
                ketqua += (1 << i)
            i -= 1
        if checked: ketqua = -ketqua
        return ketqua


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna