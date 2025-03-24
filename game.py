import math

class GameNode:
    def __init__(self, num, score = 0, bank = 0, move = None, parent = None, depth = 0):
        self.num = num
        self.score = score
        self.bank = bank
        self.move = move
        self.parent = parent
        self.child = []
        self.depth = depth
        
    def add_child(self, child):
        self.child.append(child)

class GameTree:
    def __init__(self, root):
        self.root = None
    
    def is_terminal(self, node):
        return node.num >= 3000
    
    def create_tree(self, num, max_depth):
        self.root = GameNode(num)
        self.build_tree(self.root, max_depth)

    def build_tree(self, node, max_depth):
        if self.is_terminal(node) or node.depth >= max_depth:
            return
        else:
            for multiplier in [3, 4, 5]:
                new_num = node.num * multiplier
                new_score = node.score + (1 if new_num % 2 == 0 else -1)
                new_bank = node.bank + (1 if new_num % 10 in (0, 5) else 0)

                child = GameNode(new_num, new_score, new_bank, move=multiplier, parent=node)
                node.add_child(child)
                self.build_tree(child, max_depth)

def minimax(node, maximizing):
    if not node.child:
        return node.score
    
    if maximizing:
        best_val = -math.inf
        for child in node.child:
            val = minimax(child, False)
            best_val = max(best_val, val)
        return best_val
    else:
        best_val = math.inf
        for child in node.child:
            val = minimax(child, True)
            best_val = min(best_val, val)
        return best_val

def main():
    for i in range(20, 31):
        tree = GameTree(None)
        tree.create_tree(i, 10)
        print(minimax(tree.root, True))

if __name__ == "__main__":
    main()