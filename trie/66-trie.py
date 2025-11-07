class Node:
    def __init__(self, val, child, isLeaf):
        self.val = val
        self.next = child
        self.isLeaf = isLeaf

class Trie:
    def __init__(self):
        self.root = Node('root', {}, False)

    def insert(self, word: str) -> None:
        root = self.root
        cur = self.root
        for i in range(len(word)):
            w = word[i]
            if w in cur.next:
                if i==len(word)-1:
                    cur.next[w].isLeaf = True
                cur = cur.next[w]
            else:
                next_node = Node(w, {}, i==len(word)-1)
                cur.next[w] = next_node
                cur = next_node

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            w = word[i]
            if w in cur.next:
                if i==len(word)-1:
                    if cur.next[w].isLeaf:
                        cur = cur.next[w]
                    else:
                        return False
                else:
                    cur = cur.next[w]
            else:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            w = prefix[i]
            if w in cur.next:
                cur = cur.next[w]
            else:
                return False
        return True