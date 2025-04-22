from functools import reduce

def multiply(lst):
    product = 1
    for item in lst:
        product = product * item

    return product

def subtract(lst):
    return reduce(lambda x, y: x - y, lst)

def divide(lst):
    return reduce(lambda x, y: x / y, lst)


def expressions(string , target):
    integer = int(string)
    
    lst = []

    while integer:
        lst.append(integer%10)
        integer = integer // 10

    lst = lst[::-1]
    str_lst = list(map(str,lst))


    ans = []

    if sum(lst) == target:
        ans.append('+'.join(str_lst))

    if multiply(lst) == target:
        ans.append("*".join(str_lst))
    
    if subtract(lst) == target:
        ans.append('-'.join(str_lst))

    if 0 in lst:
        if len(set(lst)) == 1:
            ans.append('+'.join(str_lst)) 
            ans.append('-'.join(str_lst)) 
            ans.append('*'.join(str_lst)) 
    else:
        if divide(lst) == target:
            ans.append('/'.join(str_lst))

    return ans

print(expressions("123", 6))