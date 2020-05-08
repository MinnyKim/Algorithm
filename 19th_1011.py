# 수학1
# Fly me to the Alpha Centauri
# 와 이거 너무 어렵네 진짜루

t = int(input())
case_list = []
for i in range(t):
    x, y = map(int, input().split())
    case_list.append([x,y])
# print(case_list)

for i in case_list:
    distance = i[1] - i[0]
    n = 0
    while True:
        if distance <= n * (n+1):
            break
        n += 1
    if distance > n * (n-1) + n:
        print(2*n)
    else:
        print(2*n-1)


#
# # 하나로 해보기
# x = int(input())
# y = int(input())
#
# distance = y-x
#
# # 일반항 n(n+1)
# n = 0
# while True:
#     if distance <= n*(n+1):
#         break
#     n += 1
# if distance > n*(n-1) + n:
#     print(2*n)
# else:
#     print(2*n-1)

