class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        freq_1= [0]*26
        freq_2= [0]*26
        for i in range(len(s1)):
            freq_1[ord(s1[i])-ord('a')]+=1
            freq_2[ord(s2[i])-ord('a')]+=1
        print(freq_1)
        print(freq_2)
        for i in range(len(s1),len(s2)):
            if freq_2 == freq_1:
                return True
            freq_2[ord(s2[i])- ord('a')]+=1 # add new char
            freq_2[ord(s2[i-len(s1)])-ord('a')]-=1 # remove old char
        return freq_1== freq_2