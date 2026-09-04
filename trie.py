class Trie:

    def __init__(self):
        self.d = {}
        

    def insert(self, word: str) -> None:
        current = self.d

        for char in word:
            if (char not in current):
                current[char] = {}

            current = current[char]
        
        current["#"] = True

        
    def search(self, word: str) -> bool:
        current = self.d

        for char in word:
            if char not in current:
                return False

            current = current[char]

        return "#" in current
        
    def startsWith(self, prefix: str) -> bool:
        current = self.d

        for char in prefix:
            if char not in current:
                return False

            current = current[char]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)



import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        class Trie:

            def __init__(self):
                self.d = {}

            def insert(self, string):
                current = self.d

                for letter in string:
                    if (letter not in current):
                        current[letter] = {}

                    current = current[letter]

                current["*"] = True

            def search(self, string):
                current = self.d

                # move to prefix
                for letter in string:
                    if (letter not in current):
                        return []

                    current = current[letter]

                result = []

                def dfs(node, word):
                    # when deja found 3 words
                    if len(result) == 3:
                        return

                    # when end of word
                    if "*" in node:
                        result.append(word)

                    for key in sorted(node.keys()):
                        if (key == "*"):
                            continue

                        dfs(node[key], word + key)

                dfs(current, string)

                return result

                    

            
        Triee = Trie()

        for string in products:
            Triee.insert(string)

        returning = []

        for i in range(len(searchWord)):
            prefix = searchWord[0:i + 1]
            returning.append(Triee.search(prefix))

        return returning





                    



                        