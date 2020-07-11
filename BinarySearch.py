def binarySearch(arr,x):
    arr.sort()
    print(arr)
    min = 0
    max = len(arr)-1
    while min <= max:
        mid = (min + max)//2
        if arr[mid] == x:
            return True
        if arr[mid] > x:
            max = mid -1
        else:
            min = mid+1

    return False

def binarySearch2(arr,x,min,max):
    if min > max:
        return -1
    mid = (min+max)//2
    if arr[mid] == x:
        return True
    if arr[mid] > x:
        return binarySearch2(arr,x,min,mid-1)
    else:
        return binarySearch2(arr,x,mid+1,max)
    return False


def search(arr,x):  #Naive algorithm o(n)
    for i in arr:
        if i == x:
         return True
    return False








if __name__ == "__main__":
    a = [10,20,30,40,50,60]

    print(binarySearch(a,50))
    print(binarySearch2(a,50,0,len(a)-1))