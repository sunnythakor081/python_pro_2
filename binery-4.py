
# binary search function for
def binarySearch(listOfArray,searchElement):
    low = 0
    high = len(listOfArray)-1
    while low <= high:
        mid = (low+high) // 2
        if(listOfArray[mid] == searchElement):
            return searchElement
        elif(listOfArray[mid] < searchElement):
            low = mid+1
        elif(listOfArray[mid] > searchElement):
            high = mid-1
    return False


# list of Array
listOfArray = [50, 10, 100, 20, 90, 30, 80, 40, 70, 60]

# Sort the List for Binary Search
listOfArray.sort()

def binarySearchusingRecursion(searchElement,low,high):
    global listOfArray
    if low <= high:
        mid = (low+high) // 2
        if(listOfArray[mid] == searchElement):
            return searchElement
        elif(listOfArray[mid] < searchElement):
            return binarySearchusingRecursion(searchElement,mid+1,high)
        elif(listOfArray[mid] > searchElement):
            # high = mid-1
            return binarySearchusingRecursion(searchElement,low,mid-1)
    else:
        return False



# User input for Search Element
searchElement = int(input("Enter Element Which you wann to search : "))

# Call the Function and Get the result back
resultElement = binarySearch(listOfArray,searchElement)
if(searchElement == resultElement):
    print(f"{searchElement} is found in list which is {resultElement}")
else:
    print(f"{searchElement} is not found in list which is {resultElement}")




print("Find using a Recursion")
low = 0
high = len(listOfArray)-1
resultElement = binarySearchusingRecursion(searchElement,low,high)
if(searchElement == resultElement):
    print(f"{searchElement} is found in list which is {resultElement}")
else:
    print(f"{searchElement} is not found in list which is {resultElement}")