def quick_sort(arr):
    n=len(arr)
    if n<=1:
        return arr
    else:
        pivot=arr[0]
        less=[x for x in arr[1:] if x<=pivot]
        greater=[x for x in arr[1:] if x>pivot]
        return quick_sort(less)+[pivot]+quick_sort(greater)
    
arr=[6,4,8,3,1,9,7]
quick_sort(arr)


#시각구현

arr=[6,4,8,3,1,9,7]
def quick(arr):
    n=len(arr)
    if n<=1:
        if n>0:
            print("termival:",arr)
            print()
        return arr
    else:
        pivot=arr[0]
        less=[x for x in arr[1:] if x <pivot]
        greater= [x for x in arr[1:] if x>pivot]

        print('array:',arr)
        print('pivot:',pivot)
        print('less',less)
        print('greater:',greater)
        print()
        return quick(less)+[pivot]+quick(greater)

quick(arr)
    