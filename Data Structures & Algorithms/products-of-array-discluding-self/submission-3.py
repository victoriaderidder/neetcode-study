class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #   my soln:
        # res = []
        # for x in range(len(nums)):
        #     index = 0
        #     product = 1
        #     while index < len(nums):
        #         if x != index:
        #             product *= nums[index]
        #         index += 1
        #     res.append(product)
        # return res

        # neetcode soln:
        res = [1] * len(nums)

        # prefix = values before i
        # postfix = values after i
        # we could do this in two arrays prefix[] + postfix[]
        # but memory of res[] doesn't count against you
        # (though that doesn't seem to be called out in the question...)
        # so we are just using one array res[]
        prefix, postfix = 1, 1

        for i in range(len(nums)):
            # i want to get the numbers before i
            # assuming [3, 1, 2, 3]
            res[i] = prefix
            # prefix = 1, res[0] = 1
            # prefix = 3, res[1] = 3
            # prefix = 3, res[2] = 3
            # prefix = 6, res[3] = 6
            prefix *= nums[i]
        
        # start at end of input array; go to beginning
        for i in range(len(nums) -1, -1, -1):
            # i want to get the numbers after i
            # assuming [3, 1, 2, 3]
            res[i] *= postfix
            # postfix = 1, res[3] = 6
            # postfix = 3, res[2] = 9
            # postfix = 6, res[1] = 18
            # postfix = 6, res[0] = 6
            postfix *= nums[i]
        
        # assuming [3, 1, 2, 3], res = [6, 9, 18, 6].
        return res

        