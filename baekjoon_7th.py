# 오늘은 3월 13일 배가 고프다 샌디치를 먹을까
# 지금 3시15분이니깐 오늘 최소 10문제 가능 홧팅

# 10871
# 수열에서 특정 숫자보다 작은 수 출력
# 와 이거 처음 보는 문법? 이다
# n,x = map(int, input().split())
# list1 = list(map(int, input().split()))
# list2 = []
# for i in range(n):
#     if list1[i] < x:
#         list2.append(list1[i])
# print(*list2)

# 10952
# while 문 사용하여 a+b (break 조건을 줌)
# list3 = []
# while True:
#     a, b = map(int, input().split())
#     if a == 0:
#         break
#     list3.append([a,b])
# for i in range(len(list3)):
#     print(list3[i][0]+list3[i][1])

# 10951
# while 문 사용하여 a+b (break 조건 안줌)
# 흑흑 이거 푼거 넘나 감뎡이라굿
# list4 = []
# while True:
#     try:
#         a,b = map(int, input().split())
#     except:
#         break
#     list4.append([a,b])
# for i in range(len(list4)):
#     print(list4[i][0]+list4[i][1])

# 1110
# 더하기 사이클 구하기
# n = int(input())
# if n < 10:
#     a = 0
#     b = n % 10
# else:
#     a = n // 10
#     b = n % 10
#
# cnt = 0
# while True:
#     c = a + b
#     d = c % 10
#     m = 10 * b + d
#     cnt += 1
#     if m < 10:
#         a = 0
#         b = m % 10
#     else:
#         a = m // 10
#         b = m % 10
#
#     if m == n:
#         break
# print(cnt)


# 이거 백준에서 개 짧게 푼ㄱㅓ,,
'''
n = int(input())
m = n
i = 0
while True:
    m = m % 10 * 10 + (m % 10 + m // 10) % 10
    i += 1
    if m == n:
        break
print(i)
'''

# 개 짧게 푼거 보고 다시 풀어보기
# n = int(input())
# m = n
# cnt = 0
# while True:
#     m = 10 * (m%10) + (m//10 + m%10)%10
#     cnt += 1
#     if m == n:
#         break
# print(cnt)

# 10818
# 최소, 최대
# 위에꺼가 훨씬 짧쥬
# n = int(input())
# list5 = list(map(int, input().split()))
# print(min(list5), max(list5))

# min = list5[0]
# max = list5[0]
# for i in range(n):
#     if min > list5[i]:
#         min = list5[i]
#     if max < list5[i]:
#         max = list5[i]
# print(min, max)

# 2562
# 리스트 안에서 최댓값
# 진짜 개고생했네 이거 하나가지고ㅡㅡ
list6 = []
while True:
    a = int(input())
    list6.append(a)
    if len(list6) == 9:
        break
# max = list6[0]
# for i in range(len(list6)):
#     if max < list6[i]:
#         max = list6[i]
#         idx = i+1
print(max(list6))
print(list6.index(max(list6))+1)

# 오늘 뿌듯한 하루였다 알차게 풀었따 히히


