class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    # 노드 삽입
    def insert(self, data):
        # 트리가 비어있는 경우 새로운 노드를 루트로 설정
        if not self.root:
            self.root = Node(data)
            
            return

        # 트리가 비어있지 않은 경우 반복문으로 적절한 위치에 노드를 삽입
        current = self.root

        while True:
            if (data < current.data):
                if current.left is None:
                    current.left = Node(data)
                    
                    return
                
                current = current.left
                
            else:
                if (current.right is None):
                    current.right = Node(data)
                    
                    return
                
                current = current.right

    # postorder 순회 (left -> right -> root)
    def postorder(self):
        result = []

        if self.root is None:
            return result

        stack = [(self.root, False)]

        while stack:
            node, visited = stack.pop()

            if node is None:
                continue

            if visited:
                result.append(node.data)
                continue

            stack.append((node, True))
            stack.append((node.right, False))
            stack.append((node.left, False))

        return result

values = []

while True:
    try:
        token = input().strip()
        
    except EOFError:
        break

    if token:
        values.append(int(token))

tree = BST()

for value in values:
    tree.insert(value)

for value in tree.postorder():
    print(value)