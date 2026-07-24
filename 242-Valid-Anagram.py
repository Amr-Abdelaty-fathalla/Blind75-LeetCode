class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # firs sol: remove after check(909 ms)
        
        # # edge case
        # if len(s) != len(t):
        #     return False

        # lst_s = []

        # for j in s:
        #     lst_s.append(j)
        
        # for i in t:
        #     if i in lst_s:
        #         lst_s.remove(i)
        
        # if len(lst_s) == 0:
        #     return True
        
        # return False



        # Second Sol: sort(15 ms)
        # srt_s = sorted(s)
        # srt_t = sorted(t)
        
        # if srt_s == srt_t:
        #     return True
        
        # return False


        # Third Solution: hash
        dct_s = {}
        dct_t = {}

        if len(s) != len(t):
            return False

        for i in s:
            if i not in dct_s:
                dct_s[i] = 1
            
            dct_s[i] += 1

        for j in t:
            if j not in dct_t:
                dct_t[j] = 1
            
            dct_t[j] += 1
        
        for m in dct_s:
            if (m not in dct_t) or (dct_s[m] != dct_t[m]):
                return False

        return True  
        
