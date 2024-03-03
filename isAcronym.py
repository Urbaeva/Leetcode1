def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        for i in range(len(words)):
            word = words[i]
            if word[0] != s[i]:
                return False
        return True
        
