def findkthSmallest(arr,n,k):
    max=0

    for i in range(n):
        if (arr[i]>max):
            max= arr[i]
    print("max is",max)

    counter =[0]*(max+1)
    print (counter)
    smallest=0

    for i in range(n):
        # print("before",counter[arr[i]])
        print(i)
        counter[arr[i]] += 1
        print("after",counter[arr[i]])
    print("after",counter[arr[i]])

    for num in range(1,max+1):
        print("counter before",counter[num])
        print("number before is",num)
        print(counter[num]>0)
        if (counter[num]>0):
            print("counter after",counter[num])
            print("smallest is",smallest)
            smallest+=counter[num]
            print("smallest is",smallest)
            print("number is",num)

        if (smallest>=k):
            print(num)
            return num

if __name__ =="__main__":
    arr =[2,21,32,4,6,20,3,15]

    N=len(arr)
    K=5
    print(findkthSmallest(arr,N,K))
