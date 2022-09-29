def dosyalama(x):
    
    for i in x:
        if isinstance(i,list):
            dosyalama(i)
        else:
            empty_list.append(i)
    
    

x= [[1,'a',['cat'],2],[[[3]],'dog'],4,5] 
empty_list = [] 
dosyalama(x)
print(empty_list)