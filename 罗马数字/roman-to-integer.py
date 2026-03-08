"""
蓝桥杯 - 罗马数字转整数
"""

def roman_to_int(s):
    roman_map = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    total = 0
    n = len(s)
    
    for i in range(n):
        if i < n-1 and roman_map[s[i]] < roman_map[s[i+1]]:
            total -= roman_map[s[i]]
        else:
            total += roman_map[s[i]]
    
    return total

if __name__ == "__main__":
    n = int(input().strip())
    for _ in range(n):
        s = input().strip()
        print(roman_to_int(s))
