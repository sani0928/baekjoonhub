import sys
input = sys.stdin.readline

n = int(input())
tree = {}
for _ in range(1, n + 1):
    node, left, right = input().split()
    tree[node] = (left, right)
prelst, inlst, postlst = [], [], []

def preorder(cur):
    if cur == '.':
        return
    l, r = tree[cur]
    prelst.append(cur)
    preorder(l)
    preorder(r)
    return

def inorder(cur):
    if cur == '.':
        return
    l, r = tree[cur]
    inorder(l)
    inlst.append(cur)
    inorder(r)
    return

def postorder(cur):
    if cur == '.':
        return
    l, r = tree[cur]
    postorder(l)
    postorder(r)
    postlst.append(cur)
    return

preorder('A'), inorder('A'), postorder('A')
print(''.join(prelst), ''.join(inlst), ''.join(postlst), sep = '\n')