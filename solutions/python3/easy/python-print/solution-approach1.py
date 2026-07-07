# ──────────────────────────────────────────────────
# Problem     Print Function
# Difficulty  Easy
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-07, 05:36 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    i = 1
    sting = ""
    while(i <= n):
        sting = sting + str(i)
        i += 1
    print(sting)
