# In this program I'm going to sort the list in increasing order,
#  so that the numbers will be ordered from the smallest to the largest.
myList = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = int(input("Enter a list element: "))
    myList.append(val)

while swapped:
    swapped = False
    for i in range(len(myList) - 1):
        if myList[i] > myList[i + 1]:
            swapped = True
            myList[i], myList[i + 1] = myList[i + 1], myList[i]

print("\nSorted:")
print(myList)
# If you want Python to sort your list, you can do it like this: 
# print(myList.sort())