def insertionSort(list):
    for e in list:
        i = list.index(e)
        while i < len(list)-1:
            if list[i] > list[i+1]:
                list[i],list[i+1] = list[i+1],list[i]
            else:
                break
            i -= 1
    return list;
list=[1,4,65,7,34,9,665]
print("Unsorted list: ",list)
print("Sorted list: ",insertionSort(list))
