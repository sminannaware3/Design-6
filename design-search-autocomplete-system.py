# Time O(n log n + n)
# Space O(2n)
from heapq import *
class AutocompleteSystem:

    def __init__(self, sentences: List[str], times: List[int]):
        self.smap = dict(zip(sentences, times))
        self.input_s = ""


    def input(self, c: str) -> List[str]:
        if c == '#':
            if self.input_s in self.smap:
                self.smap[self.input_s] += 1
            else: self.smap[self.input_s] = 1
            self.input_s = ""
            return [] 
        else:
            self.input_s += c
            return self.search(self.input_s)
    
    def search(self, c:str) -> List[str]:
        hq = []
        for key in self.smap.keys():
            if key.startswith(c):
                heappush(hq, (-self.smap[key], key)) # O(n)
                # We need minHeap for value but maxHeap for string
                # Below code does not work 
                # because python cannot sort strings in reverse order
                # Thus need to use maxHeap with value and default min ordered strings
                #heappush(hq, (self.smap[key], key))
                # if len(hq) > 3:
                #     heappop(hq)
        # matchedStr = []
        # while len(hq) > 0:
        #     matchedStr.insert(0, heappop(hq)[1])
        # return matchedStr
        return [item[1] for item in nsmallest(3, hq)] 

# Time O(N * n + n + N log N)
# Space O(N * n)
from heapq import *
class AutocompleteSystem:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.matchingStr = []

    def insert(self, s: str): # TC: O(n) n length of string, SC: O(n + N) N total matching strings
        curr = self.root
        for c in s:
            if c not in curr.children:
                newNode = self.TrieNode()
                newNode.matchingStr.append(s)
                curr.children[c] = newNode
            else:
                curr.children[c].matchingStr.append(s)
            curr = curr.children[c]
        
    def __init__(self, sentences: List[str], times: List[int]):
        self.root = self.TrieNode()
        self.smap = {}
        for sentence, time in zip(sentences, times): # TC: O(N) & TC of insert
            self.smap[sentence] = time
            self.insert(sentence) 
        self.input_s = ""

    def input(self, c: str) -> List[str]: 
        if c == '#':
            if self.input_s in self.smap:
                self.smap[self.input_s] += 1
            else: 
                self.smap[self.input_s] = 1
                self.insert(self.input_s)  # TC: O(n)
            self.input_s = ""
            return [] 
        else:
            self.input_s += c
            return self.search(self.input_s)
    
    def search(self, c:str) -> List[str]: # TC: O(n + N log N)
        hq = []
        curr = self.root
        matchedList = None
        for char in c:
            if char in curr.children:
                curr = curr.children[char]
            else: 
                curr = None
                break
        if curr != None:
            for s in curr.matchingStr:
                heappush(hq, (-self.smap[s], s)) 
        return [item[1] for item in nsmallest(3, hq)]

# Time O(N * n)
# Space O(3 + n*N)
from heapq import *
class AutocompleteSystem:

    class TrieNode:
        def __init__(self):
            self.children = {}
            self.matchingStr = []

    def insert(self, s: str): # TC: O(n) SC: O(3 + n)
        curr = self.root
        for c in s:
            if c not in curr.children:
                newNode = self.TrieNode()
                newNode.matchingStr.append(s)
                curr.children[c] = newNode
            elif s not in curr.children[c].matchingStr:
                curr.children[c].matchingStr.append(s)
            matchingStrList = sorted(curr.children[c].matchingStr, key=lambda item: (-self.smap[item], item))
            if len(matchingStrList) > 3:
                matchingStrList.pop()
            curr.children[c].matchingStr = matchingStrList
            curr = curr.children[c]
        
    def __init__(self, sentences: List[str], times: List[int]): #TC : O(N * insert)
        self.root = self.TrieNode()
        self.smap = {}
        for sentence, time in zip(sentences, times):
            self.smap[sentence] = time
            self.insert(sentence)
        self.input_s = ""

    def input(self, c: str) -> List[str]: 
        if c == '#':
            if self.input_s in self.smap:
                self.smap[self.input_s] += 1
            else: 
                self.smap[self.input_s] = 1
            self.insert(self.input_s) # TC O(n)
            self.input_s = ""
            return [] 
        else:
            self.input_s += c
            return self.search(self.input_s)
    
    def search(self, c:str) -> List[str]: # TC: O(n)
        curr = self.root
        for char in c:
            if char in curr.children:
                curr = curr.children[char]
            else: 
                curr = None
                break
        if curr != None:
            return curr.matchingStr
        return []

        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)       


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)