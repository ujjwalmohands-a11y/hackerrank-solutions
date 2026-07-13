# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true
# Problem     Capitalize!
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-13, 06:16 p.m.
# ──────────────────────────────────────────────────



# Complete the solve function below.
def solve(s):
    list = s.split(' ')
    length = len(list)
    for i in range(length):
        list[i] = list[i].capitalize()

        
    return(" ".join(list))

