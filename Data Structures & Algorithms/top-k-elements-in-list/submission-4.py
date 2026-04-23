from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_list = dict(Counter(nums))
        sorted_dict = dict(sorted(nums_list.items(), key=lambda item: item[1]))
        print(sorted_dict)
        return list(sorted_dict)[::-1][:k]
        