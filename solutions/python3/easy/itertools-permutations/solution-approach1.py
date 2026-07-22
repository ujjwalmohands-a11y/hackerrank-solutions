# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
# Problem     itertools.permutations()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-22, 04:55 p.m.
# ──────────────────────────────────────────────────

from itertools import permutations

breakInput = (input().split())


A = sorted(list(permutations(breakInput[0] , int(breakInput[1]))))
l = []
for i in A:
  l.append("".join(i))

for _ in l: print(_)

