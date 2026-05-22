class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        count_map = {}
        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1
            
        sorted_count_map = sorted(count_map.items(), key=lambda item: item[1], reverse=True) 

        result = []
        for num in range(k):
            result.append(sorted_count_map[num][0])
        return result

        
        