n=int(input())
testcases=[]
for i in range(n):
    testcases.append(int(input()))
for i in range(n):
    r=testcases[i]%12;
    if r==0:
        print(str(testcases[i]-11)+" WS")
    elif r==1:
        print(str(testcases[i]+11)+" WS")
    elif r==2:
        print(str(testcases[i]+9)+" MS")
    elif r==3:
        print(str(testcases[i]+7)+" AS")
    elif r==4:
        print(str(testcases[i]+5)+" AS")
    elif r==5:
        print(str(testcases[i]+3)+" MS")
    elif r==6:
        print(str(testcases[i]+1)+" WS")
    elif r==7:
        print(str(testcases[i]-1)+" WS")
    elif r==8:
        print(str(testcases[i]-3)+" MS")
    elif r==9:
        print(str(testcases[i]-5)+" AS")
    elif r==10:
        print(str(testcases[i]-7)+" AS")
    elif r==11:
        print(str(testcases[i]-9)+" MS")
 
