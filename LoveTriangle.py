
while(1):
    try:i=input()
    except(EOFError):break
    i=int(i)
    c=0
    s=""
    if i<9:
        print(i)
    else:
        while i:
            if(i<9):
                s=s+str(i)
                break
            s=s+str(i%9)
            i=i//9
        print(s[: :-1])
#Language: Python 3
