class Node:
    def __init__(self, val, child, isLeaf):
        self.val = val
        self.next = child
        self.isLeaf = isLeaf

class Trie:
    def __init__(self):
        self.root = Node('root', [], False)

    def insert(self, word: str) -> None:
        root = self.root
        cur = self.root
        for i in range(len(word)):
            w = word[i]
            node_exists = False
            for neigh in cur.next:
                if neigh.val == w:
                    node_exists = True
                    if i==len(word)-1:
                        neigh.isLeaf = True
                    cur = neigh
            if node_exists is False:
                next_node = Node(w, [], i==len(word)-1)
                cur.next.append(next_node)
                cur = next_node

    def search(self, word: str) -> bool:
        cur = self.root
        for i in range(len(word)):
            w = word[i]
            node_exists = False
            for neigh in cur.next:
                if neigh.val == w:
                    if i==len(word)-1:
                        if neigh.isLeaf:
                            node_exists = True
                            cur = neigh
                    else:
                        node_exists = True
                        cur = neigh
                    break
            if node_exists is False:
                return False
        return True

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for i in range(len(prefix)):
            w = prefix[i]
            node_exists = False
            for neigh in cur.next:
                if neigh.val == w:
                    node_exists = True
                    cur = neigh
                    break
            if node_exists is False:
                return False
        return True

    def print_trie(self):
        def dfs(node, prefix=''):
            if node.val != 'root':
                print(prefix + node.val + ('*' if node.isLeaf else ''))
            for child in node.next:
                dfs(child, prefix + '  ')
        dfs(self.root)

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)