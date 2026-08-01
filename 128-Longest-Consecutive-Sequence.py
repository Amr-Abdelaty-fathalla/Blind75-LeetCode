class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # long_seq = []
        # cnt = 1

        # if len(nums) == 0:
        #     return 0
        
        # if len(nums) == 1:
        #     return 1
        
        # nums.sort()
     
        # for idx in range(1, len(nums)):
        #     if nums[idx] - 1 == nums[idx-1]:
        #         cnt += 1
        #     elif nums[idx] == nums[idx-1]:
        #         cnt = cnt
        #     else:
        #         long_seq.append(cnt)
        #         cnt = 1
        
        # long_seq.append(cnt)    
        # return max(long_seq)


        # Second Sol time: O(n)
        hashset = set(nums)
        maxlen = 0

        for num in hashset:
            if num - 1 not in hashset:
                next_num = num + 1

                while next_num in hashset:
                    next_num += 1
                
                maxlen = max(maxlen, next_num - num)
        
        return maxlen


        