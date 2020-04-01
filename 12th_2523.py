# 실습 1
# 별찍기 -13
n = int(input())
for i in range(1, n+1):
    print('*'*i)
for i in range(n-1):
    print('*'*(n-i-1))