def partition(arr,pl,pr):
    pivot=arr[(pl+pr)//2]
    while pl<=pr:
        while arr[pl]<pivot:
            pl+=1
        while arr[pr]>pivot:
            pr-=1
        if pl<=pr:
            arr[pl],arr[pr]=arr[pr],arr[pl]
            pl+=1
            pr-=1
    return pl

def quick_sort(arr,pl,pr):
    if pr<=pl:
        return
    div=partition(arr,pl,pr)
    quick_sort(arr,pl,div-1)
    quick_sort(arr,div,pr)

arr=[6,4,3,7,1,8,9]
quick_sort(arr,0,len(arr)-1)
print(arr)