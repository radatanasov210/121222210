n = int(input('Vuvedi chislo='))
a, b = 0,1
for i in range (1,n):
    sum = a + b
    a = b
    b = sum
    print(b)
