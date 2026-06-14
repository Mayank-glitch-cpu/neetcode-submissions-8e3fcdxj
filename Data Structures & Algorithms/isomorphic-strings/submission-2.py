class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t= {}
        t_to_s= {}
        for s_str, t_str in zip(s,t):
            if (s_str in s_to_t) and (t_str != s_to_t[s_str]):
                return False
            if (t_str in t_to_s) and (s_str != t_to_s[t_str]):
                return False
            s_to_t[s_str] = t_str
            t_to_s[t_str] = s_str
        return True
            
