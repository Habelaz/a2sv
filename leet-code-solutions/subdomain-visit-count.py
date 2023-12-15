class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        counts = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()
            subdomains = domain.split('.')
            for i in range(len(subdomains)-1, -1, -1):
                curr_subdomain = '.'.join(subdomains[i:])
                if curr_subdomain not in counts:
                    counts[curr_subdomain] = int(count)
                else:
                    counts[curr_subdomain] += int(count)
        
        result = [str(count) + ' ' + domain for domain, count in counts.items()]
        return result
