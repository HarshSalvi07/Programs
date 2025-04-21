def swap(L,x,y):
    temp = L[x]
    L[x] = L[y]
    L[y] = temp

def bubbleSort(list):
    for i in range(len(list)):
        for k in range(len(list)-1,i,-1):
            if(list[k]<list[k-1]):
                swap(list,k,k-1)

    return list;

list=[1,2,36,5,89,3,67]
print("Unsorted list: ",list)
print("Sorted list: ",bubbleSort(list))

    
    
