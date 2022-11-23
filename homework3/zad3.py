arr = []
n=int(input('Vuvedi chislo='))
for i in range (0,n):
    a = int(input())
    arr.append(a)
print(arr)
b = int(input('Vuvedi 0 ili 1:'))
for i in range(0,n):
    if b==0:
        if i%2!=0:
            arr[i] += 5
    elif b==1:
        if i%2==0:
            arr[i] +=10
print(arr)
