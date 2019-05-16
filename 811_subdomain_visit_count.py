class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        visited = {}
        for cpdomain in cpdomains:
            (visit, domain) = cpdomain.split(' ')

            pieces = domain.split('.')
            for i in range(len(pieces)):
                visit = int(visit)
                x = '.'.join(pieces[i:])
                if x in visited:
                    visited[x] += visit
                else:
                    visited[x] = visit

        return ["{} {}".format(value, key) for key, value in visited.items()]

'''
    Runtime: 48 ms, faster than 92.25% of Python online submissions for Subdomain Visit Count.
    Memory Usage: 11.9 MB, less than 25.81% of Python online submissions for Subdomain Visit Count.
'''