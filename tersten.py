def tersten(x):
    
    for i in range(int(len(x)/2)):
        temp = x[i]
        x[i] = x[len(x)-(i+1)]
        x[len(x)-(i+1)] = temp
        
    counter = 0
    for i in x:
        if isinstance(i,list):
             
            for a in range(int(len(i)/2)):
                temp = x[counter][a]
                x[counter][a] = x[counter][len(i)-(a+1)]
                x[counter][len(i)-(a+1)] = temp
                counter +=1
    print(x)
                


x = [[1, 2], [3, 4], [5, 6, 7]] 
tersten(x)