## string

| name    | function                          | usage                            |
| ------- | --------------------------------- | -------------------------------- |
| split   | split string into two             | local, domain = email.split('@') |
| replace | replace a substr with another one | local.replace('.','')            |
| index   | get the index of substr in a str  | email.index('@')                 |
| join    | join strs                         | '.'.join(list)                   |
| lower   |                                   |                                  |

## Set

| name           | usage        |
| -------------- | ------------ |
| define set     | name = set() |
| add x into set | name.add(x)  |
|                |              |



## Dict

| Function            | usage                                                        |
| ------------------- | ------------------------------------------------------------ |
| dict to list of str | return[ "{} {}".format(key,value) for key, value in visited.items()] |
| member              | if key in dict                                               |
|                     |                                                              |

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)