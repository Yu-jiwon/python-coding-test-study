t = int(input())

d=[[0]*3 for _ in range(100001)]

d[1]=[1,0,0]
d[2]=[0,1,0]
d[3]=[1,1,1]

#미리 100001까지 계산을 해두고 그곳에서 원하는 값을 찾는게 시간초과가 안뜸    
for i in range(4,100001):
    d[i][0]=(d[i-1][1]+d[i-1][2])%1000000009 #나누기 안하면 시간초과 뜸
    d[i][1]=(d[i-2][0]+d[i-2][2])%1000000009
    d[i][2]=(d[i-3][0]+d[i-3][1])%1000000009
        

    
for _ in range(t):
    n = int(input())
    print(sum(d[n])%1000000009)
    
# 코드길이 : 343 B
# 시간 : 344 ms
# 메모리 : 50468 KB