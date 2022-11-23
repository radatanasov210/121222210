n = int(input('Vuvedi chislo='))
sum = 0
for i in range(1,n):
    sum += int(str(n)*i)
    print(str(n)*i,end='')
    print('+',end='')
sum += int(str(n)*n)
print(str(n)*n,end='')
print('=',end='')
print(sum)
