class GameNode:
    def __init__(self, num, score=0, bank=0, move=None, parent=None):
        self.num = num
        self.score = score
        self.bank = bank
        self.move = move
        self.parent = parent
        self.child = []
        
    def add_child(self, child):
        self.child.append(child)

class GameTree:
    def __init__(self, root):
        self.root = None
    
    def is_terminal(self, node):
        return node.num >= 3000
    
    def create_tree(self, num):
        self.root = GameNode(num)
        self.build_tree(self.root)

    def build_tree(self, node):
        if self.is_terminal(node):
            return
        else:
            for multiplier in [3, 4, 5]:
                new_num = node.num * multiplier
                new_score = node.score + (1 if new_num % 2 == 0 else -1)
                new_bank = node.bank + (1 if new_num % 10 in (0, 5) else 0)

                child = GameNode(new_num, new_score, new_bank, move=multiplier, parent=node)
                node.add_child(child)
                self.build_tree(child)

def main():
    for i in range(20, 31):
        tree = GameTree(None)
        tree.create_tree(i)

if __name__ == "__main__":
    main()