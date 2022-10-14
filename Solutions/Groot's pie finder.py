n=[8, 4, 3, 2, 6, 5]
k=6

l=[]
dict1={}
for i in range(len(n)):
    if(n[i]==k):
        
        dict1[i]=n[i]
    for j in range(i+1,len(n)):
        if(n[i]+n[j]== k):
            l.append(n.index(n[i]))
            l.append(n.index(n[j]))
            
            dict1[k]=l
         
            
print(dict1)