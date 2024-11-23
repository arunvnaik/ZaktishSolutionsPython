# lst=[1,2,3,4,5,6,7,8,9,10]  


def sqrtnums(lst):
    new_lst=[]
    for x in lst :
        if x== 5 :
            continue 
        else :
            new_lst.append(x**x )
    return new_lst 

lst=[1,2,3,4,5,6,7,8,9,10]  
print(sqrtnums(lst)) 