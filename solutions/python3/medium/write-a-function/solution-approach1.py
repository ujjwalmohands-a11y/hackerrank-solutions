# ──────────────────────────────────────────────────
# Problem     Write a function
# Difficulty  Medium
# Subdomain   Introduction
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-07, 05:38 p.m.
# ──────────────────────────────────────────────────

def is_leap(year):
    leap = False
    
    if(year % 4 == 0):
       if(year % 100 == 0):
            if(year % 400 == 0):
                leap = True
            else:
                leap = False 
       else:
        leap = True
    else:
      leap = False           
        
    
    return leap

