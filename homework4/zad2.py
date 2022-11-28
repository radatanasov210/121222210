n = int(input('Vuvedi chislo n='))
list=[]
list2=[]
don = {}
for i in range (n):
    a=input(("Kliuch:"))
    b = input('Stoinost:')
    don[a]=b
m = int(input('Vuvedi chislo m='))
for i in range (0,m):
    a = input('Vuvedi stoinost=')
    list.append(a)
for i in range (0,m):
    for a in don:
        if list[i]==a:
            list[i]=don[a]
            list2.append(a)
for i in range(len(list2)):
    del don[list2[i]]
print(don)
print(list)
