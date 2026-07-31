class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        long_seq = []
        cnt = 1

        if len(nums) == 0:
            return 0
        
        nums.sort()
     
        for idx in range(1, len(nums)):
            if nums[idx] - 1 == nums[idx-1]:
                cnt += 1
            elif nums[idx] == nums[idx-1]:
                cnt = cnt
            else:
                long_seq.append(cnt)
                cnt = 1
            
        long_seq.append(cnt)    
        return max(long_seq)


        