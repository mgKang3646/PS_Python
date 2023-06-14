

n = int(input())
tree = {}

for _ in range(n) :
  parent, left, right = input().split()
  tree[parent] = [left,right]

def preorder(parent) :
  if parent != "." :
    print(parent,end="")
    preorder(tree[parent][0])
    preorder(tree[parent][1])

def inorder(parent) :
  if parent != "." :
    inorder(tree[parent][0])
    print(parent,end="")
    inorder(tree[parent][1])

def postorder(parent) :
  if parent != "." :
    postorder(tree[parent][0])
    postorder(tree[parent][1])
    print(parent,end="")


preorder("A")
print()
inorder("A")
print()
postorder("A")


          
  
