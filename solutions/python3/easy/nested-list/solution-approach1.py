# ──────────────────────────────────────────────────
# Problem     Nested Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-08, 02:03 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    Records = []
    same = []
    scores = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        Records.append([name , score])
     
    
    for x in Records:
        scores.append(x[1])
        
    UsortedScores = sorted(set(scores))
    

    S_lowest = UsortedScores[1]
    
    for x in Records:
        if (x[1] == S_lowest):
            same.append(x[0])
            
    same.sort()
    
    for _ in same:
        print(_)
    
    
