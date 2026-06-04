from functools import cache
class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def countWaviness(num: int) -> int:
            if num < 100:
                return 0
            s = str(num)
            @cache
            def dfs(idx: int, pp: int, p: int, tight: bool, lz: bool) -> tuple[int, int]:
                if idx == len(s):
                    return 1, 0 
                limit = int(s[idx]) if tight else 9
                total_cnt = 0
                total_wav = 0
                for c in range(limit + 1):
                    new_tight = tight and (c == limit)
                    new_lz = lz and (c == 0)
                    new_p = 10 if new_lz else c
                    new_pp = 10 if new_lz else (10 if lz else p)
                    added_waviness = 0
                    if pp != 10 and p != 10 and not new_lz:
                        if (p > pp and p > c) or (p < pp and p < c):
                            added_waviness = 1
                    cnt, wav = dfs(idx + 1, new_pp, new_p, new_tight, new_lz)
                    total_cnt += cnt
                    total_wav += wav + added_waviness * cnt
                return total_cnt, total_wav
            return dfs(0, 10, 10, True, True)[1]
        return countWaviness(num2) - countWaviness(num1 - 1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna