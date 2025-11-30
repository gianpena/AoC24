from functools import cache
from aocinput import AOCInput

patterns = []

def possible(line):
    n = len(line)

    @cache
    def dp(i):
        if i >= n: return 1

        ans = 0
        for j in range(i+1,n+1):
            if line[i:j] in patterns:
                ans += dp(j)

        return ans

    return dp(0)

input = AOCInput(2024, 19)

ans = 0
lines = [line for line in input.lines()]
patterns = set(lines[0].split(', '))
for line in lines[2:]:
    ans += possible(line)

print(ans)