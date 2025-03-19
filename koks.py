class Koks:
    def __init__(self, num, score=0, bank=0, move=None, parent=None):
        self.num = num
        self.score = score
        self.bank = bank
        self.move = move
        self.parent = parent
        self.child = []

    def is_terminal(self):
        return self.num >= 3000

    def build_tree(self, node):
        if node.is_terminal():
            return

        for multiplier in [3, 4, 5]:
            new_num = node.num * multiplier
            new_score = node.score + (1 if new_num % 2 == 0 else -1)
            new_bank = node.bank + (1 if new_num % 10 in (0, 5) else 0)

            child = Koks(new_num, new_score, new_bank, move=multiplier, parent=node)
            node.child.append(child)
            node.build_tree(child)

def print_tree(node, indent=0):
    prefix = " " * indent
    if node.move is not None:
        move_str = f"(x{node.move}) "
    else:
        move_str = ""
    
    print(f"{prefix}{move_str}num: {node.num}, Score: {node.score}, Bank: {node.bank}")
    
    for child in node.child:
        print_tree(child, indent + 4)
        
def main():
    root = Koks(21)
    root.build_tree(root)
    print_tree(root)

if __name__ == "__main__":
    main()