def findTheRange(nop,lop):
    
#nop=5
    nop_l=[]

#lop=[[2, 4, 5], [1, 3, 6], [2, 4, 7]]

    for i in range(nop):
        
        nop_l.append(0)
        #print(nop_l)
    start=0
    end=0
    value=0
    for i in lop:
        
            
        value=i[-1]
        #print(i)
    
        #print(value)
        for k in range(i[0],i[1]):
                
            nop_l[k]+=value
            #print(max(nop_l),nop_l.index(max(nop_l)))
    op=[nop_l.index(max(nop_l)),nop_l.index(max(nop_l))+1,max(nop_l)]
    return(op)
    
    
s1=findTheRange(5, [[2, 4, 5], [1, 3, 6], [2, 4, 7]])
print(s1)