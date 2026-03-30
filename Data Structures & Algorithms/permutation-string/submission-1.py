class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_1= [0]*26
        for char in s1:
            freq_1[ord(char)-ord('a')]+=1
        print(freq_1)

        freq_2= [0]*26
        left=0
        string=''
        while left<= len(s2)-len(s1):
            for right in range(left,left+ len(s1)):
                freq_2[ord(s2[right])-ord('a')]+=1
                string+=s2[right]
            print('freq 2 for string ',string,' ',freq_2)
            if freq_2 == freq_1:
                return True
            freq_2=[0]*26
            left+=1
            string=''
        return False