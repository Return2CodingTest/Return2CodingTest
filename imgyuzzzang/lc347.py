#347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        sortedKeys= list(dict(sorted(frequency.items(), key=lambda item: -item[1])).keys())
        
        return sortedKeys[:k]
            