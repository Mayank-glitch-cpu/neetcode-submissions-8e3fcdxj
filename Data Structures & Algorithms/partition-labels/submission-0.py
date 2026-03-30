class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index= {}

        for i , c in enumerate(s):
            last_index[c]=i

        size=0
        current_max=0
        res=[]

        for i in range(len(s)):
            current_max= max(current_max, last_index[s[i]])
            # print("current max for ", s[i], " is ", current_max, " and i =", i)
            if i==current_max:
                res.append(size+1)
                size=0
            else:
                size+=1
        # print(res)
        return res