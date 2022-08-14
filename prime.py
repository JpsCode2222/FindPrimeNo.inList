A=[10,3,30,40,5,60,70,80,90,100]
B=[]
C=[]
for i in A:
    for j in range(2,i):
        flage=False
        if i % j == 0:
            flage=True
            break
    if flage == True:
        C.append(i)
    else:
        B.append(i)
print('prime no in list: ')
print(B)
print('non prime no in list: ')
print(C)

