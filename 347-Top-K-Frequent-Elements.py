class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First Sol: O(n)
        cnt_dct = {}

        if len(nums) == 0:
            return []

        for num in nums:
            if num not in cnt_dct:
                cnt_dct[num] = 1
            
            else:
                cnt_dct[num] += 1
        
        srt_cnt_dct = sorted(cnt_dct.items(), key = lambda item: item[1], reverse= True)
        return [item[0] for item in srt_cnt_dct[:k]]

        
        