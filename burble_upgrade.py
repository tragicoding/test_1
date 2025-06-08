#버블정렬의 첫번째 개선
arr=[6,2,4,3,7,1,8,9]
n=len(arr)
for i in range(0,n-1):
    n_swap=0
    print(f'#{i+1}번째 pass')
    for j in range(n-1,i,-1):
        if arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            n_swap+=1
        print(j,arr)
    if n_swap==0:
        break

#버블 정렬의 두번째 개선선
arr=[5,2,3,1,6,8,9]
n=len(arr)
k=0
while k<n-1:
    last=n-1
    print(f"#{k+1} 번째 pass")
    for j in range(n-1,k,-1):
        if arr[j-1]>arr[j]:
           arr[j-1],arr[j]=arr[j],arr[j-1]
           last=j
        print(j,arr)
    print(f'the last swap index={last}')
    k=last

