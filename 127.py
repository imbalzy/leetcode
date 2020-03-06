class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        b=[beginWord]
        lenword=len(beginWord)
        d=set()
        d.add(beginWord)
        i=0
        dic={}
        for word in wordList:
            for j in range(lenword):
                s=word[:j]+'_'+word[j+1:]
                if not s in dic:
                    dic[s]=[word]
                else:
                    dic[s].append(word)
        for j in range(lenword):
            s=beginWord[:j]+'_'+beginWord[j+1:]
            if not s in dic:
                dic[s]=[beginWord]
            else:
                dic[s].append(beginWord)
        while b:
            a=b
            b=[]
            i+=1
            for word in a:
                for j in range(lenword):
                    s=word[:j]+'_'+word[j+1:]
                    for n in dic[s]:
                        if not n in d:
                            if n==endWord:
                                return i+1
                            d.add(n)
                            b.append(n)
        return 0
