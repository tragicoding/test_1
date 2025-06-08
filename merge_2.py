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
        p1+=1
    while p2<n2:
        arr_merged.append(arr2[p2])
        
def merge_sort(arr):
    if len(arr)==1:
        print('single element:',arr)
        print()
        return arr

    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    left_sorted=merge_sort(left)
    right_sorted=merge_sort(right)
    print('mid:',mid)
    print('left:',left_sorted)
    print('right:',right_sorted)
    print()
    return merge(left_sorted,right_sorted)
arr=[5,6,4,8,3,7,9,0,1,5,2,3]
merge_sort(arr)