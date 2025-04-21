def selectionSort(list):
    for i in range(len(list)):
        min = i
        for j in range(i+1,len(list)):
            if list[min] > list [j]:
                min = j
        list[min],list[i]=list[i],list[min]

    return list;

list=[1,5,3,6,587,54,8,33]
print("Unordered list: ",list)
print("Ordered list: ",selectionSort(list))
