class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums) + 1)]
        Count = Counter(nums).items()  
        for num, freq in Count: 
            bucket[freq].append(num)
        #print('bucket[freq]', bucket)
        flat_list = [item for sublist in bucket for item in sublist]
        #print('flat_list', flat_list)
        return flat_list[::-1][:k]