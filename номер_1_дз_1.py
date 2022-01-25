import random



def check_1(lst_obj):
   
    lst_to_set = set(lst_obj)  
    return lst_to_set  



def check_2(lst_obj):
   
    for f in range(len(lst_obj)):          
        if lst_obj[f] in lst_obj[f+1:]:    
            return False                   
    return True                            



def check_3(lst_obj):
    
    lst_copy = list(lst_obj)                 
    lst_copy.sort()                          
    for i in range(len(lst_obj) - 1):        
        if lst_copy[i] == lst_copy[i+1]:     
            return False                     
    return True                              


for f in (50, 500, 1000, 5000, 10000):
   
    lst = random.sample(range(-100000, 100000), f)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))