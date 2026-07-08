# ──────────────────────────────────────────────────
# Problem     Lists
# Difficulty  Easy
# Subdomain   Basic Data Types
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-08, 03:12 p.m.
# ──────────────────────────────────────────────────

if __name__ == '__main__':
    N = int(input())
    list =[]
    
    for _ in range(N):
         
        parts = input().split()
            
        if (parts[0] == 'insert'):
            i = int(parts[1])
            e = int(parts[2])                
            list.insert(i , e)
           
        elif (parts[0] == 'remove'):
            e = int(parts[1])                
            list.remove(e)
             
        elif (parts[0] == 'append'):
            e = int(parts[1])                
            list.append(e)
               
        elif (parts[0] == 'sort'):
            list.sort()
              
        elif (parts[0] == 'pop'):
            list.pop()
               
        elif (parts[0] == 'reverse'):
            list.reverse()
        elif (parts[0] == 'print'):
            print(list)        
                 
                
                
                
                
                
                
                
