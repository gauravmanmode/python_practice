class Node:
    def __init__(self, val = 0, next = None, prev= None):
        self.next = next
        self.prev = prev
        self.val = val

def main():
    A = Node(3, Node(4), Node(5))
    node = A
    while not node== None:
        print(node.val)
        node = node.next

if __name__ == "__main__":
    main()

   

    