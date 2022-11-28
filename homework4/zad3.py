def list_avg(list,multiplier=1):
    if isinstance(multiplier,int)== False:
        return 'Error'
    b=0
    sum=0
    c=0
    for i in range(len(list)):
        try:
            b=float(list[i]) 
            c +=1
        except:
            b=0
        finally:
            sum +=b
    if c==0:
        print("Error:Division by 0")
        return
    else:
        return ((sum/c)*multiplier)
print(list_avg(['4', 1.5, "@7$", 3.5, (1, "hi")]))
print(list_avg(['6', 3, 3.0], 2))
print(list_avg(['%$', {}]))
print(list_avg([]))
