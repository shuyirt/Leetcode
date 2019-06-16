class Solution:
    def myAtoi(self, str: str) -> int:
        a = str.strip()
        if not a or a[0].isalpha():
            return 0
        
        is_negative = False
        if a[0] == '-' or a[0] == '+':
            if a[0] == '-':
                is_negative = True
            a = a[1:]
        
        count = 0 
        for v in a:
            if v.isdigit():
                count = count+v
            else:
                break
        count = count * -1 if is_negative else count
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        
        if count > INT_MAX:
            return INT_MAX
        elif count < INT_MIN:
            return INT_MIN
        else:
            return count

# Runtime: 44 ms 77.82%
# Memory Usage: 13.3 MB 39.79%