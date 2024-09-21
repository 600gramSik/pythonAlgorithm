m,n = map(int, input().split())
#숫자 입력
arr = list(map(int, input().split()))
#누적합을 위한 배열
#첫번째 요소를 0으로 한 이유는 만약 0이 아닌 빈 리스트로 선언을 하게 되면 밑에서 누적합 계산을 할 때 
#구간합이 맞지 않게 된다. 
cum = [0]
cum_sum = 0

for i in range(m):
    cum_sum+=arr[i]
    cum.append(cum_sum)
    
for j in range(n):
    a,b = map(int, input().split())
    result = cum[b] - cum[a-1]
    print(result)