def input_nums(n):
    if isinstance(n,int)== False:
        return []
    a=[]
    for i in range(0,n):
        b= input('Enter a list element: ')
        if b.isnumeric()==True:
            b=int(b)
            a.append(b)
    return a
def sum_list(list):
    sum = 0
    b=0
    for i in range(len(list)):
        try:
            b=float(list[i])
        except:
            b=0
        finally:
            sum +=b
    return sum
def max_of_two(a,b):
    if isinstance(a,int)==True or isinstance(a,float)==True:
        if isinstance(b,int)==True or isinstance(b,float)==True:
            if b>a:
                return b
            else:
                return a
        else:
            return a
    elif isinstance(b,int)==True or isinstance(b,float)==True:
        return b
    else:
        return 
print(max_of_two(sum_list(input_nums(4)), sum_list(input_nums(3))))
print(max_of_two(sum_list([4, "AA@", 3.12, "1"]), "9.2"))
