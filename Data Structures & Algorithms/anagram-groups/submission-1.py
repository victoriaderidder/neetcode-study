class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        soln = defaultdict(list)
        for x in strs:
            srted = "".join(sorted(x))
            soln[srted].append(x)
        return [value for value in soln.values()]