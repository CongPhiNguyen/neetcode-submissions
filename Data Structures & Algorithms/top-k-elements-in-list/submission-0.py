class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        key_val = list(counts.items())
        key_val.sort(key = lambda x: x[1], reverse=True)

        return [k[0] for k in key_val[:k]]
