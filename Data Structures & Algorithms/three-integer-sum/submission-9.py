class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force = 3 for loops
        # better solution = 2 pointers?? but there are 3 values needed? so 3 pointers...?
        # my attempt:
        # nums_sort = sorted(nums)
        # l, m, r = 0, 1, len(nums)-1
        # output = []
        # while m < r:
        #     print(m, r)
        #     if nums_sort[l] + nums_sort[m] + nums_sort[r] > 0:
        #         r -= 1
        #         m += 1
        #     if nums_sort[l] + nums_sort[m] + nums_sort[r] < 0:
        #         l += 1
        #         print(l)
        #     if nums_sort[l] + nums_sort[m] + nums_sort[r] == 0:
        #         output += [[nums_sort[l], nums_sort[m], nums_sort[r]]]
        #         l += 1
        #         r -= 1
        #         m += 1
        # print(output)
        # return output

        # after watching the video:
        output = []

        # O(nlogn) to sort
        nums.sort()
        
        # O(n squared) to loop
        # so complexity reduces to O(n squared)
        for i, a in enumerate(nums):
            
            # skip duplicate values on the left
            if i > 0 and a == nums[i - 1]:
                continue
            
            # two pointer solution:
            l, r = i+1, len(nums)-1
            while l < r:
                threesum = a + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                elif threesum == 0:
                    output.append([a, nums[l], nums[r]])
                    l += 1
                    # avoid duplicates
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

            
        return output