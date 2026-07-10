# ──────────────────────────────────────────────────
# Problem     String Formatting
# Difficulty  Easy
# Subdomain   Strings
# Platform    HackerRank
# Language    python3
# Status      Accepted
# Submitted   2026-07-10, 02:04 p.m.
# ──────────────────────────────────────────────────

def print_formatted(number):
    width = number.bit_length()
    strng = '' 
    for i in range(1 ,number + 1):
        octal = oct(i)[2:]
        binary = bin(i)[2:]
        hexa = hex(i).upper()[2:]
        strng = ''
        strng = str(i).rjust(width, " ") +" "+ str(octal).rjust(width, " ") +" "+ str(hexa).rjust(width, " ") +" "+ str(binary).rjust(width, " ")
        print(strng)
    
