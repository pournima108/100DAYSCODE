def partition(arr,high,low):
    pivot=arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j] < pivot:
            i=i+1
            arr[i], arr[j] = arr[j],arr[i]
    arr[i+1], arr[high]=arr[high], arr[i+1]
    return (i+1)
    
def qs(arr,low,high):
    if len(arr)==1:
        return arr
    if low < high:
        pv=partition(arr,high,low)
        qs(arr,low,pv-1)
        qs(arr,pv+1,high)

arr=[10,40,20,60,-1]
n=len(arr)
qs(arr,0,n-1)
for i in range(n):
    print(arr[i])
