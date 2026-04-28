class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # a solution for a different problem
        # res = 0
        # res_set = collections.defaultdict(set)
        # for x in nums:
        #     if res_set.get(x-1):
        #         print(x-1, x)
        #         print(res_set.get(x-1))
        #         res_set[x].add(x)
        #         res_set[x].update(res_set.get(x-1))
        #     else: res_set[x].add(x)
        #     if len(res_set[x]) > res:
        #         res = len(res_set[x])
        # return res

        # check to see if x in nums has a left neighbor
        # if no, it is the beginning of a sequence
        num_set = set(nums)
        res = 0
        for n in num_set:
            if (n-1) not in num_set:
                length = 0
                while (n + length) in num_set:
                    length += 1
                if length > res:
                    res = length
        return res
        