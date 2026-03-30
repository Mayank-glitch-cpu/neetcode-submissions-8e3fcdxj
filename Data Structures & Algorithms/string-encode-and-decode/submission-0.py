class Solution:

    def encode(self, strs: List[str]) -> str:
        seperator='#'
        encoding=''
        for string in strs:
            l=str(len(string))
            encoding+= l+seperator+string
        print(encoding)
        return encoding
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length= int(s[i:j]) # everything before j
            i = j+1
            res.append(s[i:i+length]) # append the string to result before the next #
            i+= length # reste i to i + length
        print(res)
        return res
