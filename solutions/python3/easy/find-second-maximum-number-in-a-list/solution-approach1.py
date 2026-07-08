# ──────────────────────────────────────────────────
# Problem     Find the Runner-Up Score!  
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-08, 12:51 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    Ulist = set(arr)
    sortedlist = sorted(Ulist) 
    
    runner = sortedlist[-2]
    print(runner)
    
    
