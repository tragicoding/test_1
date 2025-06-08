def merge(arr1,arr2):
    n1=len(arr1)
    n2=len(arr2)
    p1=0
    p2=0

    arr_merged=[]
    while p1<n1 and p2<n2:
        if arr1[p1] <=arr2[p2]:
            arr_merged.append(arr1[p1])
            p1+=1
        else:
            arr_merged.append(arr2[p2])
            p2+=1
    while p1<n1:
        arr_merged.append(arr1[p1])
        pq+=1
    while p2<n2:
        arr_merged.append(arr2[p2])

arr1=[2,4,6,8,11,13]
arr2=[1,2,3,4,9,16,21]
arr=merge(arr1,arr2)