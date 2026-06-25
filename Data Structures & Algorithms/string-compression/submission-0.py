class Solution:
    def compress(self, chars: List[str]) -> int:
        read = write = 0
        n = len(chars)

        while read < n:
            chars[write] = chars[read]
            write+=1
            j = read +1

            while j<n and chars[j]==chars[read]:
                j+=1

            if j - read > 1:
                for c in str(j - read):
                    chars[write]= c
                    write +=1
            
            read = j 
        return write