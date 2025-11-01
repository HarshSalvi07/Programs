arr = [10,20,30,40,50,60]
for i in arr:
    print(i, end=' ')

arr.append(70)
print("Appended array list: ",arr)

arr.insert(2,25)
print("Inserted array list: ",arr)

if 25 in arr:
    print("Element found!")
else:
    print("Element not found!")

print(arr.index(25))

arr[2] = 26
print(arr)