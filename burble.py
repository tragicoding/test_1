arr=[3,6,4,1,7,9,8]
n=len(arr)
for i in range(1,n):#n-1번의 패스
    for j in range(n-1,i-1,-1):#비교시작
        if arr[j]<arr[j-1]:  #j(n-1)번쨰는 맨 마지막 요소
            arr[j-1],arr[j]=arr[j],arr[j-1]
print(arr)


#또는(+출력까지)....바깥 루프는 실행(패스)횟수, 안쪽 루프는 비교교
arr=[4,6,2,3,1,5,9,8]
n=len(arr)
for i in range(0,n-1):
    print(f"{i+1}번째 패스")
    for j in range(n-1,i,-1):
        if arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
        print(j,arr)