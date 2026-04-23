class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        soln = dict()
        for x in strs:
            srted = "".join(sorted(x))
            if srted in soln:
                soln[srted].append(x)
            else:
                soln[srted] = [x]
        return [value for value in soln.values()]