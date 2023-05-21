n = int(input())

d = [0]*31
d[2]=3

for i in range(4,n+1):
    if i%2==0:
        d[i]=d[i-2]*3 + sum(d[:i-2])*2+2 
        #d[i-2]의 경우의수에다가 3*2의 경우수 3가지를 곱함
        #그 다음은 *2를 함
        #이걸 다 더한 것이 경우의 수
    else:
        d[i]=0 #짝수로 계산해야되므로,, 2로 나누어 떨어지지 않으면 0
print(d[n])

# 코드길이 : 385 B
# 시간 : 40 ms
# 메모리 : 31256 KB