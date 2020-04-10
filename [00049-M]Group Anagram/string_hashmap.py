class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_mapping = {}

        
        for item in strs:
            # sort the string
            sorted_string = ''.join(sorted(item))
            
            # append the sorted string in the hashmap
            if sorted_string not in anagram_mapping:
                anagram_mapping[sorted_string] = []
            anagram_mapping[sorted_string].append(item)

        return anagram_mapping.values()


# time: O(n x N), n = number of string
# space: O(1)
# Runtime: 92 ms  95.79 % 
# Memory Usage: 17.2 MB
# method: hash map, it is more scalable solution incase the time of mapping increases