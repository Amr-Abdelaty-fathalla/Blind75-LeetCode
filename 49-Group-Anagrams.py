class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # First Sol: O(n^2) -> Time Limit Exceed case: 113
        # grp_lst = []
        # tiny_lst = []

        # arr_len = len(strs)

        # for i in range(arr_len):
        #     should_skip = False

        #     for tn_lst in grp_lst:
        #         if strs[i] in tn_lst:
        #             should_skip = True
        #             break
            
        #     if should_skip:
        #         continue
            
        #     if i == arr_len-1:
        #         grp_lst.append([strs[i]])
        #         return grp_lst
            
        #     tiny_lst = [strs[i]]
        #     for j in range(i+1, arr_len):
        #         if sorted(strs[i]) == sorted(strs[j]):
        #             tiny_lst.append(strs[j])
    
        #     grp_lst.append(tiny_lst)
        
        # return grp_lst

        # Second Sol: O(n)
        grp_dct = {}

        for st_ele in strs:
            srt_st_ele = "".join(sorted(st_ele))

            if  srt_st_ele not in grp_dct:
                grp_dct[srt_st_ele] = [st_ele]
            
            else:
                grp_dct[srt_st_ele] = grp_dct.get(srt_st_ele) + [st_ele]

        return list(grp_dct.values())
            