'''A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. 
There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.'''
class Trie(object):
    class Leaf(object):
        def __init__(self, s, is_full_word):
            self.s = s
            self.children = dict()
            self.is_full_word = is_full_word
        def FindChild(self, s):
            if s in self.children:
                return self.children[s]
            else:
                return None
        def AddChild(self, s, child):
            self.children[s] = child
        def GetChildrenQty(self):
            return len(self.children)
        def GetIsFullWord(self):
            return self.is_full_word
        def MakeFullWord(self):
            self.is_full_word = 1
            


    def __init__(self):
        self.root = self.Leaf('', 0)
        

    def insert(self, word):
        current_leaf = self.root
        for i in range(len(word)):
            s1 = word[:i+1]

            new_leaf = current_leaf.FindChild(s1)
            if not new_leaf:
                new_leaf = self.Leaf(s1, 1 if s1 == word else 0)
                current_leaf.AddChild(s1, new_leaf)
            elif s1 == word:
                new_leaf.MakeFullWord()
            
            current_leaf = new_leaf
        

    def search(self, word):
        current_leaf = self.root
        for i in range(len(word)):
            s1 = word[:i+1]
            new_leaf = current_leaf.FindChild(s1)
            if not new_leaf:
                return False
            else:
                if s1 == word and new_leaf.GetIsFullWord() == 0:
                    return False
                current_leaf = new_leaf
        return True
        

    def startsWith(self, prefix):
        current_leaf = self.root
        for i in range(len(prefix)):
            s1 = prefix[:i+1]
            new_leaf = current_leaf.FindChild(s1)
            if not new_leaf:
                return False
            else:
                current_leaf = new_leaf
        return True
        


# Your Trie object will be instantiated and called as such:
obj = Trie()
obj.insert('apple')
print(obj.search('apple'))
print(obj.search('app'))
print(obj.startsWith('app'))
obj.insert('app')
print(obj.search('app'))