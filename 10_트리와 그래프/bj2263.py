import sys
input = sys.stdin.readline

n = int(input().rstrip())
inorder = list(map(int, input().rstrip().split()))
postorder = list(map(int, input().rstrip().split()))

idx = [0] * (n+1)
for i in range(n) :
    idx[inorder[i]] = i

def preorder(in_left, in_right, post_left, post_right) :
    if in_left > in_right or post_left > post_right :
        return
    
    root = postorder[post_right]
    print(root, end = " ")

    left = idx[root] - in_left
    right = in_right - idx[root]
    
    preorder(in_left, in_left+left-1, post_left, post_left+left-1)
    preorder(in_right-right+1, in_right, post_right-right, post_right-1)

preorder(0,n-1,0,n-1)