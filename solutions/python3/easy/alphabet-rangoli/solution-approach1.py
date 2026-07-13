# ──────────────────────────────────────────────────
# Link        https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true
# Problem     Alphabet Rangoli
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-13, 05:44 p.m.
# ──────────────────────────────────────────────────

def print_rangoli(size):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
    
    x = alpha[size-1 : 0 : -1] + alpha[0 : size]
    string = "-".join(x)
    
    a = string
    
    length =len(string) 
    
    for i in range(1, size):
        string =  (alpha[size-1 : size -i : -1] + alpha[size-i : size])
        print("-".join(string).center(length, "-"))
        
    print("-".join(alpha[size-1 : 0 : -1] + alpha[0 : size]))
        
    for i in range(size , 1 , -1):
        x = "-".join(alpha[size-1 : size - i +1 : -1] + alpha[size-i + 1:size])
        print(x.center(length, "-"))
    
    
    
