class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # First Sol: O(n)
        if len(nums) == 0:
            return []

        top_k_dct = {}

        for num in nums:
            if num not in top_k_dct:
                top_k_dct[num] = 1
            
            else:
                top_k_dct[num] += 1
        
        top_k_srt= sorted(top_k_dct.items(), key= lambda item: item[1], reverse= True)
        top_k_srt = top_k_srt[:k]
        

        return [item[0] for item in top_k_srt]

        
        