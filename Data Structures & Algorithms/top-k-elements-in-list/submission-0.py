class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first made a freq_map of the numbers in mums 
        freq_map={}
        for num in nums:
            if num in freq_map:
                freq_map[num]+=1
            else:
                freq_map[num]=1
        # print(freq_map)

        # now make max frequency +1 buckets
        max_freq= max(freq_map.values())
        buckets= [[] for i in range(max_freq+1)]

        print(buckets)
        # Now place the numbers based on their frequency in the buckets 
        for key, value in freq_map.items():
            buckets[value].append(key)
        # print("len of bucket",len(buckets))
        # print(buckets)
        result=[]
    
        # Now return the top k buckets travelling from end (most frequent) to k 
        for i in range(len(buckets)-1,0,-1): # from highest freq to lowest
            for num in buckets[i]: 
                result.append(num)
                if len(result)==k:
                    return result
        # print(result)
