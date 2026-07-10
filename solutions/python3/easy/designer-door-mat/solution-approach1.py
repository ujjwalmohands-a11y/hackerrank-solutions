# ──────────────────────────────────────────────────
# Problem     Designer Door Mat
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-10, 01:13 p.m.
# ──────────────────────────────────────────────────

n , m = input().split()
n = int(n)
m = int(m)

p = '.|.'

for i in range (1 , n // 2 + 1):
  x = p * (2 * i - 1)
  print ((x).center(m , '-'))
print("WELCOME".center(m, "-"))
for i in range(n//2 ,0 , - 1):
  x = p * (2 * i - 1)
  print((x).center(m , "-"))
