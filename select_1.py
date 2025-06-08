

def str_mark(seq,im):
    marks=[]
    for i in range(len(seq)):
        if i==im:
            marks.append("*"+str(seq[i])+"*")
        else:
            marks.append(str(seq[i]))
    return '['+','.join(marks)+']'

arr=[4,3,5,1,8,6,7,9]
n=len(arr)
for i in range(n-1):  #n-1번의 pass
    print(f'{i+1}번째 pass')
    im=i #i인덱스 요소 기준으로 시작
    for j in range(i+1,n):     #n-i-1번 비교....
        if arr[j]<arr[im]:
            im=j
        print(j,str_mark(arr,im))
    arr[i],arr[im]=arr[im],arr[i]


