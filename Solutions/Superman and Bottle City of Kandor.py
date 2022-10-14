l=([[[0.433, 200]], [[0.89, 400], [0.6, 300]]], [0.003, 0.005])
comp_out=l[-1] 
length_l=len(l)
outlist=[] 
#print(comp_out)
for item in range(length_l-1): 
    #print(l[i]) i=item
    for element in l[item]:
        #print(element)
        formula=0
        for value in element:
            #print(value)
            formula+=value[0]/value[1]
        outlist.append(formula)
#print(outlist)
for data in outlist:
    #print(data)
    if data>comp_out[0] and data<comp_out[1]:
        print(outlist.index(data))