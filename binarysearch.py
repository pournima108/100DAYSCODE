# def binarySearch(arr,l,r,x):
#     if r>=l:
#         mid =l+(r-l)//2
#         if arr[mid]==x:
#             return mid
#         elif arr[mid]>x:
#             return binarySearch(arr,l,mid-1,x)
#         else:
#             return binarySearch(arr,mid+1,r,x)
#     else:
#          return -1

from bisect import bisect_left,bisect_right
def left_Occurence_BinarySearch(arr,x):
    i=bisect_left(arr,x)
    print(i)

    if i!=len(arr) and arr[i]==x:
        return i
    else:
        return -1


def right_Occurence_BinarySearch(arr,x):
    i=bisect_right(arr,x)
    print(i)
    if i!=len(arr)+1 and arr[i-1]==x:
        return i
    else:
        return -1

arr=[2,7,4,5,7,9]
x=7
left_result = left_Occurence_BinarySearch(arr,x)
right_result= right_Occurence_BinarySearch(arr,x)

if left_result!=-1 and right_result!=-1:
    print("element is",left_result,right_result)
else:
    print("element is not in array")
        
    