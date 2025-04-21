list = [1,4,6,32,38,99,546]

def binarySearching(list,key):
    start = 0
    end = len(list)-1
    while end >= start:
        mid = int((start+end)/2)
        if list[mid] == key:
            return True
        elif list[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return False

print(list)
print("32 in list: ",binarySearching(list,32))
print("546 in list: ",binarySearching(list,546))
print("69 in list: ",binarySearching(list,69))
    
