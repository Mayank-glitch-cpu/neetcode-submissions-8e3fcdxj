class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic= dict.fromkeys(s,0)
        t_dic= dict.fromkeys(t,0)

        # then i  will traverse thorugh s and update the values of keys 
        for string in s:
            s_dic[string]=s_dic[string] + 1 

        # then i will traverse thorugh t and update the values of keys 
        for string in t:
            t_dic[string]=t_dic[string] + 1            

        # now i will sum the values of all the values in respective dictionary
        return s_dic==t_dic                  
