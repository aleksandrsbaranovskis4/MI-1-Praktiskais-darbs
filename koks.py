class Node:
    def __init__(self, num, score=0, bank=0, move=None, parent=None):
        self.num = num
        self.score = score
        self.bank = bank
        self.move = move
        self.parent = parent
        self.child = []
        self.final_score = None

    def is_terminal(self):
        return self.num >= 3000

    def compute_final_score(self):
        if self.score % 2 == 0:
            self.final_score = self.score - self.bank
        else:
            self.final_score = self.score + self.bank
    
    def winner(self):
        if self.final_score == 0:
            return "Tie?"
        elif self.final_score % 2 == 0:
            return "Player 1"
        else:
            return "Player 2"

def build_tree(node):
    if node.is_terminal():
        node.compute_final_score()
        return
    
    for multiplier in [3, 4, 5]:
        new_num = node.num * multiplier
        new_score = node.score + (1 if new_num % 2 == 0 else -1)
        new_bank = node.bank + (1 if new_num % 10 in (0, 5) else 0)
        
        child = Node(new_num, new_score, new_bank, move=multiplier, parent=node)
        node.child.append(child)
        build_tree(child)

def print_tree(node, indent=0):
    prefix = " " * indent
    if node.move is not None:
        move_str = f"(x{node.move}) "
    else:
        move_str = ""
    
    if node.is_terminal():
        print(f"{prefix}{move_str}num: {node.num}, Score: {node.score}, Bank: {node.bank} | Final Score: {node.final_score} | Winner: {node.winner()}")
    else:
        print(f"{prefix}{move_str}num: {node.num}, Score: {node.score}, Bank: {node.bank}")
    
    for child in node.child:
        print_tree(child, indent + 4)

def main():
    for num in range(20, 31):
        root = Node(num)
        build_tree(root)
        print_tree(root)

if __name__ == "__main__":
    main()