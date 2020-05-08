# 수학1
# 부녀회장이 될테야
# sql 푸는 시기여서 민주는 알고리즘을 풉니다

# k층 n호 = k층 (n-1)호 + (k-1)층 n호


t = int(input())
case_list = []
for i in range(t):
    k = int(input())
    n = int(input())
    case_list.append([k,n])
# print(case_list)

for i in range(len(case_list)):
    x = case_list[i][0] + 1
    y = case_list[i][1]
    apt_list = [[0 for j in range(y)] for i in range(x)]
    for j in range(x):
        apt_list[j][0] = 1
    for j in range(y):
        apt_list[0][j] = j+1
    for j in range(1, x):
        for k in range(1, y):
            apt_list[j][k] = apt_list[j][k-1] + apt_list[j-1][k]
    print(apt_list[x-1][y-1])




'''
## 하나만 받아서 풀어보기
k = int(input())
n = int(input())

# apt_list = [[0]*n]*k
apt_list = [[0 for j in range(n)] for i in range(k)]
print(apt_list)
for i in range(k):
    apt_list[i][0] = 1
print(apt_list)
for i in range(n):
    apt_list[0][i] = i+1
print(apt_list)

for i in range(1, k):
    for j in range(1, n):
        apt_list[i][j] = apt_list[i][j-1] + apt_list[i-1][j]
print(apt_list)
'''

'''
for i in range(k):
    for j in range(n):
        a[k][i] = 
'''
# for j in range(n):
#     apt_list[0][j] = 1
# apt_list[k][n] = apt_list[k][n-1] + apt_list[k-1][n]