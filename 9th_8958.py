# OX 퀴즈
n = int(input())
list2 = []
for i in range(0, n):
    case = list(input().split('X'))
    list2.append(case)

# n까지 합 구하는 함수 정의
def nSum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

for i in range(0, n):
    score = 0
    for j in range(0, len(list2[i])):
        temp = len(list2[i][j])
        score += nSum(temp)
    print(score)



# 이렇게 짧게 풀 수 있다구...?
# 와 진짜 이게 찐 알고리즘 풀이 방법같아 소오오오름
import sys
N = int(sys.stdin.readline())
for i in range(N):
    quiz_result = sys.stdin.readline()
    accum = 1
    score = 0
    for q in quiz_result:
        if q is 'O':
            score += accum
            accum += 1
        else:
            accum = 1
    print(score)
