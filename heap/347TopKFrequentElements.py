# 📖 Problem
# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# 💻
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# Output: [1,2]

import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        heap = []

        for num, frequency in count.items():
            heapq.heappush(heap, (frequency, num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [num for frequency, num in heap]