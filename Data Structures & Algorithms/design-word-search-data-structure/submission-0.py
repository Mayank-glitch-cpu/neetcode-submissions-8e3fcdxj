class Trienode:
    def __init__(self):
        self.child= {}
        self.isEnd= False

class WordDictionary:

    def __init__(self):
        self.root= Trienode()

    def addWord(self, word: str) -> None:
        curr= self.root
        for c in word:
            if c not in curr.child:
                curr.child[c]= Trienode()
            curr=curr.child[c]
        curr.isEnd= True

    def search(self, word: str) -> bool:
        # there will be two search 
        # one with no '.'
        # and with the '.'
        def dfs (i,node):
            curr= node
            for i in range(i,len(word)):
                if word[i]=='.':
                    for child in curr.child.values():
                        if dfs(i+1,child):
                            return True
                    return False
                else:
                    if word[i] not in curr.child:
                        return False
                    curr=curr.child[word[i]]
            return curr.isEnd
        return dfs(0,self.root)            
