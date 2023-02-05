class Solution:
    def sortSentence(self, s: str) -> str:
        a = list(s.split()) 
        a.sort(key=lambda x:x[len(x)-1])
        b = ''
        for i in a:
            b += i[:-1]
            b += ' '
        return b[:-1]
