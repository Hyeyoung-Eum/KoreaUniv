from itertools import combinations
from copy import deepcopy


#지역 이름 받기
name_list = list(input().split())
n = len(name_list)

#인접행렬 값들 받기
shelter_matrix = list()
fire_matrix = list()
INF = int(1e9)

for i in range(n):
    row = list(map(int, input().split())) 
    for idx, val in enumerate(row):
        if val == 0 and idx != i:
            row[idx]=INF #연결되어 있지 않은 상태를 INF로 바꿔준다
    fire_line = deepcopy(row) # 소방서를 만들 때와 대피소를 만들 때, 필요한 정보를 분리하여 처리한다.
    shelter_matrix.append(row)
    fire_matrix.append(fire_line)

#소방차가 가는데 걸리는 시간
for i in range(n):
    for j in range(n):
        # 일반 주행 시 입력 받은 값보다 절반으로 줄음
        if fire_matrix[i][j] != INF: 
            fire_matrix[i][j] = shelter_matrix[i][j] // 2
        # 역주행 시 시간 2배 소요
        elif fire_matrix[i][j] == INF and fire_matrix[j][i] != INF:
            fire_matrix[i][j] = 2 * shelter_matrix[j][i]

print('')
print("1.가중치 조건 모두 반영된 matrix")
for x in fire_matrix:
    print(x)
print('')

print("2.소방소 설치 : 각 도시까지 가는데 걸리는 비용 계산")
# Floyd-Warshall Algorithm을 이용
for k in range(n):
    for i in range(n):
        for j in range(n):
            fire_matrix[i][j] = min(fire_matrix[i][j], fire_matrix[i][k]+fire_matrix[k][j])

for x in fire_matrix:
    print(x)
print('')

# 대피소 설치 : 각 도시까지 가는데 걸리는 비용 계산
# Floyd-Warshall Algorithm을 이용
for k in range(n):
    for i in range(n):
        for j in range(n):
            shelter_matrix[i][j] = min(shelter_matrix[i][j], shelter_matrix[i][k]+shelter_matrix[k][j])

# 대피소 건설에 필요한 최소 개수 찾기
flag = False 
s_num = 1 # 필요한 대피소 개수
while s_num <= n:
    for h in combinations(list(range(n)), s_num): # s_num의 수를 가지는 도시를 골라 각 조합 상황에서 대피소의 조건에 맞는지 확인한다.
        check = [INF] * n # check라는 배열을 만들어 그 도시에서 대피소까지 가는데 걸리는 시간을 계산한다.
        for h_val in h:
            for i in range(n):
                check[i]=min(check[i],shelter_matrix[i][h_val]) # 그 도시에서 대피소까지 가는데 걸리는 시간을 계산한다.
        if max(check) != INF: # 모든 도시에서 대피소를 접근 가능하다는 뜻
            for h_val in h:
                print(name_list[h_val], end=" ")
            flag = True 
        if flag:
            break
    if flag:
        break
    else:
        s_num += 1
print('')

# 소방서를 건설 최적화 위치 2개
ans = [-1, -1]
ans_val = INF
for x1, x2 in combinations(list(range(n)), 2): #조합을 이용하여, 모든 2개의 조합 경우의 수를 다 생각한다.
    check = [INF] * n 
    for idx, des in enumerate(fire_matrix[x1]):
        check[idx] = min(check[idx], des) #최소 시간 계산
    for idx, des in enumerate(fire_matrix[x2]):
        check[idx] = min(check[idx], des) 

    # 문제 상황에 맞는 값 출력
    if max(check) < ans_val:
        ans_val = max(check)
        ans[0], ans[1] = x1, x2

print(name_list[ans[0]], name_list[ans[1]])