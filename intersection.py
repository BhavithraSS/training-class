def intersection(lst1, lst2): 
    lst3 = [value for value in lst1 if value in lst2] 
    return lst3 
lst1 = int(input("inputyour values"))
lst2 =  int(input("inputyour values"))
print(intersection(lst1, lst2)) 
