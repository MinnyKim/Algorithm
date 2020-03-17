# 와! 누가 내 코드를 읽었대! 너무 뿌듯해!!
# 오늘은 3월 11일 목표는 3개 풀기

# 두번째로 큰 정수 출력
# a,b,c = map(int, input().split())
# list1 = [a,b,c]
# list1.sort()
# print(list1[1])

# 구구단 이지이지
# n = int(input())
# for i in range(1, 10):
#     print(f'{n} * {i} = {n*i}')

# a+b 출력

# 런타임 에러남
# t = int(input())
# list2 = []
# for i in range(0, 5):
#     a,b = map(int, input().split())
#     list2.append([a,b])
#
# for j in range(t):
#     print(list2[j][0]+list2[j][1])


# 그냥 뭔가 t가 문제 인거 같아서 바꿨는데 왜 위에꺼는 백준에서 런타임 에러가 날까?


# t = int(input())
# list2 = []
# for i in range(t):
#     a, b = map(int, input().split())
#     list2.append([a, b])
#
# for j in range(0, len(list2)):
#     print(list2[j][0] + list2[j][1])

# 1~n 까지의 합
# n = int(input())
# sum = 0
# for i in range(1, n+1):
#     sum += i
# print(sum)

# 빠른 a+b 출력
import sys
t = int(sys.stdin.readline())
list3 = []
for i in range(t):
    a,b = map(int, sys.stdin.readline().split())
    list3.append([a,b])

for j in range(0, len(list3)):
    print(list3[j][0]+list3[j][1])


