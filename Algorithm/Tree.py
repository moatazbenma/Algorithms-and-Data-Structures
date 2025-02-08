class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def in_order_traversal(root, result):
    if root:
        in_order_traversal(root.left, result)
        result.append(root.value)
        in_order_traversal(root.right, result)

def tree_sort(arr):
    if not arr:
        return []
    root = None
    for value in arr:
        root = insert(root, value)
    result = []
    in_order_traversal(root, result)
    return result

# Example usage:
arr = [3, 6, 8, 10, 1, 2, 1]
print(tree_sort(arr))
