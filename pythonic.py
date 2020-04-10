# bulk definition
left, right = 0, len(s) - 1
left, right = left + 1, right - 1

# swap
s[left], s[right] = s[right], s[left]


# counter
hashtable = collections.Counter(arr)
sum(hashtable.values)