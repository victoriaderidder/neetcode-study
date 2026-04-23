from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # my initial soln:
        # nums_list = dict(Counter(nums))
        # sorted_dict = dict(sorted(nums_list.items(), key=lambda item: item[1]))
        # print(sorted_dict)
        # return list(sorted_dict)[::-1][:k]

        # neetcode video approach: heap the same size as input array
        freq = [[] for i in range((len(nums) + 1))]
        
        #hash map for count
        # ({} is another way to do dict() apparently)
        count = {}

        for x in nums:
            # 0 is a default value here: 
            # if x is not already in count{} set it to 0
            count[x] = 1 + count.get(x, 0)

        # go through key-value pairs in count
        for x, c in count.items():
            # remember the index here is the count!
            # ex. if nums is [7, 4, 4, 3]
            # then count[1] = [7, 3]
            freq[c].append(x)

        res = []

        # this is syntax for: use length of freq-1 as start
        # go down to index 0
        # decrement by -1 each time
        for x in range(len(freq) - 1, 0, -1):
            # go thru freq sublists
            for n in freq[x]:
                res.append(n)
                if len(res) == k:
                    return res