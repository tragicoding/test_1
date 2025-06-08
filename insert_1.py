arr=[6,4,1,7,3,9,8]
n=len(arr)
for i in range(1,n):
    print(f'{i}번째 pass')
    cur=arr[i]
    j=0
    for j in range(i,0,-1):
        if arr[j-1]>cur:  #나보다 크면
            arr[j]=arr[j-1]  #뒤로가
            j-=1
            print(j,arr)
        else:
            print(j,arr)
            break
    arr[j]=cur
    print(arr)

#구현2
arr=[6,4,1,7,3,9,8]
n=len(arr)
for i in range(1,n):
    print(f'{i}번째 pass')
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
            print(j,arr)
        else:
            print(j,arr)
            break
