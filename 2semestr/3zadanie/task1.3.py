class TrieNode:
    def __init__(self):
        self.children = {}  
        self.parent = None 
        self.is_end = False 
        self.output = None   

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Добавление слова в бор"""
        node = self.root
        for char in word:
            if char not in node.children:
                new_node = TrieNode()
                new_node.parent = node  
                node.children[char] = new_node
            node = node.children[char]
        node.is_end = True    
        node.output = word    
    
    def search(self, word):
        """Поиск слова в боре"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end and node.output == word
    
    
    def delete(self, word):
        """Удаление слова """
        node = self.root
        for char in word:
            if char not in node.children:
                return False 
            node = node.children[char]
        
        if not node.is_end:
            return False  

        node.is_end = False
        node.output = None

        while node != self.root and not node.children and not node.is_end:
            parent = node.parent
            for char, child in parent.children.items():
                if child is node:
                    del parent.children[char]
                    break
            node = parent
        
        return True

trie = Trie()

trie.insert("a")
trie.insert("art")
trie.insert("artrt")

print(trie.search("a"))       # True
print(trie.search("artr"))         # True
print(trie.search("blablablu"))    # False
