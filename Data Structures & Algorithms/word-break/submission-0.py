class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # dp solution  time O(n*m*t) space O(n); n is len(s), m is number fo words in dict and t is max lentgh of any word in dict
        dp= [False]* (len(s)+1)
        dp[len(s)]= True

        for i in range(len(s)-1,-1,-1):
            for word in wordDict:
                if (i+len(word))<= len(s) and s[i:i+len(word)]==word: # first check if there are enough character for comapring to s
                    dp[i]= dp[i+len(word)]
                if dp[i]:
                    break
        return dp[0]
