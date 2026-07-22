# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true
# Problem     itertools.product()
# Difficulty  Easy
# Subdomain   Itertools
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-22, 04:21 p.m.
# ──────────────────────────────────────────────────

from itertools import product

A = list(map(int , (input().split())))
B = list(map(int , (input().split())))

axb = list(product(A,B))

for i in axb:
  print(i , end = " ")
  
