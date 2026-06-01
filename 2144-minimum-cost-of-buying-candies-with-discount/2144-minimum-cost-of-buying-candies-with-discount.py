class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        luutru = (sorted(cost)[::-1])
        tong = 0
        for i in range (len(luutru)):
            if (i + 1) % 3 == 0:
                continue
            else: tong += luutru[i]
        return tong

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna