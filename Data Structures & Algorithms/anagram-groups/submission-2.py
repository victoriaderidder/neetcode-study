class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        soln = defaultdict(list)
        for x in strs:
            count = [0] * 26
            for c in x:
                count[ord(c) - ord('a')] += 1
            soln[tuple(count)].append(x)
        return [value for value in soln.values()]