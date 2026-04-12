import sys
input = sys.stdin.readline

n = int(input().strip())

inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# inorder에서 각 값의 인덱스를 빠르게 찾기 위해 딕셔너리를 사용
inorder_index = [0] * (n + 1)

for i, value in enumerate(inorder):
    inorder_index[value] = i

preorder = []

stack = [(0, n - 1, 0, n - 1)]

while stack:
    in_left, in_right, post_left, post_right = stack.pop()

    if (in_left > in_right):
        continue

    # postorder의 마지막 요소는 항상 트리의 루트
    root = postorder[post_right]
    preorder.append(root)

    # 루트의 인덱스를 inorder에서 찾아서 왼쪽과 오른쪽 서브트리의 크기를 계산
    root_index = inorder_index[root]
    left_size = root_index - in_left

    # 스택은 LIFO -> 오른쪽을 먼저 넣고 왼쪽을 나중에 append
    # 실제 처리 순서는 root -> left -> right
    if (root_index + 1 <= in_right):
        stack.append(
            (
                root_index + 1,
                in_right,
                post_left + left_size,
                post_right - 1,
            )
        )

    if (in_left <= root_index - 1):
        stack.append(
            (
                in_left,
                root_index - 1,
                post_left,
                post_left + left_size - 1,
            )
        )

print(" ".join(map(str, preorder)))