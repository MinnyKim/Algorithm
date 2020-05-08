# 수학2
# 소수 찾기

n = int(input())
listN = map(int, input().split())
listN = list(listN)
# print(listN)

cnt = 0
for i in listN:
    n = 1
    sum = 0
    while True:
        if i == n:
            break
        if i % n == 0:
            sum += 1
        n += 1
    if sum == 1:
        cnt += 1
print(cnt)


# # 소수 찾아보기
# x = int(input())
#
# n = 1
# sum = 0
#
# while True:
#     if x == n:
#         break
#     if x%n == 0:
#         sum += 1
#     n += 1
# print(sum)
# # 여기서 sum이 1인거만 소수~