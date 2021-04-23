
L=int(input())
n=int(input())
for i in range(n):
    a,b=input().split()
    w=int(a)
    h=int(b)
    if w==h and w>=L and h>=L:
        print('ACCEPTED')
    elif w<L or h<L:
        print('UPLOAD ANOTHER')
    else:
        print('CROP IT')
Language: Python 3
