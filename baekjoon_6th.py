# 오늘은 3월 12일
# 알고리즘 푸는데 조금씩 재밌어지는 중>3<
# 1~n 출력
# n = int(input())
# for i in range(n):
#     print(i+1)

# 현재 시간은 5시니깐 한시간동안 다섯문제 뿌신다
# 1~n 거꾸로 출력
# n = int(input())
# for i in range(n):
#     print(n-i)

# 뭔 a+b 출력은 맨날 해
# t = int(input())
# listA = []
# for i in range(t):
#     a,b = map(int, input().split())
#     listA.append([a,b])
# for j in range(0, len(listA)):
#     print(f'Case #{j+1}: {listA[j][0]+listA[j][1]}')

# 또또 a+b
# t = int(input())
# listB = []
# for i in range(t):
#     a,b = map(int, input().split())
#     listB.append([a,b])
# for j in range(0, len(listB)):
#     print(f'Case #{j+1}: {listB[j][0]} + {listB[j][1]} = {listB[j][0]+listB[j][1]}')

# 오랜만에 별찍기
# n = int(input())
# for i in range(n):
#     print('*'*(i+1))

# 2439
# 별찍기 2
# 와 이거 다음에 꼭 다시 풀어봐라 2439번 푸름이도 풀어보라해야지
n = int(input())
for i in range(n):
    print('{:>{}}'.format('*'*(i+1),n))



