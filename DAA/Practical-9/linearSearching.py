list = [44,543,23,75,898,1,243]

def linearSearching(list,key):
    for e in list:
        if e == key:
            return True
    return False

print("List: ",list)
print("23 in list: ",linearSearching(list,23))
print("243 in list: ",linearSearching(list,243))
print("69 in list: ",linearSearching(list,69))
