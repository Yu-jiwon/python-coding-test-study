# 1->3,3->1, 5->5 이런식으로 사이클이 생겨야 하는 건 알겠다.
# 이걸 어떻게 구현해야 하는지는 모르겠다.

n = int(input())
num={}
for i in range(1,n+1):
    num[i]=int(input())

# dfs로 풀기
# 정점들을 돌면서 연결이 되는지 파악,,
