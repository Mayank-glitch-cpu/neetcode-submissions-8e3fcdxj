class Trienode:
    def __init__(self):
        self.children={}
        self.EndOfWord=False

class PrefixTree:

    def __init__(self):
        self.root= Trienode()

    def insert(self, word: str) -> None:
        curr= self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]= Trienode()
            curr= curr.children[c]
        curr.EndOfWord= True

    def search(self, word: str) -> bool:
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr= curr.children[c]
        return curr.EndOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr= curr.children[c]
        return True
        