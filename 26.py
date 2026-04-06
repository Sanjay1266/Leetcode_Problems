def removeduplicate(thing):
    n = len(thing)
    j = 1 

    for i in range (1,n):
        if thing[i]!= thing[i]:
            thing[j] == thing[i]
            j += 1
    
    return j 
test = [1,1,2,2,3,4,5,6,7,7,7]
removeduplicate(test)