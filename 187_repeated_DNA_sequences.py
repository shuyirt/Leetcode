    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        found = set()
        repeated = set()
        
        for i in range(len(s)-9):
            t = s[i:i+10]
            if t in found:
                repeated.add(t)
            else:
                found.add(t)
        return list(repeated)
# Runtime: 60 ms, faster than 95.39% of Python3 online submissions for Repeated DNA Sequences.
# Memory Usage: 25.2 MB, less than 62.73% of Python3 online submissions for Repeated DNA Sequences.