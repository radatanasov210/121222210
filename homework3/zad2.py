sum = 1
n = int(input('Vuvedi chislo='))
if n==0:
    print(1)
else:
    for i in range(1,n+1):
        sum = sum*i
print(sum)
