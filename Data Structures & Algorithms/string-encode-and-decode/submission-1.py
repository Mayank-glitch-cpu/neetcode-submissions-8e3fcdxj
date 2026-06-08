class Solution:

    def encode(self, strs: List[str]) -> str:
        encoding= ''
        seperator = '#'
        for word in strs:
            l= str(len(word))
            encoding += l + seperator + word
        print(encoding)
        return encoding

    def decode(self, s: str) -> List[str]:
        res= []
        i=0

        while i < len(s):
            j=i
            while s[j] != '#':
                j+=1
            length= int(s[i:j])
            i=j+1
            res.append(s[i : i + length])
            i+=length
        print(res)
        return res
